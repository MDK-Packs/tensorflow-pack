import sqlite3
import argparse
import os
import sys

#python main
def main():
#get argument from command line
    parser = argparse.ArgumentParser(
        description="Copy test sources from tensorflow repo to sources in test package.")
    # add the --results option
    parser.add_argument("--results", type=str, default=os.path.curdir,
                        help="stdio log of testrun")
    # Check if path in --results exists
    if not os.path.exists(parser.parse_args().results):
        print("File " + parser.parse_args().results + " does not exist")
        sys.exit(1)
    #connect to database
    conn = sqlite3.connect('test_results.db')
    db = conn.cursor()
    #create table
    db.execute('''CREATE TABLE IF NOT EXISTS results
                 (package text, testname text, compiler text, cvariant text, targetcpu text, testok boolean)''')
    #insert a row of data
    # print --results
    print("Working on results: " + parser.parse_args().results)
    # Read results file
    with open(parser.parse_args().results, 'r') as stream:
        results = stream.read()
    # Walk trough results file line by line
    for line in results.splitlines():
        # Check if line contains "Working on project: "
        if "Working on project: " in line:
            # Get project name
            project_file = line.split("Working on project: ")[1]
            splitstring = project_file.split("/") 
            package = splitstring[2]
            project = splitstring[4]
            print("Project: " + project_file)
            print("Package: " + package)
            # Extract string between two strings "+" and ".axf"
            cpu = project.split("+")[1]
            cpu = cpu.split(".cprj")[0]
            print("Target CPU: " + cpu)
            # Extract string between two strings "_" and "+"
            compiler = project.split("_")[1]
            compiler = compiler.split("+")[0]
            print("Compiler: " + compiler)
            # Extract string between two strings "Validation." and "_"
            cvariant = project.split("Validation.")[1]
            cvariant = cvariant.split("_")[0]
            print("Cvariant: " + cvariant)
        # Check if line contains "Testing "
        if "Testing " in line:
            test_name = line.split("Testing ")[1]
            print("Register: " + test_name)
            test_ok = "False"
            # Check if next line contains "Testing" or "passed" or "xterm"
            if "Testing" in results.splitlines()[results.splitlines().index(line)+1]:
                test_ok = "True"
            elif "xterm" in results.splitlines()[results.splitlines().index(line)+1]:
                test_ok = "True"
            elif "passed" in results.splitlines()[results.splitlines().index(line)+1]:
                test_ok = "True"
            db.execute("INSERT INTO results VALUES ('"+package+"','"+test_name+"', '"+compiler+"','"+cvariant+"', '"+cpu+"', '"+test_ok+"')")
    #save data to database
    conn.commit()
    #close connection
    conn.close()
    return 0


#python application entry point
if __name__ == "__main__":
    main()