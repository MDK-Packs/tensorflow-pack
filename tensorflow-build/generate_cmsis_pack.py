# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
""" Generate CMSIS Pack """

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from shutil import copyfile

import argparse
import shutil
import zipfile
import tarfile
import re
import os
import platform
import six
import requests
import zipfile
import datetime
import fnmatch
import semantic_version


run_path = os.path.dirname(__file__)
tf_path = ""
outpath = os.path.join(run_path, "./gen/")
kernelpath = ""
pack_build = os.path.join(outpath, "./build")
utilities_dir = os.path.join(outpath, "./utilities")


def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            new_s = s.replace(find, replace)
            if s != new_s:
                print("Replacing " + find + " with " + replace + " in " + filepath)
                with open(filepath, "w") as f:
                    f.write(new_s)


def sanitize_xml(unsanitized):
    """Uses a whitelist to avoid generating bad XML."""
    return re.sub(r'[^a-zA-Z0-9+_\-/\\.]', '', six.ensure_str(unsanitized))


def sanitize_SemVer(unsanitized):
    """Uses a whitelist to avoid generating bad SemVer."""
    return str(semantic_version.Version.coerce(unsanitized))


def prepare_environment():
    global packcheck_name
    # Pack build utilities Repository
    utilities_os = platform.system()

    print("Detected Host OS: " + utilities_os)

    if utilities_os == "Linux":
        if platform.machine() == "aarch64":
            packcheck_url = "https://github.com/Open-CMSIS-Pack/devtools/releases/download/tools%2Fpackchk%2F1.3.98/packchk-1.3.98-linux64-arm64.tbz2"
        else:
            packcheck_url = "https://github.com/Open-CMSIS-Pack/devtools/releases/download/tools%2Fpackchk%2F1.3.98/packchk-1.3.98-linux64-amd64.tbz2"
        packcheck_name = "packchk"
    elif utilities_os == "Windows":
        packcheck_url = "https://github.com/Open-CMSIS-Pack/devtools/releases/download/tools%2Fpackchk%2F1.3.98/packchk-1.3.98-windows64-amd64.zip"
        packcheck_name = "PackChk.exe"
    elif utilities_os == "Darwin":
        packcheck_url = "https://github.com/Open-CMSIS-Pack/devtools/releases/download/tools%2Fpackchk%2F1.3.98/packchk-1.3.98-darwin64-amd64.tbz2"
        packcheck_name = "packchk"
    else:
        print("No PackChk executable for Host OS " +
              utilities_os + " available. Exit.")
        exit()

    print("Preparing build environment directories.")

    if os.path.lexists(outpath) is False:
        os.makedirs(outpath)
    if os.path.lexists(pack_build) is False:
        os.makedirs(pack_build)
    if os.path.lexists(utilities_dir) is False:
        os.mkdir(utilities_dir)

    print("Downloading binary release of PackCheck utility.")

    packcheck_tmp = requests.get(packcheck_url)
    if packcheck_url.endswith(".tbz2"):
        with open(utilities_dir + "/" + packcheck_name + ".tbz2", "wb") as f:
            f.write(packcheck_tmp.content)
        with tarfile.open(utilities_dir + "/" + packcheck_name + ".tbz2", 'r:bz2') as tarObj:
            tarObj.extractall(path=utilities_dir)
    else:
        open(utilities_dir + "/" + packcheck_name +
             ".zip", "wb").write(packcheck_tmp.content)
        with zipfile.ZipFile(utilities_dir + "/" + packcheck_name + ".zip", 'r') as zipObj:
            zipObj.extractall(path=utilities_dir)
    if utilities_os == "Linux" or "Darwin":
        os.chmod(utilities_dir + "/" + packcheck_name, 0o775)
    copyfile(tf_path+"/LICENSE", pack_build+"/LICENSE")


def get_version():
    test_str = open(tf_path + "/tensorflow/tools/pip_package/setup.py").read()
    regex = r"(?<=_VERSION = ).*"
    matches = re.search(regex, test_str, re.MULTILINE)
    ret = matches.group().replace("'", "")
    return ret


def make_component_file_list(srcs_list):
    replace_srcs = ""
    srcs_list = set(srcs_list)
    # create a new list for include pathes
    include_list = []
    for src in srcs_list:
        src = src.split("\n")[0]
        if not src:
            continue
        ext = os.path.splitext(src)[1]
        if ext == '.h':
            incdir = os.path.dirname(src)
            include_list.append(incdir)
        elif ext == '.c':
            category = "sourceC"
        elif ext == '.cc':
            src = src.replace(".cc", ".cpp")
            category = "sourceCpp"
            print("Converting .cc to .cpp: " + src)
        elif ext == '.cpp':
            category = "sourceCpp"
        else:
            continue
        basename = sanitize_xml(os.path.basename(src))
        clean_src = sanitize_xml(src)
        clean_src = clean_src.replace("'", "")
        if ext != ".h" and src != "tensorflow/lite/kernels/kernel_util.cpp" \
                and src != "tensorflow/lite/micro/system_setup.cpp" \
                and src != "tensorflow/lite/c/common.c" \
                and src != "tensorflow/lite/micro/cortex_m_generic/micro_time.cpp" \
                and src != "tensorflow/lite/micro/cortex_m_generic/debug_log.cpp" \
                and src.endswith("_test.cc") == False:
            replace_srcs += '        <file category=\"' + \
                category + '\" name=\"' + src + '\"/> \n'
        dest_fpath = pack_build+'/'+src
        # os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)
        # copyfile(tf_path+'/'+src, dest_fpath)
        # print ("Copied " + src + " to " + dest_fpath)
    include_list = set(include_list)
    print("Extracted include directories ", include_list)
    for src in include_list:
        src = src.split("\\n")[0]
        print(src)
        if not src:
            continue
        ext = os.path.splitext(src)[1]
        basename = sanitize_xml(os.path.basename(src))
        clean_src = sanitize_xml(src)
        replace_srcs += '        <file category=\"include\" name=\"' + src + '/\"/> \n'
    return replace_srcs


def load_list_from_file(filename):
    with open(filename, "r") as lstfile:
        lines = lstfile.readlines()
    lstfile.close()
    return lines


def main(unparsed_args, flags):
    global tf_path
    global kernelpath

    tf_path = flags.tensorflow_path
    kernelpath = tf_path + "/tensorflow/lite/micro/kernels/"

    print(tf_path)
    print(kernelpath)

    prepare_environment()
    # fix this one day:
    #  subprocess.call(['sh', './tensorflow-pack/tensorflow-build/additionals.sh'])

    # read file into string
    if flags.history != "":
        with open(flags.history, "r") as history_file:
            history_str = history_file.read()

    # get --srcs and --hdrs from arguments
    core_srcs_list = load_list_from_file(flags.srcs)
    core_hdrs_list = load_list_from_file(flags.hdrs)
    all_core_srcs_list = core_srcs_list + core_hdrs_list
    all_core_srcs_list.sort()

    print(all_core_srcs_list)

    # get --srcs and --hdrs from arguments
    util_srcs_list = load_list_from_file(flags.util_srcs)
    # util_hdrs_list = load_list_from_file(flags.util_hdrs)
    all_util_srcs_list = util_srcs_list  # + util_hdrs_list
    all_util_srcs_list.sort()

    # get --srcs-cmsis_nn and --hdrs-cmsis_nn from arguments
    cmsis_nn_srcs_list = load_list_from_file(flags.srcs_cmsis_nn)
    cmsis_nn_hdrs_list = load_list_from_file(flags.hdrs_cmsis_nn)
    all_cmsis_nn_srcs_list = cmsis_nn_srcs_list + cmsis_nn_hdrs_list
    all_cmsis_nn_srcs_list.sort()

    # get --srcs-ethos and --hdrs-ethos from arguments
    ethos_srcs_list = load_list_from_file(flags.srcs_ethos)
    ethos_hdrs_list = load_list_from_file(flags.hdrs_ethos)
    all_ethos_srcs_list = ethos_srcs_list + ethos_hdrs_list
    all_ethos_srcs_list.sort()

    # get --testsrcs and --testhdrs from arguments
    test_srcs_list = load_list_from_file(flags.testsrcs)
    test_hdrs_list = load_list_from_file(flags.testhdrs)
    all_test_srcs_list = test_srcs_list + test_hdrs_list
    all_test_srcs_list.sort()

    # get signal library if exists ("signal.lst" alongside flags.srcs)
    replace_signal_srcs = ""
    if os.path.exists(flags.srcs.replace("srcs.", "signal.")):
      signal_srcs_list = load_list_from_file(flags.srcs.replace("srcs.", "signal."))
    replace_signal_srcs = make_component_file_list(signal_srcs_list)

    print(replace_signal_srcs)

    replace_core_srcs = make_component_file_list(all_core_srcs_list)
    replace_util_srcs = make_component_file_list(all_util_srcs_list)
    replace_test_srcs = make_component_file_list(all_test_srcs_list)
    replace_cmsis_srcs = make_component_file_list(all_cmsis_nn_srcs_list)
    replace_ethos_srcs = make_component_file_list(all_ethos_srcs_list)

    # fix includes for CMSIS-NN, as we use the pack instead
    findReplace(outpath, "CMSIS/NN/Include/", "", "*.cpp")
    findReplace(outpath, "Include/arm_nnfunctions.h",
                "arm_nnfunctions.h", "*.cpp")
    findReplace(outpath, "Include/arm_nn_types.h",
                "arm_nnfunctions.h", "*.cpp")

    # fix the micro_time.cpp to use the correct CMSIS device header define
    invalid_device_include = "#ifdef CMSIS_DEVICE_ARM_CORTEX_M_XX_HEADER_FILE\n#include CMSIS_DEVICE_ARM_CORTEX_M_XX_HEADER_FILE\n#endif"
    valid_device_include = "#include \"RTE_Components.h\"\n#include CMSIS_device_header"

    findReplace(outpath, invalid_device_include,
                valid_device_include, "*.cpp")

    now = datetime.datetime.now()
    calversion = datetime.datetime.today().strftime('%Y%m%d')
    tmpl_pdsc_date = now.strftime('%Y-%m-%d')
    if flags.release:
        pack_version = flags.release
    if flags.candidate_rev:
        pack_version = flags.release + "-" + flags.candidate_rev

    pack_version = sanitize_SemVer(pack_version)

    # load pdsc template from ../templates
    with open(flags.input_template, 'r') as input_template_file:
        template_file_text = input_template_file.read()

    template_file_text = re.sub(
        r'%{KERNEL_FILES_REFERENCE}%', replace_core_srcs, six.ensure_str(template_file_text))
    template_file_text = re.sub(
        r'%{KERNEL_FILES_CMSIS}%', replace_cmsis_srcs, six.ensure_str(template_file_text))
    template_file_text = re.sub(
        r'%{KERNEL_FILES_ETHOS}%', replace_ethos_srcs, six.ensure_str(template_file_text))
    template_file_text = re.sub(
        r'%{KERNEL_UTIL_FILES}%', replace_util_srcs, six.ensure_str(template_file_text))
    template_file_text = re.sub(
        r'%{TEST_FILES}%', replace_test_srcs, six.ensure_str(template_file_text))
    template_file_text = re.sub(
        r'%{SIGNAL_FILES_REFERENCE}%', replace_signal_srcs, six.ensure_str(template_file_text))
    template_file_text = re.sub(
        r'%{RELEASE_VERSION}%', pack_version, template_file_text)
    template_file_text = re.sub(
        r'%{RELEASE_DATE}%', tmpl_pdsc_date, template_file_text)
    template_file_text = re.sub(
        r'%{HISTORY}%', history_str, template_file_text)

    with open(pack_build + "/tensorflow.tensorflow-lite-micro.pdsc", 'w') as output_file:
        output_file.write(template_file_text)
    print("Running PackCheck")
    # p = subprocess.check_call([utilities_dir + '/' + packcheck_name, os.path.join(pack_build, "./tensorflow.tensorflow-lite-micro.pdsc")], stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

    print("Creating zip package... ")
    os.chdir(os.path.dirname(outpath+"/build/"))

    out_dir = "../../../out"

    # Name of the ziped pack file
    zip_filename = f"tensorflow.tensorflow-lite-micro.{pack_version}.pack"

    # Check if the output directory exists, if not create it
    if not os.path.exists(os.path.abspath(out_dir)):
        os.makedirs(os.path.abspath(out_dir))

    def zipdir(path, ziph):
        # Add all files and folders in the path to the ziph
        for root, dirs, files in os.walk(path):
            for file in files:
                # Exclude the zip file itself, if it is in the same folder
                if file != zip_filename:
                    ziph.write(os.path.join(root, file), os.path.relpath(
                        os.path.join(root, file), path))

    # Create the zip file
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(".", zipf)

    # Move the zip file to the output directory
    shutil.move(zip_filename, os.path.join(out_dir, zip_filename))

    print("Done.")


def parse_args():
    """Converts the raw arguments into accessible flags."""
    parser = argparse.ArgumentParser(
        usage='Use "python %(prog)s --help" for more information', formatter_class=argparse.HelpFormatter)
    parser.register('type', 'bool', lambda v: v.lower() == 'true')
    parser.add_argument(
        '--input_template',
        type=str,
        default='',
        help='Path to template file pdsc.')
    parser.add_argument(
        '--hdrs',
        type=str,
        default='./hdrs.lst',
        help='Headers for cvariant Reference')
    parser.add_argument(
        '--srcs',
        type=str,
        default='./srcs.lst',
        help='Sources for cvariant Reference')
    parser.add_argument(
        '--util_hdrs',
        type=str,
        default='./util_hdrs.lst',
        help='Headers for Kernel Utils')
    parser.add_argument(
        '--util_srcs',
        type=str,
        default='./util_srcs.lst',
        help='Sources for Kernel Utils')
    parser.add_argument(
        '--hdrs-cmsis-nn',
        type=str,
        default='./hdrs.cmsis-nn.lst',
        help='Headers for cvariant CMSIS-NN')
    parser.add_argument(
        '--srcs-cmsis-nn',
        type=str,
        default='./srcs.cmsis-nn.lst',
        help='Sources for cvariant CMSIS-NN')
    parser.add_argument(
        '--hdrs-ethos',
        type=str,
        default='./hdrs.ethos.lst',
        help='Headers for cvariant Ethos-U')
    parser.add_argument(
        '--srcs-ethos',
        type=str,
        default='./srcs.ethos.lst',
        help='Sources for cvariant Ethos-U')
    parser.add_argument(
        '--testhdrs',
        type=str,
        default='./hdrs.test.lst',
        help='Headers for component Testing')
    parser.add_argument(
        '--testsrcs',
        type=str,
        default='./srcs.test.lst',
        help='Sources for component Testing')
    parser.add_argument(
        '--release',
        type=str,
        help='Release versioning')
    parser.add_argument(
        '--candidate_rev',
        type=str,
        default="",
        help='Release candidate versioning, e.g. rc1, rc2, etc.')
    parser.add_argument(
        '--history',
        type=str,
        default="",
        help='Release history.')
    parser.add_argument(
        '--tensorflow_path',
        type=str,
        required=True,
        help='Path to root of tensorflow git')
    flags, unparsed_args = parser.parse_known_args()

    main(unparsed_args, flags)


if __name__ == '__main__':
    parse_args()
