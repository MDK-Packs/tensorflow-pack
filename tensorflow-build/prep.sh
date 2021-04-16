#!/bin/sh
ref_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 microlite printvar-tagged-MICROLITE_CC_SRCS"
ref_hdr_make="printvar-tagged-MICROLITE_CC_HDRS"
util_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 microlite printvar-tagged-MICROLITE_CC_BASE_SRCS"
nn_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 microlite printvar-tagged-MICROLITE_CC_SRCS"
nn_hdr_make="-printvar-tagged-MICROLITE_CC_HDRS"
ethos_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 TARGET_ARCH=cortex-m55 CO_PROCESSOR=ethos_u microlite printvar-tagged-MICROLITE_CC_SRCS"
ethos_hdr_make="CO_PROCESSOR=ethos_u microlite printvar-tagged-MICROLITE_CC_HDRS"
test_src_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 microlite printvar-tagged-MICROLITE_TEST_SRCS"
test_hdr_make="-j8 TARGET=cortex_m_generic TARGET_ARCH=cortex-m55 microlite printvar-tagged-MICROLITE_TEST_HDRS"


cd /workspace/host/tensorflow
tensorflow/lite/micro/tools/make/download_and_extract.sh "http://mirror.tensorflow.org/github.com/mborgerding/kissfft/archive/v130.zip" "438ba1fef5783cc5f5f201395cc477ca" tensorflow/lite/micro/tools/make/downloads/kissfft patch_kissfft

make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $ref_src_make > /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $ref_hdr_make > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $util_src_make > /workspace/host/tensorflow-pack/tensorflow-build/util_srcs.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $nn_src_make > /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $nn_src_make > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $ethos_src_make > /workspace/host/tensorflow-pack/tensorflow-build/srcs.ethos.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $ethos_hdr_make > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.ethos.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $test_src_make > /workspace/host/tensorflow-pack/tensorflow-build/srcs.test.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak $test_hdr_make > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.test.lst
