#!/bin/sh

echo "Starting 3rd-Party builds for revision :" $1 $2

cd ./tensorflow-pack/3rdparty-build

# Check if path exists or exit
if [ ! -d "./src" ]; then
    echo "Path ./3rdparty-build/src does not exist. Exiting."
    echo "Make sure to execute tensorflow-build/build_r.sh first."
    exit 1
fi

# Build Ethos-U driver pack
python3 gen_pack.py --path ethos-u-driver --version 1.$1  --candidate_rev=$2 
cp ./ethos-u-driver/build/*.pack ./
# Build flatbuffers pack
python3 gen_pack.py --path flatbuffers --version 1.$1 --candidate_rev=$2 
cp ./flatbuffers/build/*.pack ./
# Build gemmlowp pack
python3 gen_pack.py --path gemmlowp --version 1.$1 --candidate_rev=$2 
cp ./gemmlowp/build/*.pack ./
# Build ruy pack
python3 gen_pack.py --path ruy --version 1.$1 --candidate_rev=$2 
cp ./ruy/build/*.pack ./
# Build kissfft pack
python3 gen_pack.py --path kissfft --version 1.$1 --candidate_rev=$2 
cp ./kissfft/build/*.pack ./







