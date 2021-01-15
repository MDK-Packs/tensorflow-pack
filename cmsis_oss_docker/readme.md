# Base image 
- Ubuntu latest x86_64
# Generic Tools
- Python 3.8
- curl
- wget
- bzip2
- unzip
- git
- build-essential (native GCC, make) 
# Arm Tools 
- GNU Arm Embedded Toolchain: 10-2020-q4-major release (Linux x86_64)
- Fixed Virtual Platform model of Corstone-300 MPS2 based platform Cortex-M55 (Linux x86)
- Fixed Virtual Platform model of Corstone-300 MPS3 based platform Cortex-M55 + Ethos-U55 (Linux x86)

# Create a image from the Dockerfile
docker build --pull --rm -f "Dockerfile" -t cmsisossdocker:latest "."

# Run image in detached mode and mount host directory
docker run -i -v C:\Projects\cmsis_oss_docker\tests:/workspace/host --name mycontainer -d cmsisossdocker

# Excute image interactive
docker exec -it mycontainer /bin/bash

# Example of PackChk Usage
docker exec mycontainer PackChk host/PackChk/MyVendor.MyPack.pdsc

# Example of Arm GCC Usage
docker exec mycontainer arm-none-eabi-gcc -S -mcpu=cortex-m55 -mthumb host/gcc/test.c

# Example of CMSIS-build Usage
docker exec mycontainer cbuild.sh host/cbuild/ARMCM55_DSP_FPU_MVE.cprj