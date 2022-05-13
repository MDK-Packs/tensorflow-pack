#!/bin/sh

echo $1
mkdir ./tensorflow-pack/tensorflow-build/rel
mkdir ./tensorflow-pack/tensorflow-build/rel/mlplatform
mkdir ./tensorflow-pack/tensorflow-build/gen
mkdir ./tensorflow-pack/tensorflow-build/gen/build
# Get ml-platforms root
wget -O ./tensorflow-pack/tensorflow-build/rel/master.tar.gz https://review.mlplatform.org/plugins/gitiles/ml/ethos-u/ethos-u/+archive/refs/heads/master.tar.gz
# Extract tar.gz
tar -xzf ./tensorflow-pack/tensorflow-build/rel/master.tar.gz -C ./tensorflow-pack/tensorflow-build/rel/mlplatform
# Get ml-platforms srcs
cd ./tensorflow-pack/tensorflow-build/rel/mlplatform/
python3 fetch_externals.py -c $1.json fetch

cd ./core_software/tflite_micro
python3 ./tensorflow/lite/micro/tools/project_generation/create_tflm_tree.py  \
   --makefile_options="TARGET=cortex_m_generic TARGET_ARCH=cortex-m7" \
   --print_src_files --rename_cc_to_cpp\
   ../../../../../tensorflow-build/src \
   > ../../../../../tensorflow-build/srcs.raw
rsync -a ../../../../../tensorflow-build/src/tensorflow ../../../../../tensorflow-build/gen/build

python3 ./tensorflow/lite/micro/tools/project_generation/create_tflm_tree.py  \
   --makefile_options="TARGET=cortex_m_generic OPTIMIZED_KERNEL_DIR=cmsis_nn TARGET_ARCH=cortex-m55" \
   --print_src_files --rename_cc_to_cpp\
   ../../../../../tensorflow-build/src \
   > ../../../../../tensorflow-build/srcs.cmsis-nn.raw
rsync -a ../../../../../tensorflow-build/src/tensorflow ../../../../../tensorflow-build/gen/build

python3 ./tensorflow/lite/micro/tools/project_generation/create_tflm_tree.py  \
   --makefile_options="TARGET=cortex_m_generic OPTIMIZED_KERNEL_DIR=cmsis_nn CO_PROCESSOR=ethos_u ETHOSU_ARCH=u55 TARGET_ARCH=cortex-m55" \
   --print_src_files \
   ../../../../../tensorflow-build/src --rename_cc_to_cpp\
   > ../../../../../tensorflow-build/srcs.ethos_u.raw
rsync -a ../../../../../tensorflow-build/src/tensorflow ../../../../../tensorflow-build/gen/build

rsync -a ../../../../../tensorflow-build/src/third_party/ ../../../../../3rdparty-build/src

cd ../../../../../..
python3 ./tensorflow-pack/tensorflow-build/clean_file_list.py \
        ./tensorflow-pack/tensorflow-build/srcs.raw > ./tensorflow-pack/tensorflow-build/srcs.lst
python3 ./tensorflow-pack/tensorflow-build/clean_file_list.py \
        ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.raw > ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
python3 ./tensorflow-pack/tensorflow-build/clean_file_list.py \
        ./tensorflow-pack/tensorflow-build/srcs.ethos_u.raw > ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst

python3 ./tensorflow-pack/tensorflow-build/generate_cmsis_pack.py  \
   --release=1.$1-RC \
   --input_template=./tensorflow-pack/tensorflow-build/template/cmsis_pdsc.tpl \
   --tensorflow_path=./tensorflow-pack/tensorflow-build/src \
   --srcs=./tensorflow-pack/tensorflow-build/srcs.lst \
   --hdrs=./tensorflow-pack/tensorflow-build/empty.lst \
   --hdrs-cmsis-nn=./tensorflow-pack/tensorflow-build/empty.lst \
   --srcs-cmsis-nn=./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst \
   --hdrs-ethos=./tensorflow-pack/tensorflow-build/empty.lst \
   --srcs-ethos=./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst \
   --testhdrs=./tensorflow-pack/tensorflow-build/empty.lst \
   --testsrcs=./tensorflow-pack/tensorflow-build/empty.lst \
   --util_src=./tensorflow-pack/tensorflow-build/empty.lst  

























