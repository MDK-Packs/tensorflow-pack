import sys

in_filename = sys.argv[1]

txt_file = open(in_filename, "r")
file_content = txt_file.read()
content_list = file_content.split(" ")
txt_file.close()

no_dupes_list = list(dict.fromkeys(content_list))

for filename in no_dupes_list:
   if not "downloads" in filename and not "LICENSE" in filename:
      print(filename)
