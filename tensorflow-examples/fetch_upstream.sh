#!/bin/bash

repo_url="https://github.com/tensorflow/tflite-micro.git"
dest_dir="tflite-micro"

if git clone --depth 1 "$repo_url" "$dest_dir"; then
    examples_dir="$dest_dir/tensorflow/lite/micro/examples"
    echo "Cloned repository '$repo_url' into '$dest_dir'"
    echo "TensorFlow Lite Micro examples are available in '$examples_dir'"
else
    echo "Unable to clone the repository. Please check the URL and your internet connection."
fi
