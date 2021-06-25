#!/bin/sh

# Add debug_log_callback.h to source lists
sed -i 's/<LIST>/<LIST>tensorflow\/lite\/micro\/cortex_m_generic\/debug_log_callback.h /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/<LIST>/<LIST>tensorflow\/lite\/micro\/cortex_m_generic\/debug_log_callback.h /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.ethos.lst
sed -i 's/<LIST>/<LIST>tensorflow\/lite\/micro\/cortex_m_generic\/debug_log_callback.h /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.lst

# Remove conv_test_common.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/kernels\/conv_test_common.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/kernels\/conv_test_common.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/kernels\/conv_test_common.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst

# Remove system_setup.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/util_srcs.lst

# Remove micro_time.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/micro_time.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/micro_time.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/micro_time.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/micro_time.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/util_srcs.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/micro_time.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/micro_time.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/micro_time.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/micro_time.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/util_srcs.lst

# Remove debug_log.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/debug_log.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/debug_log.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/debug_log.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/debug_log.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/util_srcs.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/debug_log.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/debug_log.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/debug_log.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst
sed -i 's/tensorflow\/lite\/micro\/cortex_m_generic\/debug_log.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/util_srcs.lst

# Copy sources that are statically declared in pdsc
mkdir -p /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/
mkdir /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic
cp /workspace/host/tensorflow/tensorflow/lite/micro/system_setup.cc /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/system_setup.cc
cp /workspace/host/tensorflow/tensorflow/lite/micro/cortex_m_generic/debug_log.cc /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic/debug_log.cc
cp /workspace/host/tensorflow/tensorflow/lite/micro/cortex_m_generic/micro_time.cc /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic/micro_time.cc

