#!/bin/sh -v

# Mark up source list for generate_cmsis_pack.py 
sed -i 's/echo/<LIST>/g'  ./tensorflow-pack/tensorflow-build/srcs.lst
sed -i '$a </LIST>' ./tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/echo/<LIST>/g' ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i '$a </LIST>' ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/echo/<LIST>/g' ./tensorflow-pack/tensorflow-build/srcs.ethos.lst
sed -i '$a </LIST>' ./tensorflow-pack/tensorflow-build/srcs.ethos.lst

sed -i 's/echo/<LIST>/g' ./tensorflow-pack/tensorflow-build/hdrs.lst
sed -i '$a </LIST>' ./tensorflow-pack/tensorflow-build/hdrs.lst
sed -i 's/echo/<LIST>/g' ./tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i '$a </LIST>' ./tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/echo/<LIST>/g' ./tensorflow-pack/tensorflow-build/hdrs.ethos.lst
sed -i '$a </LIST>' ./tensorflow-pack/tensorflow-build/hdrs.ethos.lst

# Add debug_log_callback.h to source lists
sed -i 's/<LIST>/<LIST>tensorflow\/lite\/micro\/cortex_m_generic\/debug_log_callback.h /' ./tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/<LIST>/<LIST>tensorflow\/lite\/micro\/cortex_m_generic\/debug_log_callback.h /' ./tensorflow-pack/tensorflow-build/hdrs.ethos.lst
sed -i 's/<LIST>/<LIST>tensorflow\/lite\/micro\/cortex_m_generic\/debug_log_callback.h /' ./tensorflow-pack/tensorflow-build/hdrs.lst

# Remove conv_test_common.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/kernels\/conv_test_common.cc / /' ./tensorflow-pack/tensorflow-build/srcs.ethos.lst
sed -i 's/tensorflow\/lite\/micro\/kernels\/conv_test_common.cc / /' ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/kernels\/conv_test_common.cc / /' ./tensorflow-pack/tensorflow-build/srcs.lst

# Remove system_setup.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' ./tensorflow-pack/tensorflow-build/srcs.ethos.lst
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' ./tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' ./tensorflow-pack/tensorflow-build/util_srcs.lst

# Remove micro_time.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/micro_time.cc / /' ./tensorflow-pack/tensorflow-build/srcs.ethos.lst
sed -i 's/tensorflow\/lite\/micro\/micro_time.cc / /' ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/micro_time.cc / /' ./tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/micro_time.cc / /' ./tensorflow-pack/tensorflow-build/util_srcs.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/micro_time.cc / /' ./tensorflow-pack/tensorflow-build/srcs.ethos.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/micro_time.cc / /' ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/micro_time.cc / /' ./tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/micro_time.cc / /' ./tensorflow-pack/tensorflow-build/util_srcs.lst

# Remove debug_log.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/debug_log.cc / /' ./tensorflow-pack/tensorflow-build/srcs.ethos.lst
sed -i 's/tensorflow\/lite\/micro\/debug_log.cc / /' ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/debug_log.cc / /' ./tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/debug_log.cc / /' ./tensorflow-pack/tensorflow-build/util_srcs.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/debug_log.cc / /' ./tensorflow-pack/tensorflow-build/srcs.ethos.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/debug_log.cc / /' ./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/debug_log.cc / /' ./tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/debug_log.cc / /' ./tensorflow-pack/tensorflow-build/util_srcs.lst

# Remove default ethosu.cc from ethosu cvariant
sed -i 's/tensorflow\/lite\/micro\/kernels\/ethosu.cc /tensorflow\/lite\/micro\/kernels\/ethos_u\/ethosu.cc  /' ./tensorflow-pack/tensorflow-build/srcs.ethos.lst

# Copy sources that are statically declared in pdsc
mkdir -p ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/
mkdir -p ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic
cp ./tensorflow/tensorflow/lite/micro/system_setup.cc ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/system_setup.cc
cp ./tensorflow/tensorflow/lite/micro/cortex_m_generic/debug_log.cc ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic/debug_log.cc
cp ./tensorflow/tensorflow/lite/micro/cortex_m_generic/micro_time.cc ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic/micro_time.cc

