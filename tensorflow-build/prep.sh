cd /workspace/host/tensorflow

make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak TAGS= TARGET=cortex_m_generic printvar-tagged-MICROLITE_CC_SRCS > /workspace/host/tensorflow-pack/tensorflow-build/srcs.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak TAGS= TARGET=cortex_m_generic printvar-tagged-MICROLITE_CC_HDRS > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak TAGS=cmsis-nn TARGET=cortex_m_generic printvar-tagged-MICROLITE_CC_SRCS > /workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak TAGS=cmsis-nn TARGET=cortex_m_generic printvar-tagged-MICROLITE_CC_HDRS > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak TAGS=ethos-u TARGET=cortex_m_generic printvar-tagged-MICROLITE_CC_SRCS > /workspace/host/tensorflow-pack/tensorflow-build/srcs.ethos.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak TAGS=ethos-u TARGET=cortex_m_generic printvar-tagged-MICROLITE_CC_HDRS > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.ethos.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak TAGS= TARGET=cortex_m_generic printvar-tagged-MICROLITE_TEST_SRCS > /workspace/host/tensorflow-pack/tensorflow-build/srcs.test.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f /workspace/host/tensorflow-pack/tensorflow-build/make/print.mak TAGS= TARGET=cortex_m_generic printvar-tagged-MICROLITE_TEST_HDRS > /workspace/host/tensorflow-pack/tensorflow-build/hdrs.test.lst

