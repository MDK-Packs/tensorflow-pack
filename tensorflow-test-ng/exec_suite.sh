#!/bin/sh

# Iterate through all folders in ./gen 
# and generate test projects
for folder in ./gen/*; do
    csolution convert -s $folder/Validation.csolution.yml -o $folder/
done

for folder in ./gen/*; do
    for target in $folder/*; do
        #find .cprj file in target folder
        cprj_file=$(find $target -name "*.cprj")
        cbuild $cprj_file
    done
done
