#!/bin/sh


echo Building from latest main branch - nightly build" $1

mkdir ./tensorflow-pack/tensorflow-build/rel
mkdir ./tensorflow-pack/tensorflow-build/rel/mlplatform
mkdir ./tensorflow-pack/tensorflow-build/gen
mkdir ./tensorflow-pack/tensorflow-build/gen/build
# Get ml-platforms root
wget -O ./tensorflow-pack/tensorflow-build/rel/master.tar.gz https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u/-/archive/main/ethos-u-main.tar.gz
# Extract tar.gz
tar -xzf ./tensorflow-pack/tensorflow-build/rel/master.tar.gz -C ./tensorflow-pack/tensorflow-build/rel/mlplatform
# Get ml-platforms srcs
cd ./tensorflow-pack/tensorflow-build/rel/mlplatform/

echo Fetching ml-platforms sources
python3 fetch_externals.py fetch


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
   > ../../../../../tensorflow-build/srcs.cmsis_nn.raw
rsync -a ../../../../../tensorflow-build/src/tensorflow ../../../../../tensorflow-build/gen/build

python3 ./tensorflow/lite/micro/tools/project_generation/create_tflm_tree.py  \
   --makefile_options="TARGET=cortex_m_generic OPTIMIZED_KERNEL_DIR=cmsis_nn CO_PROCESSOR=ethos_u ETHOSU_ARCH=u55 TARGET_ARCH=cortex-m55" \
   --print_src_files \
   ../../../../../tensorflow-build/src --rename_cc_to_cpp\
   > ../../../../../tensorflow-build/srcs.ethos_u.raw
rsync -a ../../../../../tensorflow-build/src/tensorflow ../../../../../tensorflow-build/gen/build

rsync -a ./tensorflow/lite/micro/testing/*.h ../../../../../tensorflow-build/gen/build/tensorflow/lite/micro/testing/ 

rsync -a ../../../../../tensorflow-build/src/third_party/ ../../../../../3rdparty-build/src
rsync -a ../core_driver/ ../../../../../3rdparty-build/src/ethos_u_core_driver

cd ../../../../../..
python3 ./tensorflow-pack/tensorflow-build/clean_file_list.py \
        ./tensorflow-pack/tensorflow-build/srcs.raw > ./tensorflow-pack/tensorflow-build/srcs.lst
python3 ./tensorflow-pack/tensorflow-build/clean_file_list.py \
        ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.raw > ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst
python3 ./tensorflow-pack/tensorflow-build/clean_file_list.py \
        ./tensorflow-pack/tensorflow-build/srcs.ethos_u.raw > ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst


python3 ./tensorflow-pack/tensorflow-build/generate_cmsis_pack.py  \
   --release=1.99 \
   --candidate_rev=$1 \
   --input_template=./tensorflow-pack/tensorflow-build/template/cmsis_pdsc.tpl \
   --history=./tensorflow-pack/tensorflow-build/history.txt \
   --tensorflow_path=./tensorflow-pack/tensorflow-build/src \
   --srcs=./tensorflow-pack/tensorflow-build/srcs.lst \
   --hdrs=./tensorflow-pack/tensorflow-build/empty.lst \
   --hdrs-cmsis-nn=./tensorflow-pack/tensorflow-build/empty.lst \
   --srcs-cmsis-nn=./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst \
   --hdrs-ethos=./tensorflow-pack/tensorflow-build/empty.lst \
   --srcs-ethos=./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst \
   --testhdrs=./tensorflow-pack/tensorflow-build/empty.lst \
   --testsrcs=./tensorflow-pack/tensorflow-build/testsrcs.lst \
   --util_src=./tensorflow-pack/tensorflow-build/empty.lst  

























