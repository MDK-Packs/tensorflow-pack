import os
import shutil
import sys
import yaml
import os
import argparse

# Add the parent directory of the module to sys.path
module_parent_dir = "./tflite-micro/tensorflow/lite/micro/tools/project_generation"
sys.path.insert(0, module_parent_dir)

# Import the module
from create_tflm_tree import _create_examples_tree, _rename_cc_to_cpp

def list_subfolders(path):
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

def create_csolution_yml(out_path, cproject_files):
    csolution_yml = {
        'solution': {
            'compiler': 'GCC',
            'packs': [
                {'pack': 'ARM::CMSIS@5.9.0'},
                {'pack': 'ARM::CMSIS-NN@4.0.0'},
                {'pack': 'ARM::CMSIS-DSP@1.14.4'},
                {'pack': 'Keil::V2M-MPS2_CMx_BSP@1.8.0'},
                {'pack': 'tensorflow::tensorflow-lite-micro'},
                {'pack': 'tensorflow::flatbuffers'},
                {'pack': 'tensorflow::ruy'},
                {'pack': 'tensorflow::kissfft'},
                {'pack': 'tensorflow::gemmlowp'},
            ],
            'target-types': [
                {
                    'type': 'AVH',
                    'device': 'CMSDK_CM7_SP_VHT',
                },
            ],
            'build-types': [
                {
                    'type': 'Debug',
                    'debug': 'on',
                    'optimize': 'size',
                },
                {
                    'type': 'Release',
                    'debug': 'off',
                    'optimize': 'size',
                },
            ],
            'projects': [{'project': os.path.join('.', folder, p)} for folder, p in cproject_files],
        }
    }

    csolution_yml_path = os.path.join(out_path, 'tflite_micro_examples.csolution.yml')
    
    with open(csolution_yml_path, 'w') as outfile:
        yaml.dump(csolution_yml, outfile, default_flow_style=False, sort_keys=False)

    print(f"Created 'tflite_micro_examples.csolution.yml' in '{out_path}'")

def create_cproject_yml(folder_path, folder_name):
    cproject_yml = {
        'project': {
           'layers': [
                {'layer': '../../Layer/Target/CM7_SP_VHT_GCC/Target.clayer.yml'},
            ],
            'add-path': [
                './src',
            ],
            'groups': [],
            'components': [
                {'component': 'CMSIS:DSP&Source'},
                {'component': 'CMSIS:NN Lib'},
                {'component': 'tensorflow::Machine Learning:TensorFlow:Kernel&CMSIS-NN'},
                {'component': 'tensorflow::Machine Learning:TensorFlow:Kernel Utils'},
                {'component': 'tensorflow::Machine Learning:TensorFlow:Testing'},
                {'component': 'tensorflow::Data Exchange:Serialization:flatbuffers&tensorflow'},
                {'component': 'tensorflow::Data Processing:Math:gemmlowp fixed-point&tensorflow' },
                {'component': 'tensorflow::Data Processing:Math:kissfft&tensorflow'},
                {'component': 'tensorflow::Data Processing:Math:ruy&tensorflow'},
            ],
        }
    }

    for group_name in os.listdir(folder_path):
        print(group_name)

        group_folder = os.path.join(folder_path, group_name)
        
        if os.path.isdir(group_folder):
            files = []
            
            for root, _, file_names in os.walk(group_folder):
                for file_name in file_names:
                    file_ext = os.path.splitext(file_name)[-1]
                    if file_ext in ('.c', '.cpp', '.h'):
                        rel_path = os.path.relpath(root, folder_path)
                        files.append({'file': os.path.join(rel_path, file_name)})

            if files:
                cproject_yml['project']['groups'].append({
                    'group': group_name,
                    'files': files,
                })

    with open(os.path.join(folder_path, f"{folder_name}.cproject.yml"), 'w') as outfile:
        yaml.dump(cproject_yml, outfile, default_flow_style=False, sort_keys=False)

def list_subfolders_with_makefile_inc(path):
    subfolders = []
    for d in os.listdir(path):
        full_path = os.path.join(path, d)
        if os.path.isdir(full_path) and os.path.isfile(os.path.join(full_path, "Makefile.inc")):
            subfolders.append(d)
    # Workaround, use custom list for now as some miss the list_x_example_sources target
    subfolders = ["hello_world", "person_detection", "micro_speech"]

    return subfolders

def move_sources_to_src_folder(out_path, folder_name):
    src_folder = os.path.join(out_path, 'src')
    os.makedirs(src_folder, exist_ok=True)

    for root, dirs, files in os.walk(out_path):
        if root == src_folder:
            continue

        rel_path = os.path.relpath(root, out_path)
        if rel_path.startswith('src'):
            continue

        for file in files:
            file_ext = os.path.splitext(file)[-1]
            if file_ext in ('.c', '.cpp', '.h'):
                file_path = os.path.join(root, file)
                
                if folder_name in rel_path:
                    new_rel_path = rel_path.split(folder_name)[-1].lstrip('/')
                else:
                    new_rel_path = rel_path.split('examples/', 1)[-1]
                
                new_path = os.path.join(src_folder, new_rel_path, file)
                new_folder = os.path.dirname(new_path)
                os.makedirs(new_folder, exist_ok=True)
                shutil.move(file_path, new_path) 

def remove_empty_folders(start_path):
    for root, dirs, files in os.walk(start_path, topdown=False):
        for directory in dirs:
            dir_path = os.path.join(root, directory)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Removed empty directory: {dir_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build examples from tflite-micro.")
    parser.add_argument("version", help="Version string to store for internal use.")
    args = parser.parse_args()

    version = args.version

    examples_path = "./tflite-micro/tensorflow/lite/micro/examples"
    tensorflow_root = "./tflite-micro/"

    if os.path.exists(examples_path):
        subfolders = list_subfolders_with_makefile_inc(examples_path)
        print(f"Subfolders containing 'Makefile.inc' in '{examples_path}':")
        for folder in subfolders:
            print(f" - {folder}")
            examples_tmp = []
            examples_tmp.append(folder)
            example_out = os.path.join("out", folder)
            _create_examples_tree(example_out, examples_tmp, tensorflow_root)
            _rename_cc_to_cpp(example_out)            
            move_sources_to_src_folder(example_out, folder)  # Move sources to 'src' subfolder and flatten the folder structure
            remove_empty_folders(example_out)     
            create_cproject_yml(example_out, folder)
            print(f"Created '{folder}.cproject.yml' for '{folder}'")
        cproject_files = [(folder, f"{folder}.cproject.yml") for folder in subfolders]
        create_csolution_yml("out", cproject_files)

    else:
        print(f"The path '{examples_path}' does not exist. Please make sure you've cloned the repository.")

