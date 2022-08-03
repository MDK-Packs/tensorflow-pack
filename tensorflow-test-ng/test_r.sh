#!/bin/sh
# Create string with list of yml inventorys to run
inventory_list="generic_tests.yml kernel_tests_cmsis.yml test_tests.yml"
<<<<<<< Updated upstream
=======
#inventory_list="test_tests.yml"
>>>>>>> Stashed changes

rm -R ./tensorflow-pack/tensorflow-test-ng/Source
mkdir ./tensorflow-pack/tensorflow-test-ng/Source

for inventory in $inventory_list; do
    python3 ./tensorflow-pack/tensorflow-test-ng/copy_sources.py \
    --tflm_path=./tensorflow-pack/tensorflow-build/rel/mlplatform/core_software/tflite_micro \
    --inventory=./tensorflow-pack/tensorflow-test-ng/$inventory \
    --out_path=./tensorflow-pack/tensorflow-test-ng/Source
done

rm -R ./tensorflow-pack/tensorflow-test-ng/gen
mkdir ./tensorflow-pack/tensorflow-test-ng/gen

for inventory in $inventory_list; do
    python3 ./tensorflow-pack/tensorflow-test-ng/create_tests.py \
    --inventory=./tensorflow-pack/tensorflow-test-ng/$inventory  \
    --out_path=./tensorflow-pack/tensorflow-test-ng/gen
done