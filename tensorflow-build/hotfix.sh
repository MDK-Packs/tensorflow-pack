#!/bin/sh

# Add debug_log_callback.h to source lists
sed -i 's/<LIST>/<LIST>tensorflow\/lite\/micro\/cortex_m_generic\/debug_log_callback.h /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/<LIST>/<LIST>tensorflow\/lite\/micro\/cortex_m_generic\/debug_log_callback.h /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.ethos.lst
sed -i 's/<LIST>/<LIST>tensorflow\/lite\/micro\/cortex_m_generic\/debug_log_callback.h /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.lst

# Remove Generic Debug_log.cc from Kernel Utils
sed -i 's/tensorflow\/lite\/micro\/debug_log.cc/ /' util_srcs.lst

# Remove conv_test_common.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/kernels\/conv_test_common.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/kernels\/conv_test_common.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/kernels\/conv_test_common.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst

# Remove system_setup.cc from all lists
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
sed -i 's/tensorflow\/lite\/micro\/system_setup.cc / /' /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst
