#!/bin/sh -v 
ref_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 list_library_sources"
ref_hdr_make="list_library_headers"
nn_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 OPTIMIZED_KERNEL_DIR=cmsis_nn list_library_sources"
nn_hdr_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 OPTIMIZED_KERNEL_DIR=cmsis_nn list_library_headers"
#ethos_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 OPTIMIZED_KERNEL_DIR=cmsis_nn TARGET_ARCH=cortex-m55 CO_PROCESSOR=ethos_u list_library_sources"
ethos_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 OPTIMIZED_KERNEL_DIR=cmsis_nn list_library_sources"
ethos_hdr_make="list_library_headers"

util_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 build printvar-tagged-MICROLITE_CC_BASE_SRCS"

test_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 build printvar-tagged-MICROLITE_TEST_SRCS"
test_hdr_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 build printvar-tagged-MICROLITE_TEST_HDRS"


cd /workspace/host/tensorflow
#Download additional software
make -f tensorflow/lite/micro/tools/make/Makefile third_party_downloads 

make -n -f tensorflow/lite/micro/tools/make/Makefile $ref_src_make  > /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst
make -n -f tensorflow/lite/micro/tools/make/Makefile $ref_hdr_make > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.lst
make -n -f tensorflow/lite/micro/tools/make/Makefile $nn_src_make > /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
make -n -f tensorflow/lite/micro/tools/make/Makefile $nn_hdr_make > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
make -n -f tensorflow/lite/micro/tools/make/Makefile $ethos_src_make > /workspace/host/tensorflow-pack/tensorflow-build/srcs.ethos.lst
make -n -f tensorflow/lite/micro/tools/make/Makefile $ethos_hdr_make > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.ethos.lst

make -n -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $util_src_make > /workspace/host/tensorflow-pack/tensorflow-build/util_srcs.lst

make -n -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $test_src_make > /workspace/host/tensorflow-pack/tensorflow-build/srcs.test.lst
make -n -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $test_hdr_make > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.test.lst
