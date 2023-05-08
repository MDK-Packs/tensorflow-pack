# TensorFlow Lite Micro Examples Builder

This Python script automates the process of building examples from the TensorFlow Lite Micro repository. It supports creating `cproject` and `csolution` YAML files for Keil MDK / CMSIS Build tools projects.

## Functions and Usage

1. **list_subfolders(path):** Lists all the subfolders in a given directory.

2. **create_csolution_yml(out_path, cproject_files):** Creates a `csolution.yml` file in the specified output directory, using a list of `cproject` file paths.

3. **create_cproject_yml(folder_path, folder_name):** Creates a `cproject.yml` file in the specified folder, based on the contents of the folder.

4. **list_subfolders_with_makefile_inc(path):** Lists all subfolders in a given directory containing a `Makefile.inc` file.

5. **move_sources_to_src_folder(out_path, folder_name):** Moves source files from an input folder to a `src` subfolder in the output directory, maintaining the original folder structure.

6. **remove_empty_folders(start_path):** Removes all empty folders in a directory tree starting from the specified path.

7. **_create_examples_tree() and _rename_cc_to_cpp()** are imported from the `create_tflm_tree` module to generate example projects and rename `.cc` files to `.cpp`.

## Running the Script

To run the script, you need to provide the version string as an argument:

```bash
python3 tensorflow-examples/create_example_projects.py "1.0.0"
