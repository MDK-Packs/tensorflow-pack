[![Release CI using Arm Virtual Hardware](https://github.com/MDK-Packs/tensorflow-pack/actions/workflows/release_vht.yml/badge.svg)](https://github.com/MDK-Packs/tensorflow-pack/actions/workflows/release_vht.yml)

# tensorflow-pack
Build and test environment for CMSIS-Pack containing TensorFlow Lite Micro

## Requirements:
(based on 20.04 Ubuntu Linux environment)
Packages apt
- python3
- python3_venv
- python3-pip
- wget
- rsync
- git

Packages pip
- pillow

## Start the pack build

```./tensorflow-build/build_r.sh <rev> <rc>```

```./3rdparty-build/build_r.sh <rec> ```
  
  
