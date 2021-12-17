import os, sys
from junit_xml import TestSuite, TestCase

def main():
    for filename in os.listdir(in_path):
      if filename.endswith(".stdio"):
        filename =  in_path + filename 
        print(">>> Parsing file: " , filename)
        test_fn_name = os.path.basename(filename)
        test_report_fn = filename + ".junit"
        junit_file = open(test_report_fn, "w")
        print(">>>TEST Writing report to ", junit_file)
        junit_cases = []        
        with open(filename) as f:
          lines = f.readlines()
          for line in lines:
            if "Testing" in line:
              line = line.split(' ')
              line = [i.strip() for i in line]
              print(line[1])
              tc = TestCase(classname=test_fn_name, name=line[1], elapsed_sec=0, stderr="", stdout="")
              junit_cases.append(tc)
            if "~~~" in line:
              if "PASSED" in line:
                print(">>> Tests Passed")
              if "FAILED" in line:
                print(">>> Tests Failed")
        junit_report = TestSuite("Tensorflow Tests", junit_cases, package=test_fn_name, properties={"ARMCLANG": "Reference"}) 
        TestSuite.to_file(junit_file, [junit_report], prettyprint=False)
        junit_file.close()
        continue
      else:
        continue

in_path = sys.argv[1]

if __name__ == '__main__':
    main()

