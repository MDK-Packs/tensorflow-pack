# Patch 25-02.1 : Error: L6200E: Symbol __ARM_use_no_argv multiply defined (by hexdump_test.o ...)
# Approach      : Use sed to replace       ./src/tensorflow/lite/micro/cortex_m_generic/micro_time.cpp
# Files         : ./src/tensorflow/lite/micro/cortex_m_generic/micro_time.cpp
echo "Applying Patch 25-02.1"

sed -i 's/int main(int argc, char\*\* argv)/int main(void)/g'   ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/micro_test.h
