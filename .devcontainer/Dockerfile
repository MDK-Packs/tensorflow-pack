# Use the specified image as the base
FROM ghcr.io/arm-software/avh-mlops/arm-mlops-docker-licensed-community:latest

# Set the working directory in the container
WORKDIR /tensorflow-pack

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install rsync wget git zip curl ninja-build -y --fix-missing

RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN sh ./get-docker.sh

RUN pip3 install pillow requests six semantic_version pyyml

ENV DOCKER_HOST=unix:///var/run/user/1000/docker.sock
