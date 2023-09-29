#!/bin/sh

echo "Starting 3rd-Party Building from latest main branch - nightly build:" $1


cd ./tensorflow-pack/3rdparty-build

# Check if path exists or exit
if [ ! -d "./src" ]; then
    echo "Path ./3rdparty-build/src does not exist. Exiting."
    echo "Make sure to execute tensorflow-build/build_r.sh first."
    exit 1
fi

# Build Ethos-U driver pack
python3 gen_pack.py --path ethos-u-driver --version 1.99.0  --candidate_rev=$1 --history=../../tensorflow-pack/tensorflow-build/history.txt
cp ./ethos-u-driver/build/*.pack ../out
# Build flatbuffers pack
python3 gen_pack.py --path flatbuffers --version 1.99.0 --candidate_rev=$1 --history=../../tensorflow-pack/tensorflow-build/history.txt
cp ./flatbuffers/build/*.pack ../out
# Build gemmlowp pack
python3 gen_pack.py --path gemmlowp --version 1.99.0 --candidate_rev=$1 --history=../../tensorflow-pack/tensorflow-build/history.txt
cp ./gemmlowp/build/*.pack ../out
# Build ruy pack
python3 gen_pack.py --path ruy --version 1.99.0 --candidate_rev=$1 --history=../../tensorflow-pack/tensorflow-build/history.txt
cp ./ruy/build/*.pack ../ou
# Build kissfft pack
python3 gen_pack.py --path kissfft --version 1.99.0 --candidate_rev=$1 --history=../../tensorflow-pack/tensorflow-build/history.txt
cp ./kissfft/build/*.pack ../out







