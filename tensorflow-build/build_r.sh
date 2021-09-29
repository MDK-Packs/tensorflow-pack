#!/bin/sh

python3 /workspace/host/tensorflow-pack/tensorflow-build/generate_cmsis_pack.py  --release --tensorflow_path=/workspace/host/tensorflow --input_template=/workspace/host/tensorflow-pack/tensorflow-build/template/cmsis_pdsc.tpl  --srcs=/workspace/host/tensorflow-pack/tensorflow-build/srcs.lst --hdrs=/workspace/host/tensorflow-pack/tensorflow-build/hdrs.lst --hdrs-cmsis-nn=/workspace/host/tensorflow-pack/tensorflow-build/srcs.cmsis-nn.lst --srcs-cmsis-nn=/workspace/host/tensorflow-pack/tensorflow-build/hdrs.cmsis-nn.lst --hdrs-ethos=/workspace/host/tensorflow-pack/tensorflow-build/srcs.ethos.lst --srcs-ethos=/workspace/host/tensorflow-pack/tensorflow-build/hdrs.ethos.lst --testhdrs=/workspace/host/tensorflow-pack/tensorflow-build/srcs.test.lst --testsrcs=/workspace/host/tensorflow-pack/tensorflow-build/hdrs.test.lst --util_src=/workspace/host/tensorflow-pack/tensorflow-build/util_srcs.lst

























