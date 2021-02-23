# Version: 0.2
# Date: 2020-05-25
# This bash script generates a CMSIS Software Pack:
#
# Requirements:
# python 3.5

import os, platform
import requests
import zipfile
import shutil
import subprocess
import time

# Upstream repository
UPSTREAM_URL="https://github.com/google/flatbuffers/archive/master.zip"

# Pack Vendor
PACK_VENDOR="MDK-Packs"
# Pack Name
PACK_NAME="flatbuffers"

# NO NEED TO EDIT BELOW
# Contributions merge
CONTRIB_MERGE="./contributions/merge"
# Contributions additional folders/files
CONTRIB_ADD="./contributions/add"

# Pack Destination Folder
PACK_DESTINATION="./"

# Pack Build Folder
PACK_BUILD="./build"

# Pack build utilities Repository
UTILITIES_URL="https://github.com/ARM-software/CMSIS_5/blob/master/"
UTILITIES_TAG="1.0.0"
UTILITIES_DIR="./Utilities"
UTILITIES_OS=platform.system()

print ("Detected Host OS: " + UTILITIES_OS)

if UTILITIES_OS == "Linux" : 
    packcheck_url = "https://github.com/ARM-software/CMSIS_5/blob/develop/CMSIS/Utilities/Linux64/PackChk?raw=true"
    packcheck_name = "PackChk"
elif UTILITIES_OS == "Windows" :
    packcheck_url = "https://github.com/ARM-software/CMSIS_5/blob/develop/CMSIS/Utilities/Win32/PackChk.exe?raw=true"
    packcheck_name = "PackChk.exe"
else: 
    print("No PackChk executable for Host OS " + UTILITIES_OS + " available. Exit.")
    exit()

print ("Preparing build environment directories.")
path = os.getcwd()
if os.path.isdir(path + "/" + PACK_BUILD):
  shutil.rmtree(PACK_BUILD)  
os.mkdir(path + "/" + PACK_BUILD)

if os.path.isdir(path + "/" + UTILITIES_DIR):
  shutil.rmtree(UTILITIES_DIR)  
os.mkdir(path + "/" + UTILITIES_DIR)

print ("Downloading binary release of PackCheck utility.")

packcheck_tmp = requests.get(packcheck_url)
open(UTILITIES_DIR + "/" + packcheck_name, 'wb').write(packcheck_tmp.content)
if UTILITIES_OS == "Linux" : 
    os.chmod(UTILITIES_DIR + "/" + packcheck_name, 777)

print ("Downloading repository master branch.")

upstream_tmp = requests.get(UPSTREAM_URL)
open("./repo.zip", 'wb').write(upstream_tmp.content)
with zipfile.ZipFile("./repo.zip", 'r') as zip_ref:
    zip_ref.extractall(PACK_BUILD)

os.rename(PACK_BUILD+"/"+PACK_NAME+"-master/", PACK_BUILD+"/src")

print ("Merging repositories.")

add_files = os.listdir(CONTRIB_ADD)
for file_name in add_files:
    full_file_name = os.path.join(CONTRIB_ADD, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, PACK_BUILD)

print ("Running PackCheck")
print ("./Utilities/"+packcheck_name, PACK_BUILD+"/"+PACK_VENDOR+"."+PACK_NAME+".pdsc", "-nPackName.txt")
p = subprocess.check_call(["./Utilities/"+packcheck_name, PACK_BUILD+"/"+PACK_VENDOR+"."+PACK_NAME+".pdsc", "-n PackName.txt"], stdin=None, stdout=None, stderr=None, shell=False, timeout=None)

print (os.getcwd())
with open (os.getcwd()+"/PackName.txt", "r") as packversion_file:
    packfile_name=packversion_file.readline()

print("Pack Version determined: " + packfile_name)

os.chdir("./build")
print (os.getcwd())

print ("Creating zip package: " + packfile_name)
with zipfile.ZipFile(packfile_name,"w",zipfile.ZIP_DEFLATED,allowZip64=True) as zf:
    for root, _, filenames in os.walk('./'):
        for name in filenames:
            name = os.path.join(root, name)
            name = os.path.normpath(name)
            zf.write(name, name)


