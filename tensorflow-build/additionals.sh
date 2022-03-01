# Copy sources that are statically declared in pdsc
mkdir -p ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/
mkdir ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic
cp ./tensorflow/tensorflow/lite/micro/system_setup.cc ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/system_setup.cc
cp ./tensorflow/tensorflow/lite/micro/cortex_m_generic/debug_log.cc ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic/debug_log.cc
cp ./tensorflow/tensorflow/lite/micro/cortex_m_generic/micro_time.cc ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic/micro_time.cc

