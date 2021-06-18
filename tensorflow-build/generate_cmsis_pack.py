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
import tempfile
import zipfile
import re
import os, platform
import six
import requests
import subprocess
import zipfile
import datetime
from os import listdir
from os.path import isfile, join
import fnmatch

run_path = os.path.dirname(__file__)
tf_path = ""
outpath = run_path + "/gen/"
kernelpath = "" 
pack_build = outpath + "build"
utilities_dir = outpath + "utilities"

def findReplace(directory, find, replace, filePattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in fnmatch.filter(files, filePattern):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

def sanitize_xml(unsanitized):
  """Uses a whitelist to avoid generating bad XML."""
  return re.sub(r'[^a-zA-Z0-9+_\-/\\.]', '', six.ensure_str(unsanitized))

def prepare_environment():
  global packcheck_name
  if os.path.lexists(outpath):
    shutil.rmtree(outpath)  

  # Pack build utilities Repository
  utilities_os=platform.system()

  print ("Detected Host OS: " + utilities_os)

  if utilities_os == "Linux" : 
      packcheck_url = "https://github.com/ARM-software/CMSIS_5/blob/develop/CMSIS/Utilities/Linux64/PackChk?raw=true"
      packcheck_name = "PackChk"
  elif utilities_os == "Windows" :
      packcheck_url = "https://github.com/ARM-software/CMSIS_5/blob/develop/CMSIS/Utilities/Win32/PackChk.exe?raw=true"
      packcheck_name = "PackChk.exe"
  else: 
      print("No PackChk executable for Host OS " + utilities_os + " available. Exit.")
      exit()

  print ("Preparing build environment directories.")

  os.makedirs(outpath)
  os.mkdir(pack_build)
  os.mkdir(utilities_dir)

  print ("Downloading binary release of PackCheck utility.")

  packcheck_tmp = requests.get(packcheck_url)
  open(utilities_dir  + "/" + packcheck_name, 'wb').write(packcheck_tmp.content)
  if utilities_os == "Linux" : 
      os.chmod(utilities_dir  + "/" + packcheck_name, 0o775)

  copyfile(tf_path+"/LICENSE", pack_build+"/LICENSE")

def get_version ():
  test_str = open(tf_path + "/tensorflow/tools/pip_package/setup.py").read()
  regex = r"(?<=_VERSION = ).*"
  matches = re.search(regex, test_str, re.MULTILINE)
  ret = matches.group().replace("'","") 
  return ret


def make_component_file_list (srcs_list):
  replace_srcs = ''
  srcs_list = set(srcs_list)
  print (srcs_list)
  for src in srcs_list:
    if not src:
      continue
    ext = os.path.splitext(src)[1]
    if ext == '.h':
      category = "header"
    elif ext == '.c':
      category = "sourceC"
    elif ext ==  '.cc' or ext == '.cpp':
      category = "sourceCpp"
    else :
      continue
    basename = sanitize_xml(os.path.basename(src))
    clean_src = sanitize_xml(src)
    if src != "tensorflow/lite/kernels/kernel_util.cc" and src.endswith("_test.cc") == False:
      replace_srcs += '        <file category=\"'+ category +'\" name=\"' + src + '\"/> \n'
    dest_fpath = pack_build+'/'+src
    os.makedirs(os.path.dirname(dest_fpath), exist_ok=True)
    copyfile(tf_path+'/'+src, dest_fpath)
  return replace_srcs


def load_list_from_file (filename):
  with open (filename, "r") as lstfile:
    raw_string=lstfile.readlines()
    extracted_string = re.findall(r'<LIST>(.+?)</LIST>',str(raw_string))
    if extracted_string:
      return extracted_string.pop(0).split(" ")
  return "".split(" ")

def main(unparsed_args, flags):
  global tf_path 
  global kernelpath 

  tf_path = flags.tensorflow_path
  kernelpath = tf_path + "/tensorflow/lite/micro/kernels/"

  print (tf_path)
  print (kernelpath)

  prepare_environment()

  #get --srcs and --hdrs from arguments
  core_srcs_list = load_list_from_file(flags.srcs)
  core_hdrs_list = load_list_from_file(flags.hdrs)
  all_core_srcs_list = core_srcs_list + core_hdrs_list
  all_core_srcs_list.sort()

  #get --srcs and --hdrs from arguments
  util_srcs_list = load_list_from_file(flags.util_srcs)
  #util_hdrs_list = load_list_from_file(flags.util_hdrs)
  all_util_srcs_list = util_srcs_list #+ util_hdrs_list
  all_util_srcs_list.sort()

  #get --srcs-cmsis_nn and --hdrs-cmsis_nn from arguments
  cmsis_nn_srcs_list = load_list_from_file(flags.srcs_cmsis_nn)
  cmsis_nn_hdrs_list = load_list_from_file(flags.hdrs_cmsis_nn)
  all_cmsis_nn_srcs_list = cmsis_nn_srcs_list + cmsis_nn_hdrs_list
  all_cmsis_nn_srcs_list.sort()

  #get --srcs-ethos and --hdrs-ethos from arguments
  ethos_srcs_list = load_list_from_file(flags.srcs_ethos)
  ethos_hdrs_list = load_list_from_file(flags.hdrs_ethos)
  all_ethos_srcs_list = ethos_srcs_list + ethos_hdrs_list
  all_ethos_srcs_list.sort()

  #get --testsrcs and --testhdrs from arguments
  test_srcs_list = load_list_from_file(flags.testsrcs)
  test_hdrs_list = load_list_from_file(flags.testhdrs)
  all_test_srcs_list = test_srcs_list + test_hdrs_list
  all_test_srcs_list.sort()

  replace_core_srcs = make_component_file_list(all_core_srcs_list)
  replace_util_srcs = make_component_file_list(all_util_srcs_list)
  replace_test_srcs = make_component_file_list(all_test_srcs_list)
  replace_cmsis_srcs = make_component_file_list(all_cmsis_nn_srcs_list)
  replace_ethos_srcs = make_component_file_list(all_ethos_srcs_list)
  
  # fix includes for CMSIS-NN, as we use the pack instead
  findReplace(outpath, "cmsis/CMSIS/NN/Include/", "", "*.cc")

  now = datetime.datetime.now()
  calversion = datetime.datetime.today().strftime('%Y%m%d')
  tmpl_pdsc_date = now.strftime('%Y-%m-%d')
  pack_version = "0.2." + calversion + "-preview"  #get_version()

  #load pdsc template from ../templates
  with open(flags.input_template, 'r') as input_template_file:
    template_file_text = input_template_file.read()

  template_file_text = re.sub(r'%{KERNEL_FILES_REFERENCE}%', replace_core_srcs, six.ensure_str(template_file_text))
  template_file_text = re.sub(r'%{KERNEL_FILES_CMSIS}%', replace_cmsis_srcs, six.ensure_str(template_file_text))
  template_file_text = re.sub(r'%{KERNEL_FILES_ETHOS}%', replace_ethos_srcs, six.ensure_str(template_file_text))
  template_file_text = re.sub(r'%{KERNEL_UTIL_FILES}%', replace_util_srcs, six.ensure_str(template_file_text))
  template_file_text = re.sub(r'%{TEST_FILES}%', replace_test_srcs, six.ensure_str(template_file_text))
  template_file_text = re.sub(r'%{RELEASE_VERSION}%', pack_version, template_file_text)
  template_file_text = re.sub(r'%{RELEASE_DATE}%', tmpl_pdsc_date, template_file_text) 
                     

  with open(pack_build + "/tensorflow.tensorflow-lite-micro.pdsc", 'w') as output_file:
    output_file.write(template_file_text)
  print ("Running PackCheck")
  p = subprocess.check_call([utilities_dir+ '/' +packcheck_name, pack_build + "/tensorflow.tensorflow-lite-micro.pdsc"], stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

  print ("Creating zip package... ")
  os.chdir(os.path.dirname(outpath+"/build/"))

  with zipfile.ZipFile(outpath + "tensorflow.tensorflow-lite-micro."+pack_version+".pack","w",zipfile.ZIP_DEFLATED,allowZip64=True) as zf:
      for root, _, filenames in os.walk(os.path.basename(".")):
          for name in filenames:
              name = os.path.join(root, name)
              name = os.path.normpath(name)
              zf.write(name, name)
  print("Done.")

def parse_args():
  """Converts the raw arguments into accessible flags."""
  parser = argparse.ArgumentParser(usage='Use "python %(prog)s --help" for more information', formatter_class=argparse.HelpFormatter)
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
      '--tensorflow_path',
      type=str,
      required=True,
      help='Path to root of tensorflow git')
  flags, unparsed_args = parser.parse_known_args()

  main(unparsed_args, flags)


if __name__ == '__main__':
  parse_args()
  
