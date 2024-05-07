
# tensorflow-build

Directory contains scripts and assets to compile the CMSIS-pack containing the latest TensorFlow Lite Micro. 


## build_r.sh (build_d.sh for development releases)
The build_r.sh script serves as the entry point for running a full workflow that involves downloading, sorting, generating source trees, and building a pack. Steps involved in this workflow:

1. **Get the latest root repository**: The script starts by retrieving the latest root repository from mlplatform.org. This repository contains a list of JSON files that index release SHAs for a specific release. This step ensures that the script is working with the most up-to-date information.

2. **Retrieve repositories for a specified release**: The script then proceeds to retrieve the repositories associated with a specified release. The release version is passed to the script as a parameter. For example, if the release version is "20.02", the script will fetch the repositories related to that specific release.

3. **Create source trees**: The create_tflm_tree.py script is used to generate source trees for different variants, namely "Reference", "CMSIS-NN", and "Ethos-U". These source trees serve as the foundation for building the pack.

4. **Write source file lists**: For each source tree generated in the previous step, the script writes a list of files used in that particular source tree into a text file with a name like srcs.*.lst. These lists of source files provide a comprehensive overview of the files included in each source tree.

5. **Merge determined sources**: The script then merges the determined sources into a build directory. This step brings together the necessary files from the different source trees to create a unified set of sources for the pack.

6. **Apply patches**: The script applies a series of patches to the source files. These patches are necessary to ensure compatibility and correct functionality of the TensorFlow Lite Micro code within the CMSIS-Pack environment. The patches are applied using the 'patch' command, and the specific patches to be applied are determined by the script based on the release version and the specific source tree variant.

7. **Run generate_cmsis_pack.py**: Finally, the script executes the generate_cmsis_pack.py script and passes the lists of sources as arguments. This script is responsible for generating the CMSIS pack, which is a collection of software components and device support files used in embedded systems development.

## generate_cmsis_pack.py
This script is responsible for generating the CMSIS pack. It takes several parameters, including paths to source files, headers, and the release version. Here are the steps involved in this script:

1. **Read Parameters**: The script starts by reading the parameters passed to it. These parameters include paths to source files, headers, and the release version.

2. **Pull PackChk**: The script then pulls PackChk for the platform the script is executed on. PackChk is a tool used to validate the CMSIS pack.

3. **Generate PDSC File**: Using the input parameters, the script generates a PDSC (Pack Description) file. This file describes the pack contents, including software components, device support files, and examples.

4. **Validate PDSC File**: The generated PDSC file is then validated using PackChk. If the validation fails, the script will stop execution.

5. **Generate CMSIS Pack**: If the PDSC file passes validation, the script proceeds to generate the CMSIS pack. This pack is a collection of software components and device support files used in embedded systems development.

6. **Output**: The output of this script is a tensorflow-lite-micro.*.pack file, which is only generated when the PDSC validation passes.

## generate_cmsis_pack.py Usage
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

## Additional Scripts in the Repository

### get_releases.py

"""
This script retrieves the latest releases from a GitHub repository.

Usage:
  python get_releases.py [repository]

Arguments:
  repository (str): The name of the GitHub repository to retrieve releases from.

Returns:
  list: A list of dictionaries, where each dictionary represents a release and contains the following keys:
    - name (str): The name of the release.
    - tag_name (str): The tag name of the release.
    - published_at (str): The date and time when the release was published.
    - assets (list): A list of dictionaries representing the assets associated with the release, where each dictionary contains the following keys:
      - name (str): The name of the asset.
      - download_url (str): The URL to download the asset.

Example:
  python get_releases.py myrepo
"""

### clean_file_list.py
"""
This script provides functions to clean up a list of file names.

The `clean_file_list` module contains functions that can be used to remove unwanted characters and formats from a list of file names. It provides a simple and efficient way to sanitize file names before further processing.

Usage:
   python clean_file_list.py