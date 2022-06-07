# Version: 0.5
# Date: 2021-05-25
# This python script generates a CMSIS Software Pack
#
# Requirements:
# python 3.6+
# 
# Usage:
#
# python3 gen_pack.py <arguments>
#
# required:
# --path - Path cotaining the config.yml and all assets
#
# optional:
# --version - Specify a custom version number
# --date-tag - Tag the version with todays date
# config.yml - Pack build configuration 
#
# 
#


import os, platform
import requests
import zipfile
import shutil
import subprocess
import time
import datetime

import yaml
import argparse
import re

import distutils
from distutils import dir_util

import semantic_version

def sanitize_SemVer(unsanitized):
    """Uses a whitelist to avoid generating bad SemVer."""
    return str(semantic_version.Version.coerce(unsanitized))

def main(unparsed_args, flags):
  print (flags)

  with open( os.path.abspath(flags.path + "/config.yml"), "r") as ymlfile:
      cfg = yaml.safe_load(ymlfile)

  if shutil.which("packchk") is None:
    print("Error: packchk is not available on path")
    exit()

  PACK_BUILD = cfg["build"]
  pack_path = os.path.realpath(os.path.join(os.path.abspath(flags.path), PACK_BUILD))
  print(pack_path)

  CONTRIB_ADD = cfg["add"]
  add_path = os.path.realpath(os.path.join(os.path.abspath(flags.path), CONTRIB_ADD))
  print(add_path)

  SOURCE_ADD = cfg["local_source"]
  src_path = os.path.realpath(os.path.join(os.path.abspath(flags.path), SOURCE_ADD)) 
  src_dest = os.path.realpath(os.path.join(pack_path, cfg["src_dest"]))
  print(src_path)

  OUTPATH = cfg["out"]
  out_path = os.path.realpath(os.path.join(os.path.abspath(flags.path), OUTPATH))
  print(out_path)

  PDSCPATH = cfg["pdsc"]
  pdsc_path = os.path.realpath(os.path.join(os.path.abspath(flags.path), PDSCPATH))
  print(pdsc_path)

  print (">>> Preparing build environment directories.") 
  if os.path.isdir(pack_path):
    shutil.rmtree(pack_path)  
  os.mkdir(pack_path)

  print (">>> Determining version string.") 
  pack_version = cfg["version"]
  print (cfg["version"])
  if flags.version is not None:
    pack_version = flags.version
  now = datetime.datetime.now()
  calversion = datetime.datetime.today().strftime('%Y%m%d')
  tmpl_pdsc_date = now.strftime('%Y-%m-%d')
  if flags.date_tag:
    pack_version = pack_version + "." + calversion 
  elif flags.candidate_rev:
    pack_version = pack_version + "-" + flags.candidate_rev 
  else:
    pack_version = pack_version
  pack_version = sanitize_SemVer(pack_version)
  print(">>> Version: ", pack_version)  

  if cfg["local_source"] is not None:
    print (">>> Merging local source:")
    print (">>> ", src_path, "==>" ,src_dest)
    os.mkdir(src_dest)
    distutils.dir_util.copy_tree(src_path, src_dest, verbose=1)    

  if cfg["remote_source"] is not None:
    print (">>> Merging remote source:")
    print (">>> ", cfg["remote_source"], "==>" ,src_dest)
    upstream_tmp = requests.get(cfg["remote_source"])
    open("./download.zip", 'wb').write(upstream_tmp.content)
    with zipfile.ZipFile("./download.zip", 'r') as zip_ref:
      zip_ref.extractall(src_dest)

  if cfg["add"] is not None:
    print (">>> Merging additions.")
    print (">>> ", add_path, "==>" ,pack_path)
    distutils.dir_util.copy_tree(add_path, pack_path)   

  history_str = ""
   # read file into string
  if flags.history != "":
    with open(flags.history, "r") as history_file:
      history_str = history_file.read()
      history_str = history_str.replace("tensorflow.tensorflow-lite-micro", cfg["vendor"]+"."+cfg["name"])    
      print(history_str)

  if cfg["pdsc"] is not None:
    print (">>> Merging pdsc.")
    new_pdsc_path = os.path.join(pack_path , os.path.basename(pdsc_path))
    #load pdsc template from ../templates
    with open(pdsc_path+".tpl", 'r') as input_template_file:
      template_file_text = input_template_file.read()
    pdsc_path = new_pdsc_path
    template_file_text = re.sub(r'%{RELEASE_VERSION}%', pack_version, template_file_text)
    template_file_text = re.sub(r'%{RELEASE_DATE}%', tmpl_pdsc_date, template_file_text)    
    template_file_text = re.sub(r'%{HISTORY}%', history_str, template_file_text)
    with open(pdsc_path, 'w') as output_file:
      output_file.write(template_file_text)
    print(template_file_text)

  print (">>> Running PackCheck")
  command = "packchk -n PackName.txt " + pdsc_path
  print (">>>", command)
  os.system(command)

  with open (os.getcwd() + "/PackName.txt", "r") as packversion_file:
      packfile_name=packversion_file.readline()

  os.chdir(pack_path)

  print ("Creating zip package: " + packfile_name)
  with zipfile.ZipFile(packfile_name,"w",zipfile.ZIP_DEFLATED,allowZip64=True) as zf:
    for root, _, filenames in os.walk('./'):
        for name in filenames:
            name = os.path.join(root, name)
            name = os.path.normpath(name)
            zf.write(name, name)


def parse_args():
  """Converts the raw arguments into accessible flags."""
  parser = argparse.ArgumentParser(usage='Use "python %(prog)s --help" for more information', formatter_class=argparse.HelpFormatter)
  parser.register('type', 'bool', lambda v: v.lower() == 'true')
  parser.add_argument(
      '--path',
      type=str,
      default='',
      help='Path to pack assets.')
  parser.add_argument(
      '--version',
      type=str,
      default=None,
      help='Set or override version with custom setting.')
  parser.add_argument(
        '--candidate_rev',
        type=str,
        default="",
        help='Release candidate versioning, e.g. rc1, rc2, etc.')  
  parser.add_argument(
      '--date_tag',
      default=False,
      action='store_true',
      help='Tag versions with date.')
  parser.add_argument(
        '--history',
        type=str,
        default="",
        help='Release history.')    

  flags, unparsed_args = parser.parse_known_args()

  main(unparsed_args, flags)

if __name__ == '__main__':
  parse_args()
  
