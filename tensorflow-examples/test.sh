#!/bin/bash
./clean.sh
./build_r.sh 1.23.2-rc10
# Create all cprj projects from the targets and projects in the solution
csolution convert -s out/tflite_micro_examples.csolution.yml

# Where the *.cprj files are located
search_folder="out"

# Initialize success and failure counters
success_count=0
failure_count=0

# Find all *.cprj files and call cbuild with each file
while read -r cprj_file; do
    echo "Building: $cprj_file"
    build_output=$(cbuild "$cprj_file" 2>&1)
    echo "$build_output"

    if echo "$build_output" | grep -q "info cbuild: build finished successfully!"; then
        ((success_count++))
    else
        ((failure_count++))
    fi
done < <(find "$search_folder" -type f -name "*.cprj")

# Print the build report
echo "-----------------------------------------"
echo "Build report:"
echo "Successful builds: $success_count"
echo "Failed builds: $failure_count"
