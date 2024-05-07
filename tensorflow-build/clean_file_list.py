import sys

in_filename = sys.argv[1]

txt_file = open(in_filename, "r")
file_content = txt_file.read()
content_list = file_content.split(" ")
txt_file.close()

no_dupes_list = list(dict.fromkeys(content_list))
signal_files_list = []

for filename in no_dupes_list:
   if filename.startswith("signal/"):
      signal_files_list.append(filename)
      no_dupes_list.remove(filename)
   elif not "downloads" in filename and not "LICENSE" in filename:
      print(filename)


signal_filename = in_filename.replace("srcs.", "signal.").replace(".raw", ".lst")
with open(signal_filename, 'w') as f:
   for item in signal_files_list:
      f.write("%s\n" % item)

