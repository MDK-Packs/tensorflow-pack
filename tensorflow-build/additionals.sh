# Copy sources that are statically declared in pdsc
mkdir -p /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/
mkdir /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic
cp /workspace/host/tensorflow/tensorflow/lite/micro/system_setup.cc /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/system_setup.cc
cp /workspace/host/tensorflow/tensorflow/lite/micro/cortex_m_generic/debug_log.cc /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic/debug_log.cc
cp /workspace/host/tensorflow/tensorflow/lite/micro/cortex_m_generic/micro_time.cc /workspace/host/tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic/micro_time.cc

