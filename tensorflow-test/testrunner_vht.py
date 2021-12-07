import os
import sys
import subprocess
import datetime
import argparse
import shutil
from time import perf_counter
import yaml
import re
import six

# get the datetime, when the script got started
datetime_string = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# get the script's directory, where template and work folders are located / created
test_on_arm_base = os.path.dirname(os.path.abspath(sys.argv[0]))

last_stderr = ""
last_stdout = ""


def create_run_command(device_name, debug_file_name):
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
        run_command_string = fvp_executable_name + " --config-file " + os.path.join(test_on_arm_base,"templates", (fvp_executable_name + ".config")) + " --cpulimit=10"
    else:
        run_command_string = 0


    return run_command_string


def add_case_vht_yml(toolchain, project_file_name):
    global last_stderr
    global last_stdout

    cbuild_script_name = "cbuild.sh"
    build_command = cbuild_script_name + project_file_name

    print (build_command)


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
        test_on_arm_base, "vht", cvariant, toolchain, device_name)
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
                #print(">>>TEST Skipping copy of RTE folder. Reason: ", e)
        else:
            print("could not create cprj file")
            cproj_file_name = 0
        template_file.close()
    else:
        print("template file does not exist")
        cproj_file_name = 0

    return cproj_file_name



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
    test_devices = get_test_devices(os.path.join(test_on_arm_base, "templates", cvariant, toolchain))
    print (test_on_arm_base)
    # create a logfile for collecting high-level results in a csv file
    #log_file = open(os.path.join(test_on_arm_base, "test_on_vht_setup_log") + datetime_string + ".csv", "w")
    #log_file.write("%s %s %s" % (datetime_string, cvariant, toolchain))
    # without device name, create the top column with file names in the csv logfile
    # print ("logfile and testfolder ", tflm_path, " ",log_file)
    #result = add_case(0, 0, 0, tflm_path, log_file, 0)
    
    with open( os.path.abspath(inventory_file), "r") as ymlfile:
      inventory = yaml.safe_load(ymlfile)

    vht_yml_data = dict(
        suite = dict(
            name = "tensorflow-lite-micro-tests",
            model = "VHT-Corstone-300",
            configuration = "",
            working_dir = "/home/ubuntu/vhtwork",
            pre="",
            post="",
            
            builds = [],
            tests = []
        )
    )


    with open('data.yml', 'w') as outfile:
       yaml.dump(vht_yml_data, outfile, default_flow_style=False)


    # Open the vht.yml 
    #junit_file = open(os.path.join(test_on_arm_base, test_report_fn), "w")
    #print(">>>TEST Writing report to ", junit_file)
    junit_cases = []

    if inventory_file:
        # threre are some files to test
        device_counter = 0
        for test_device in test_devices:
            print(">>>TEST Testing on device:", test_device)
            work_path_name = os.path.join(
                test_on_arm_base, "vht", cvariant, toolchain, test_device)
            if os.path.exists(work_path_name):
                # clean old work folder
                shutil.rmtree(work_path_name)
            # create work folder
            os.makedirs(work_path_name)
            for key, value in inventory.items():
              print(">>>TEST Test Suite: ", value['readable'])
              for test in value['tests']:
                testname = [key for key in test.keys()][0]   
                cproj_file_name = create_cproj(cvariant, toolchain, test_device, test['sources'], testname, tflm_path)
                print(cproj_file_name)
    else:
        print("Error: no files to test in \"",
              tflm_path, "\", use --tflm_path option!")
        test_error = 1
    properties = {"cvariant": cvariant, "toolchain": toolchain}

    #sys.exit( test_error )


if __name__ == '__main__':
    main()
