
import argparse
import os
import sys
import xml.etree.ElementTree as ET

vhtdict = {
    "CMSDK_CM0plus_VHT": "VHT_MPS2_Cortex-M0plus", 
    "CMSDK_CM3_VHT" : "VHT_MPS2_Cortex-M3", 
    "CMSDK_CM4_FP_VHT" : "VHT_MPS2_Cortex-M4", 
    "CMSDK_CM7_DP_VHT" : "VHT_MPS2_Cortex-M7", 
    "CMSDK_CM7_SP_VHT" : "VHT_MPS2_Cortex-M7", 
    "IOTKit_CM23_VHT" : "VHT_MPS2_Cortex-M23", 
    "IOTKit_CM33_FP_VHT" : "VHT_MPS2_Cortex-M33", 
    "SSE-300-MPS3" : "VHT_MPS3_Corstone_SSE-300"
}
def main():
#get argument from command line
    parser = argparse.ArgumentParser(
        description="Copy test sources from tensorflow repo to sources in test package.")
    # add the --project option
    parser.add_argument("--project", type=str, default=os.path.curdir,
                        help="CPRJ with test")

    # Check if path in --project exists
    if not os.path.exists(parser.parse_args().project):
        print("Path " + parser.parse_args().project + " does not exist")
        sys.exit(1)
    # print --project
    print("Working on project: " + parser.parse_args().project)
    basepath = "./" + os.path.dirname(parser.parse_args().project)    
    # Open CPRJ file as XML file
    tree = ET.parse(parser.parse_args().project)
    root = tree.getroot()
    #retrieve output path
    output_xml = root.findall('./target/output')[0]
    executable_name = output_xml.get('name')+".axf"
    output_path = os.path.join(basepath, output_xml.get('outdir'))
    print(executable_name)
    # Check if outpath exists
    if not os.path.exists(output_path):
        print("Path " + output_path + " does not exist")
      #  sys.exit(1) 
    target_xml = root.findall('./target')[0]
    device_name = target_xml.get('Dname')
    print(device_name, "executed on ", vhtdict[device_name])
    os.system(vhtdict[device_name] + "	--timelimit -a " + output_path + "/" + executable_name)

if __name__ == '__main__':
    main()
