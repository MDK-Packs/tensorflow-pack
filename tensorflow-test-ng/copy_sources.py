
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


def main():
    test_error = 0
    # create the argument parser
    parser = argparse.ArgumentParser(
        description="Copy test sources from tensorflow repo to sources in test package.")
    # add the --tflm_path option
    parser.add_argument("--tflm_path", type=str, default=os.path.curdir,
                        help="path, basepath for sources from inventory")
    parser.add_argument("--out_path", type=str, default=os.path.curdir,
                        help="path, output path for sources from inventory")                    
    parser.add_argument("--inventory", type=str, default="",
                        help="yml file with a list of tests and sources for complex tests")

    # Check if path in --tflm_path exists
    if not os.path.exists(parser.parse_args().tflm_path):
        print("Path " + parser.parse_args().tflm_path + " does not exist")
        sys.exit(1)
    # print --tflm_path
    print("Working on tflm_path: " + parser.parse_args().tflm_path)

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
                for src in test['sources']:
                    src_path = os.path.join(parser.parse_args().tflm_path, src)
                    dst_path = os.path.join(parser.parse_args().out_path, src)
                    if os.path.exists(src_path):
                        #replace extension from .cc to .cpp
                        if src_path.endswith(".cc"):
                            dst_path = dst_path.replace(".cc", ".cpp")
                        print(src_path, " ==> " , dst_path)
                        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                        shutil.copy(src_path, dst_path)


if __name__ == '__main__':
    main()
