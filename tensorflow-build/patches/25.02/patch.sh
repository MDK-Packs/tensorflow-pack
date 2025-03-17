# Patch 25.02.1 : Remove unnecessary files 
# Approach      : Remove unnecessary files from folder /tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/ and the file lists srcs.cmsis_nn.lst, srcs.ethos_u.lst, and srcs.lst
# Files         : hexdump_test.cc, hexdump_test.cpp
echo "Applying Patch 25-02.1"
[ -f ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/hexdump_test.cpp ] && rm ./tensorflow-pack/tensorflow-build/gen/build/tensorflow/lite/micro/hexdump_test.cpp
grep -v 'hexdump_test.cc' ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.cmsis_nn.lst
grep -v 'hexdump_test.cc' ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.ethos_u.lst
grep -v 'hexdump_test.cc' ./tensorflow-pack/tensorflow-build/srcs.lst > temp && mv temp ./tensorflow-pack/tensorflow-build/srcs.lst
