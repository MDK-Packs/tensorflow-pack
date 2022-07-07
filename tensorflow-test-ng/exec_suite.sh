#!/bin/sh

counter = 0
# Iterate through all folders in ./gen 
# and generate test projects
for folder in ./gen/*; do
    # increment counter
    echo Package $counter $folder
    ((counter=counter+1))
    # Generate test project
    csolution convert -s $folder/Validation.csolution.yml -o $folder/
done

counter = 0
for folder in ./gen/*; do
    echo Package $counter $folder
    ((counter=counter+1))
    for target in $folder/*; do
        #find .cprj file in target folder
        cprj_file=$(find $target -name "*.cprj")  
        echo "Building: " $cprj_file
        cbuild $cprj_file > $target/build.log
        python3 avh_exec_test.py --project=$cprj_file > $target/test_result.log
        python3 record_test_results.py --results=$target/test_result.log
    done
done
