# Patch 25-02.1 : Error: L6200E: Symbol __ARM_use_no_argv multiply defined (by hexdump_test.o ...)
# Approach      : Use sed to replace   int main(int argc, char** argv)  with int main(void)
# Files         : ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/testing/micro_test.h
echo "Applying Patch 25-02.1"
pwd
# sed -i 's/int main(int argc, char\*\* argv)/int main(void)/g' ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/testing/micro_test.h

sed -i 's/int main(int argc, char\*\* argv)/int micro_test_main(int argc, char\*\* argv)/g' ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/testing/micro_test.h
cat ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/testing/micro_test.h


# sed -i 's/int main(int argc, char\*\* argv)/int main(void)/g' ./tensorflow-pack/tensorflow-build/rel/ethos-u-main/core_software/tflite_micro/tensorflow/lite/micro/testing/micro_test.h
sed -i 's/int main(int argc, char\*\* argv)/int micro_test_main(int argc, char\*\* argv)/g' ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/testing/micro_test.h 
cat ./tensorflow-pack/tensorflow-build/rel/ethos-u-main/core_software/tflite_micro/tensorflow/lite/micro/testing/micro_test.h