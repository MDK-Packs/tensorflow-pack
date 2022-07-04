
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

def sanitize_xml(unsanitized):
    """Uses a whitelist to avoid generating bad XML."""
    return re.sub(r'[^a-zA-Z0-9+_\-/\\.]', '', six.ensure_str(unsanitized))


def write_file_list (file_list, file_name):
    with open(file_name) as f:
        s = f.read()
        if "<-- test_src_files -->" not in s:
            print('Error when writing Test.clayer.yml')
            return
    with open(file_name, 'w') as f:
        print('Writing Test.clayer.yml')
        s = s.replace("<-- test_src_files -->", file_list)
        f.write(s)

def make_file_list(base_path ,srcs_list):
    replace_srcs = ''
    srcs_list = set(srcs_list)
    for src in srcs_list:
        if not src:
            continue
        clean_src = sanitize_xml(os.path.join(base_path,src))
        #replace extension .cc with .cpp
        if clean_src.endswith(".cc"):
               clean_src = clean_src.replace(".cc", ".cpp")
        replace_srcs += '    - file: ' + clean_src + ' \n'
    return replace_srcs

def main():
    test_error = 0
    # create the argument parser
    parser = argparse.ArgumentParser(
        description="Run tensorflow-lite-micro tests on Arm VFPs.")
    parser.add_argument("--out_path", type=str, default=os.path.curdir,
                        help="path, output path for sources from inventory")                    
    parser.add_argument("--inventory", type=str, default="",
                        help="yml file with a list of tests and sources for complex tests")


    # Check if path in --out_path exists
    if not os.path.exists(parser.parse_args().out_path):
        print("Path " + parser.parse_args().out_path + " does not exist")
        sys.exit(1)
    # print --out_path
    print("Working on out_path: " + parser.parse_args().out_path)

    # Check if inventory file exists
    if not os.path.exists(parser.parse_args().inventory):
        print("File " + parser.parse_args().inventory + " does not exist")
        sys.exit(1)
    # print --inventory
    print("Working on inventory: " + parser.parse_args().inventory)

    # Read inventory file
    with open(parser.parse_args().inventory, 'r') as stream:
        inventory = yaml.safe_load(stream)

    if inventory:
        for key, value in inventory.items():
            print(">>>TEST Test Suite: ", value['readable'])
            for test in value['tests']:
                testname = [key for key in test.keys()][0]   
                #cproj_file_name = create_cproj(cvariant, toolchain, test_device, test['sources'], testname, tflm_path)
                print(testname)
                src_yml = make_file_list("../../Source/", test['sources'])
                test_dir = os.path.join(parser.parse_args().out_path, testname)
                #create directory for test in out_path
                os.makedirs(test_dir, exist_ok=True)
                shutil.copy(os.path.dirname(__file__)+"/Project/Validation.cproject.yml", test_dir)
                shutil.copy(os.path.dirname(__file__)+"/Project/Validation.csolution.yml", test_dir)
                shutil.copy(os.path.dirname(__file__)+"/Layer/Test/Test.clayer.yml", test_dir)
                # replace string in Test.clayer.yml
                write_file_list(src_yml, os.path.join(test_dir, "Test.clayer.yml"))
            

if __name__ == '__main__':
    main()
