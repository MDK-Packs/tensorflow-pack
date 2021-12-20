# tensorflow-build

Directory contains scripts and assets to compile the CMSIS-pack containing the latest TensorFlow Lite Micro. 

Scripts are called in the order:
prep.sh -> hotfix.sh -> additionals.sh -> build.sh (or build_r.sh for Release builds)

## prep.sh
Run make from tensorflow repository in various configurations. Extracts sources using the list_library_sources target.

## hotfix.sh
Patch list of sources if required.

## additionals.sh
Some files are statically declared in the pack description. They need to be copied manually, as the build script does not know about them.

## build.sh
Call the generate_cmsis_pack.py and pass all generated lists of sources.

## generate_cmsis_pack.py 
```
Parameters are:
  --input_template        Path to template file pdsc.
  --hdrs                  Headers for cvariant Reference
  --srcs                  Sources for cvariant Reference
  --util_hdrs             Headers for Kernel Utils
  --util_srcs             Sources for Kernel Utils
  --hdrs-cmsis-nn         Headers for cvariant CMSIS-NN
  --srcs-cmsis-nn         Sources for cvariant CMSIS-NN
  --hdrs-ethos            Headers for cvariant Ethos-U
  --srcs-ethos            Sources for cvariant Ethos-U
  --testhdrs              Headers for component "Testing"
  --testsrcs              Sources for component "Testing"
  --release               Release version
  --tensorflow_path       Path to root of tensorflow git
```
