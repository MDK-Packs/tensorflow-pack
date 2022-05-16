#!/bin/sh

echo "Starting 3rd-Party builds for revision :" $1

# Check if path exists or exit
if [ ! -d "./3rdparty-build/src" ]; then
    echo "Path ./3rdparty-build/src does not exist. Exiting."
    echo "Make sure to execute tensorflow-build/build_r.sh first."
    exit 1
fi

# Build Ethos-U driver pack
python3 gen_pack.py --path ethos-u-driver --version 1.$1
cp ./ethos-u-driver/build/*.pack ../out/
# Build flatbuffers pack
python3 gen_pack.py --path flatbuffers --version 1.$1
cp ./flatbuffers/build/*.pack ../out/
# Build gemmlowp pack
python3 gen_pack.py --path gemmlowp --version 1.$1
cp ./gemmlowp/build/*.pack ../out/
# Build ruy pack
python3 gen_pack.py --path ruy --version 1.$1
cp ./ruy/build/*.pack ../out/
# Build kissfft pack
python3 gen_pack.py --path kissfft --version 1.$1
cp ./kissfft/build/*.pack ../out/







