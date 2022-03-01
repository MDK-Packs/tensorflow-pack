#!/bin/sh

python3 ./tensorflow-pack/tensorflow-build/generate_cmsis_pack.py  --release --tensorflow_path=./tensorflow --input_template=./tensorflow-pack/tensorflow-build/template/cmsis_pdsc.tpl  --srcs=./tensorflow-pack/tensorflow-build/srcs.lst --hdrs=./tensorflow-pack/tensorflow-build/hdrs.lst --hdrs-cmsis-nn=./tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst --srcs-cmsis-nn=./tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst --hdrs-ethos=./tensorflow-pack/tensorflow-build/srcs.ethos.lst --srcs-ethos=./tensorflow-pack/tensorflow-build/hdrs.ethos.lst --testhdrs=./tensorflow-pack/tensorflow-build/srcs.test.lst --testsrcs=./tensorflow-pack/tensorflow-build/hdrs.test.lst --util_src=./tensorflow-pack/tensorflow-build/util_srcs.lst

























