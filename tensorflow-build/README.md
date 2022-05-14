# tensorflow-build

Directory contains scripts and assets to compile the CMSIS-pack containing the latest TensorFlow Lite Micro. 

## build_r.sh
Entry point to run the full workflow to download, sort, generate source trees and build the pack.

### The workflow is:

1. Get the latest root repository from mlplatform.org. It contains a list of json files with an index of release SHAs for a specific release.
2. Retrieve the repositories for a specified release (e.g. "20.02"). This release is passed to the github workflow as a parameter.
3. create_tflm_tree.py is used to create the source trees for variants "Reference", "CMSIS-NN", "Ethos-U".
4. For each source tree a list of files used it written into a srcs.*.lst text file.
5. Merge determined sources into build directory.
6. Run generate_cmsis_pack.py and pass the lists of sources.

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

Internally generate_cmsis_pack.py will pull PackChk for the platform the script is executed on. 
The generated pdsc will be validated and the tensorflow-lite-micro.*.pack will only be generated when validation passes.