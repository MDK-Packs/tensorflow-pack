cd /workspace

docker run -i -v /workspace:/workspace/host --mac-address="00:02:F7:FF:55:55" --name build_runtime -d armswdev/cmsis_tools_m55:latest 
docker exec build_runtime pip3 install six requests pyyaml junit_xml

git clone https://github.com/tensorflow/tflite-micro.git tensorflow
docker exec build_runtime /bin/bash /workspace/host/tensorflow-pack/tensorflow-build/prep.sh
docker exec build_runtime /bin/bash /workspace/host/tensorflow-pack/tensorflow-build/hotfix.sh
docker exec build_runtime /bin/bash /workspace/host/tensorflow-pack/tensorflow-build/build.sh

docker stop build_runtime
docker rm build_runtime
