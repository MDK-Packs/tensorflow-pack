#!/bin/sh

# Iterate through all folders in ./gen 
# and generate test projects
for folder in ./gen/*; do
    # increment counter
    echo Package $folder
    # Generate test project
    csolution convert -n -s $folder/Validation.csolution.yml -o $folder/
done

for folder in ./gen/*; do
    for target in $folder/*; do
        #find .cprj file in target folder
        cprj_file=$(find $target -name "*.cprj")
        #if cprj file exists
        if [ -f "$cprj_file" ]; then
          echo "Building: " $cprj_file
          cbuild $cprj_file > $target/build.log
          python3 avh_exec_test.py --project=$cprj_file > $target/test_result.log
          python3 record_test_results.py --results=$target/test_result.log
        fi
    done
done
