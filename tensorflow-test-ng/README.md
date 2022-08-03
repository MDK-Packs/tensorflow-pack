
Next-gen test infrastructure

# Requirements:


for test_r.sh:
- Linux 
- python3 
- 

for exec_suite.sh:
- AVH (or compatible) 1.3.0+
- CMSIS Toolbox v?


# Assets
**test_r.sh**: Entry point for test suite preparation after pack release process. Will be called as 

Example invokation:

``` ./tensorflow-pack/tensorflow-test-ng/test_r.sh ``` 


**copy_sources.py**: *Called from test_r.sh.* Collects sources required for test suite and copys them from tflite-micro repo to specified folder.
Parameters:
- --tflm_path: Path to tflite-micro repository
- --inventory: Test inventory yml file that lists sources of a test
- --out_path: Path to copy sources to.

Example invokation:

```python3 ./tensorflow-pack/tensorflow-test-ng/copy_sources.py --tflm_path=./tensorflow-pack/tensorflow-build/rel/mlplatform/core_software/tflite_micro --inventory=./tensorflow-pack/tensorflow-test-ng/test_tests.yml --out_path=./tensorflow-pack/tensorflow-test-ng/Source```
 

**create_tests.py**: *Called from test_r.sh.* Compiles the csolution yml files - one for each test provided in an inventory yml.
Parameters:
- --inventory: Test inventory yml file that lists sources of a test
- --out_path: Root folder to create csolution projects in. Subfolders will be named according to tests in inventory.

Example invokation: 

```python3 ./tensorflow-pack/tensorflow-test-ng/create_tests.py --inventory=./tensorflow-pack/tensorflow-test-ng/$inventory --out_path=./tensorflow-pack/tensorflow-test-ng/gen ``` 


**exec_suite.sh**: Called after test_r.sh to create and execute tests and register test results.

Example invokation: 

```./exec_suite.sh```

**avh_exec_test.py**: *Called from exec_suite.sh.* Read a CPRJ project file, find the executable and determine the VHT model by the device in the project. Execute on VHT.

Example invokation: 

``` python3 avh_exec_test.py --project=./gen/test_helpers_test/project.cprj 	```

**record_test_results.py**: *Called from exec_suite.sh.* Read the console log of a test execution. Find tests and results. Register into an SQL database (SQLite)

Example invokation:

``` python3 record_test_results.py --results=./gen/test_helpers_test/test_result.log 	```

