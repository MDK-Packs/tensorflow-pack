# Use the specified image as the base
FROM ghcr.io/arm-software/avh-mlops/arm-mlops-docker-licensed-community:latest

# Set the working directory in the container
WORKDIR /tensorflow-pack

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install rsync wget git zip curl -y --fix-missing

RUN pip3 install pillow requests six semantic_version pyyml

#RUN su -l arm_mlops_docker -c "cpackget index --force https://www.keil.com/pack/index.pidx"