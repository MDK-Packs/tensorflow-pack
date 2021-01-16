rm *.lst
cd ../tensorflow
make -f tensorflow/lite/micro/tools/make/Makefile -f ../tensorflow-build/make/print.mak TAGS= TARGET=cortex_m_generic_makefile printvar-tagged-MICROLITE_CC_SRCS > ../tensorflow-build/srcs.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f ../tensorflow-build/make/print.mak TAGS= TARGET=cortex_m_generic_makefile printvar-tagged-MICROLITE_CC_HDRS > ../tensorflow-build/hdrs.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f ../tensorflow-build/make/print.mak TAGS=cmsis-nn TARGET=cortex_m_generic_makefile printvar-tagged-MICROLITE_CC_SRCS > ../tensorflow-build/srcs.cmsis-nn.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f ../tensorflow-build/make/print.mak TAGS=cmsis-nn TARGET=cortex_m_generic_makefile printvar-tagged-MICROLITE_CC_HDRS > ../tensorflow-build/hdrs.cmsis-nn.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f ../tensorflow-build/make/print.mak TAGS=ethos-u TARGET=cortex_m_generic_makefile printvar-tagged-MICROLITE_CC_SRCS > ../tensorflow-build/srcs.ethos.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f ../tensorflow-build/make/print.mak TAGS=ethos-u TARGET=cortex_m_generic_makefile printvar-tagged-MICROLITE_CC_HDRS > ../tensorflow-build/hdrs.ethos.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f ../tensorflow-build/make/print.mak TAGS= TARGET=cortex_m_generic_makefile printvar-tagged-MICROLITE_TEST_SRCS > ../tensorflow-build/srcs.test.lst
make -f tensorflow/lite/micro/tools/make/Makefile -f ../tensorflow-build/make/print.mak TAGS= TARGET=cortex_m_generic_makefile printvar-tagged-MICROLITE_TEST_HDRS > ../tensorflow-build/hdrs.test.lst


