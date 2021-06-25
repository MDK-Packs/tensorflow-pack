import os
import sys
import subprocess
import datetime
import argparse
import shutil
from time import perf_counter
from junit_xml import TestSuite, TestCase
import yaml
import re
import six

# get the datetime, when the script got started
datetime_string = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# get the script's directory, where template and work folders are located / created
test_on_arm_base = os.path.dirname(os.path.abspath(sys.argv[0]))

last_stderr = ""
last_stdout = ""


def run_debug(device_name, debug_file_name):
    if "ARMCM0" == device_name:
        fvp_executable_name = "FVP_MPS2_Cortex-M0"
    elif "ARMCM0P" == device_name:
        fvp_executable_name = "FVP_MPS2_Cortex-M0plus"
    elif "ARMCM3" == device_name:
        fvp_executable_name = "FVP_MPS2_Cortex-M3"
    elif "ARMCM4" == device_name or "ARMCM4_FP" == device_name:
        fvp_executable_name = "FVP_MPS2_Cortex-M4"
    elif "ARMCM7" == device_name or "ARMCM7_SP" == device_name or "ARMCM7_DP" == device_name:
        fvp_executable_name = "FVP_MPS2_Cortex-M7"
    elif "ARMCM23" == device_name:
        fvp_executable_name = "FVP_MPS2_Cortex-M23"
    elif "ARMCM33" == device_name or "ARMCM33_DSP_FP" == device_name:
        fvp_executable_name = "FVP_MPS2_Cortex-M33"
    elif "ARMCM35P" == device_name or "ARMCM35P_DSP_FP" == device_name:
        fvp_executable_name = "FVP_MPS2_Cortex-M35P"
    elif "ARMCM55_DSP_FPU_MVE" == device_name:
        fvp_executable_name = "FVP_MPS2_Cortex-M55"
    elif "SSE-300-MPS3" == device_name:
        fvp_executable_name = "FVP_Corstone_SSE-300_Ethos-U55"
    else:
        fvp_executable_name = 0

    if fvp_executable_name:
        result = subprocess.run([fvp_executable_name, "--config-file", os.path.join(test_on_arm_base,
                                "templates", (fvp_executable_name + ".config")), "--cpulimit=10", debug_file_name], capture_output=True, text=True)
        last_stdout = result.stdout
        if 0 == result.returncode:
            # running the FVP itself was ok
            if 0 < result.stdout.find("~~~ALL TESTS PASSED~~~") and 0 > result.stdout.find("Error:"):
                # the tensorflow "ok" string is found and no additional "Error" from a fault handler
                Error = 0
            else:
                # running the test was no ok
                print(result.stdout)
                Error = 1
        else:
            # running the FVP itself was not ok
            print(result.stdout)
            print("fvp returncode not ok" + " (" + str(result.returncode) + ")")
            Error = 1
    else:
        print(">>>TEST Warning: No FVP available for Device - Skipping execution")
        Error = 1

    return Error


def build_cproj(toolchain, project_file_name):
    global last_stderr
    global last_stdout
    cbuild_script_name = "cbuild.sh"
    result = subprocess.run(
        [cbuild_script_name, project_file_name], capture_output=True, text=True)
    if result.returncode:
        print(result.stderr)
        last_stderr = result.stderr
        last_stdout = result.stdout
        debug_file_name = 0
    else:
        debug_file_name = os.path.join(os.path.join(os.path.dirname(
            project_file_name), ""), os.path.basename(project_file_name).rstrip(".cprj"))
        if "GCC" == toolchain:
            debug_file_name = debug_file_name + ".elf"
        else:
            debug_file_name = debug_file_name + ".axf"
        print(">>>TEST Build successful: " + debug_file_name)
    return debug_file_name


def sanitize_xml(unsanitized):
    """Uses a whitelist to avoid generating bad XML."""
    return re.sub(r'[^a-zA-Z0-9+_\-/\\.]', '', six.ensure_str(unsanitized))


def make_component_file_list(base_path ,srcs_list):
    replace_srcs = ''
    srcs_list = set(srcs_list)
    for src in srcs_list:
        if not src:
            continue
        ext = os.path.splitext(src)[1]
        if ext == '.h':
            category = "header"
        elif ext == '.c':
            category = "sourceC"
        elif ext == '.cc' or ext == '.cpp':
            category = "sourceCpp"
        else:
            continue
        clean_src = sanitize_xml(os.path.join(base_path,src))
        replace_srcs += '        <file category=\"' + \
                category + '\" name=\"' + clean_src + '\"/> \n'
    return replace_srcs


def create_cproj(cvariant, toolchain, device_name, source_list, test_name, tflm_path):
    test_directory_name = os.path.join(
        test_on_arm_base, "work", cvariant, toolchain, device_name)
    template_directory_name = os.path.join(
        test_on_arm_base, "templates", cvariant, toolchain, device_name)

    template_file_name = os.path.join(
        template_directory_name, device_name) + ".cprj"
    template_file = open(template_file_name, "rt")
    if template_file:
        test_executable_name = os.path.basename(test_name).rstrip(".cc")
        cproj_file_name = os.path.join(
            test_directory_name, test_executable_name) + ".cprj"
        cproj_file = open(cproj_file_name, "wt")
        if cproj_file:
            for input_line in template_file:
                if 0 < input_line.find("_executable_to_test"):
                    output_line = input_line.replace(
                        '_executable_to_test', test_executable_name)
                elif 0 < input_line.find("_file_block_xml_"):
                    replacement_str = make_component_file_list(tflm_path, source_list)
                    output_line = input_line.replace(
                        '_file_block_xml_', replacement_str)
                else:
                    output_line = input_line
                cproj_file.write(output_line)
            cproj_file.close()
            try:
                shutil.copytree(os.path.join(template_directory_name, "RTE"), os.path.join(
                    test_directory_name, "RTE"))
            except:
                e = sys.exc_info()[0]
                print(">>>TEST Skipping copy of RTE folder. Reason: ", e)
        else:
            print("could not create cprj file")
            cproj_file_name = 0
        template_file.close()
    else:
        print("template file does not exist")
        cproj_file_name = 0

    return cproj_file_name


def run_test_on_arm_yml(cvariant, toolchain, device_name, tflm_path, test_list, log_file, junit_report):
    total_counter = 0
    success_counter = 0
    failure_counter = 0
    global last_stderr
    global last_stdout

    for test in test_list:        
      # for test purpose do not all
      # if 1 <= total_counter:
      #  break
      total_counter = total_counter + 1
      last_stderr = ""
      last_stdout = ""
      
      testname = [key for key in test.keys()][0]

      if device_name:
          print(">>>TEST Generating test project: " + testname + " on device=" +
                device_name + " toolchain=" + toolchain + " cvariant=" + cvariant)
          startTime = perf_counter()
          cproj_file_name = create_cproj(
              cvariant, toolchain, device_name, test['sources'], testname, tflm_path)
          tcname = device_name + ":" + toolchain + ":" + cvariant
          if cproj_file_name:
              debug_file_name = build_cproj(toolchain, cproj_file_name)
              if debug_file_name:
                  Error = 0
                  Error = run_debug(device_name, debug_file_name)
                  tc = TestCase(classname=testname, name=tcname, elapsed_sec=(
                      perf_counter() - startTime))
                  if 0 == Error:
                      tc = TestCase(classname=testname, name=tcname, elapsed_sec=(
                          perf_counter() - startTime), stderr=last_stderr, stdout=last_stdout)
                      print(">>>TEST All Tests passed: " + testname)
                      log_file.write(", %s" % "success")
                      success_counter = success_counter + 1
                      junit_report.append(tc)
                  else:
                      tc = TestCase(classname=testname, name=tcname, elapsed_sec=(
                          perf_counter() - startTime), stderr=last_stderr, stdout=last_stdout)
                      print(">>!TEST failure: tests failed " +
                            testname)
                      log_file.write(", %s" % "failure: debug result")
                      tc.add_failure_info(
                          "Unit Tests report failed Tests")
                      failure_counter = failure_counter + 1
                      junit_report.append(tc)
              else:
                  tc = TestCase(classname=testname, name=tcname, elapsed_sec=(
                      perf_counter() - startTime), stderr=last_stderr, stdout=last_stdout)
                  print(">>!TEST failure: build failed: " + testname)
                  log_file.write(", %s" % "failure: debug file")
                  tc.add_failure_info("CMSIS Build reports failure")
                  failure_counter = failure_counter + 1
                  junit_report.append(tc)
          else:
              tc = TestCase(classname=testname, name=tcname, elapsed_sec=(
                  perf_counter() - startTime), stderr=last_stderr, stdout=last_stdout)
              print(">>!TEST failure: project generation failed" +
                    testname)
              log_file.write(", %s" % "failure: cprj file")
              tc.add_failure_info("Test project creation failed")
              failure_counter = failure_counter + 1
              junit_report.append(tc)
      else:
          log_file.write(", %s" % testname[testname.find(
              "tensorflow/lite/micro"):len(testname)])

    return [total_counter, success_counter, failure_counter]



def run_test_on_arm_path(cvariant, toolchain, device_name, search_path, log_file, junit_report):
    total_counter = 0
    success_counter = 0
    failure_counter = 0
    global last_stderr
    global last_stdout

    for file_name in os.listdir(os.path.join(os.getcwd(), search_path)):
        if file_name.endswith("_test.cc"):
            # for test purpose do not all
            # if 1 <= total_counter:
            #  break
            total_counter = total_counter + 1
            test_file_name = os.path.join(search_path, file_name)
            last_stderr = ""
            last_stdout = ""

            if device_name:
                print(">>>TEST Running test unit: " + file_name + " on device=" +
                      device_name + " toolchain=" + toolchain + " cvariant=" + cvariant)
                startTime = perf_counter()
                cproj_file_name = create_cproj(
                    cvariant, toolchain, device_name, test_file_name)
                tcname = device_name + ":" + toolchain + ":" + cvariant
                if cproj_file_name:
                    debug_file_name = build_cproj(toolchain, cproj_file_name)
                    if debug_file_name:
                        Error = 0
                        Error = run_debug(device_name, debug_file_name)
                        tc = TestCase(classname=file_name, name=tcname, elapsed_sec=(
                            perf_counter() - startTime))
                        if 0 == Error:
                            tc = TestCase(classname=file_name, name=tcname, elapsed_sec=(
                                perf_counter() - startTime), stderr=last_stderr, stdout=last_stdout)
                            print(">>>TEST All Tests passed: " + test_file_name)
                            log_file.write(", %s" % "success")
                            success_counter = success_counter + 1
                            junit_report.append(tc)
                        else:
                            tc = TestCase(classname=file_name, name=tcname, elapsed_sec=(
                                perf_counter() - startTime), stderr=last_stderr, stdout=last_stdout)
                            print(">>!TEST failure: tests failed " +
                                  test_file_name)
                            log_file.write(", %s" % "failure: debug result")
                            tc.add_failure_info(
                                "Unit Tests report failed Tests")
                            failure_counter = failure_counter + 1
                            junit_report.append(tc)
                    else:
                        tc = TestCase(classname=file_name, name=tcname, elapsed_sec=(
                            perf_counter() - startTime), stderr=last_stderr, stdout=last_stdout)
                        print(">>!TEST failure: build failed: " + test_file_name)
                        log_file.write(", %s" % "failure: debug file")
                        tc.add_failure_info("CMSIS Build reports failure")
                        failure_counter = failure_counter + 1
                        junit_report.append(tc)
                else:
                    tc = TestCase(classname=file_name, name=tcname, elapsed_sec=(
                        perf_counter() - startTime), stderr=last_stderr, stdout=last_stdout)
                    print(">>!TEST failure: project generation failed" +
                          test_file_name)
                    log_file.write(", %s" % "failure: cprj file")
                    tc.add_failure_info("Test project creation failed")
                    failure_counter = failure_counter + 1
                    junit_report.append(tc)
            else:
                log_file.write(", %s" % test_file_name[test_file_name.find(
                    "tensorflow/lite/micro"):len(test_file_name)])

    return [total_counter, success_counter, failure_counter]


def get_test_devices(template_folder_name):
    return [d for d in os.listdir(template_folder_name) if os.path.isdir(os.path.join(template_folder_name, d))]


def main():
    test_error = 0
    # create the argument parser
    parser = argparse.ArgumentParser(
        description="Run tensorflow-lite-micro tests on Arm VFPs.")
    # add the --tflm_path option
    parser.add_argument("--tflm_path", type=str, default=os.path.curdir,
                        help="path, basepath for sources from inventory")
    parser.add_argument("--toolchain", type=str, default="ARMCLANG",
                        help="toolchain to build the tests with (ARMCLANG, GCC)")
    parser.add_argument("--cvariant", type=str, default="CMSIS-NN",
                        help="variant of tensorflow lite micro to use (Reference, CMSIS-NN, Ethos-U)")
    parser.add_argument("--inventory", type=str, default="",
                        help="yml file with a list of tests and sources for complex tests")

    # parse the arguments
    arguments = parser.parse_args()
    tflm_path = arguments.tflm_path
    toolchain = arguments.toolchain
    cvariant = arguments.cvariant
    inventory_file = arguments.inventory
    # get the availabe test devices from the template folder
    test_devices = get_test_devices(os.path.join(
        test_on_arm_base, "templates", cvariant, toolchain))
    # create a logfile for collecting high-level results in a csv file
    log_file = open(os.path.join(test_on_arm_base,
                    "test_on_arm_results_") + datetime_string + ".csv", "w")
    log_file.write("%s %s %s" % (datetime_string, cvariant, toolchain))
    # without device name, create the top column with file names in the csv logfile
    result = run_test_on_arm_path(0, 0, 0, tflm_path, log_file, 0)

    
    with open( os.path.abspath(inventory_file), "r") as ymlfile:
      inventory = yaml.safe_load(ymlfile)

    # Open the junit format test report file
    test_folder = os.path.basename(os.path.normpath(tflm_path))
    test_report_fn = test_folder + ".junit"
    junit_file = open(os.path.join(test_on_arm_base, test_report_fn), "w")
    print(">>>TEST Writing report to ", junit_file)
    junit_cases = []

    if inventory_file:
        # threre are some files to test
        device_counter = 0
        for test_device in test_devices:
            # for test purpose do not all devices
            # if test_device != "ARMCM3":
            #  continue
            # test each *_test.cc for this device
            device_counter = device_counter + 1
            print(">>>TEST Testing on device:", test_device)
            work_path_name = os.path.join(
                test_on_arm_base, "work", cvariant, toolchain, test_device)
            if os.path.exists(work_path_name):
                # clean old work folder
                shutil.rmtree(work_path_name)
            # create work folder
            os.makedirs(work_path_name)
            log_file.write("\n%s" % test_device)
            for key, value in inventory.items():
              print(">>>TEST Test Suite: ", value['readable'])
                #for test in value['tests']: 
                #  print(test)
                #  for source in test['sources']:
                #  print(source)
              result = run_test_on_arm_yml(cvariant, toolchain, test_device, tflm_path, value['tests'] , log_file, junit_cases)
              print("total:", result[0], "success:",
                  result[1], "failure:", result[2])
            if result[2]:
                # something went wrong
                test_error = 1
    else:
        print("Error: no files to test in \"",
              tflm_path, "\", use --tflm_path option!")
        test_error = 1
    properties = {"cvariant": cvariant, "toolchain": toolchain}
    junit_report = TestSuite(
        "Tensorflow Tests", junit_cases, package=test_folder, properties=properties)
    TestSuite.to_file(junit_file, [junit_report], prettyprint=False)
    junit_file.close()

    log_file.write("\n")
    log_file.close()

    #sys.exit( test_error )


if __name__ == '__main__':
    main()
