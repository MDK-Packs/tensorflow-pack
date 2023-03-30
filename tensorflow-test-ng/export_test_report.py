import sqlite3
import argparse
import os 

def main():
    test_error = 0
    # create the argument parser
    parser = argparse.ArgumentParser(
        description="Export various test report files from test results SQLite database.")
    parser.add_argument("--out_path", type=str, default=os.path.curdir,
                        help="path, output path for reports")                    
    parser.add_argument("--report", type=str, default="test_results.db",
                        help="yml file with a list of tests and sources for complex tests")

    # Check if path in --out_path exists
    if not os.path.exists(parser.parse_args().out_path):
        print("Path " + parser.parse_args().out_path + " does not exist")
        sys.exit(1)
    
    # Check if report file exists
    if not os.path.exists(parser.parse_args().report):
        print("File " + parser.parse_args().report + " does not exist")
        sys.exit(1)

    # Read report file as SQLite database
    conn = sqlite3.connect(parser.parse_args().report)
    c = conn.cursor()
    c.execute("SELECT * FROM results WHERE testname = 'ALL_TESTS'")
    test_results = c.fetchall()
    conn.close()
    print(test_results)



if __name__ == '__main__':
    main()
