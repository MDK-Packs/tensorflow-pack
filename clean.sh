#!/bin/sh

rm -rf ./tensorflow-build/gen
rm -rf ./tensorflow-build/src
rm -rf ./tensorflow-build/rel
rm -rf ./3rdparty-build/src

# Traverse through all subdirectories and find folders with the name "build"
# and delete the folder.
for dir in $(find . -type d -name "build"); do
    rm -rf $dir
done

