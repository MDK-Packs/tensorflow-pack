
# Patch 24-02.1 : Use correct registers for CMSIS6 Core 
# Approach      : Use sed to replace CoreDebug symbol with new name DCB ind ./src/tensorflow/lite/micro/cortex_m_generic/micro_time.cpp
# Files         : ./src/tensorflow/lite/micro/cortex_m_generic/micro_time.cpp
echo "Applying Patch 24-02.1"
sed -i 's/CoreDebug/DCB/g' ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/cortex_m_generic/micro_time.cpp


# Patch 24-02.2 : Add RecordingMicroAllocator
# Approach      : cp files from ./tensorflow-pack/tensorflow-build/rel/mlplatform/core_software/tflite_micro/tensorflow/lite/micro/
#                 to            ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/    
# Files         : recording_micro_allocator.cpp, recording_micro_allocator.h, recording_micro_interpreter.cpp 
echo "Applying Patch 24-02.2"
cp ./tensorflow-pack/tensorflow-build/rel/mlplatform/core_software/tflite_micro/tensorflow/lite/micro/recording_micro_allocator.cc ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/recording_micro_allocator.cpp
cp ./tensorflow-pack/tensorflow-build/rel/mlplatform/core_software/tflite_micro/tensorflow/lite/micro/recording_micro_allocator.h ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/recording_micro_allocator.h
cp ./tensorflow-pack/tensorflow-build/rel/mlplatform/core_software/tflite_micro/tensorflow/lite/micro/recording_micro_interpreter.h ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/recording_micro_interpreter.h

# Patch 24.08.1: Remove unnecessary files 
# Approach      : Remove unnecessary files from ./tensorflow-pack/tensorflow-build/rel/mlplatform/core_software/tflite_micro/tensorflow/lite/micro/ and the file lists *.lst
# Files         : static_vector.h, static_vector_test.cpp, span_test.cpp
echo "Applying Patch 24-08.1"
[ -f ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/static_vector.h ] && rm ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/static_vector.h
[ -f ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/static_vector_test.cpp ] && rm ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/static_vector_test.cpp
[ -f ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/span_test.cpp ] && rm ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/span_test.cpp
grep -v 'static_vector.h' ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst
grep -v 'static_vector_test.cc' ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst
grep -v 'span_test.cc' ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst
grep -v 'static_vector.h' ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst
grep -v 'static_vector_test.cc' ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst
grep -v 'span_test.cc' ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst
grep -v 'static_vector.h' ./tensorflow-pack/tensorflow-build/srcs.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.lst
grep -v 'static_vector_test.cc' ./tensorflow-pack/tensorflow-build/srcs.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.lst
grep -v 'span_test.cc' ./tensorflow-pack/tensorflow-build/srcs.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.lst