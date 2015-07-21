
import sys
import datetime

operation = sys.argv[1]
file_path = sys.argv[2]

now = datetime.datetime.now()
date = now.strftime("%m-%d-%Y %H:%M:%S")

def build_inc():
	build_file = None

	with open(file_path, 'r') as f:
		build_file = f.read()

	build_file = build_file.split('\n')

	for i, line in enumerate(build_file):
		if "@version" in line:
			temp_line = build_file[i].split(' ')
			version = temp_line[1].split('.')
			version[2] = str(int(version[2]) + 1)
			version = '.'.join(version)
			temp_line[1] = version
			build_file[i] = ' '.join(temp_line)
		
		if "@updated" in line:
			build_file[i] = "\t@updated " + date

	with open(file_path, 'w') as f:
		f.write('\n'.join(build_file))

def add_class():
	build_file = None

	class_name = sys.argv[3]
	namespace = sys.argv[4]

	with open(file_path, 'r') as f:
		build_file = f.read()

	build_file = build_file.replace(
		">\n\n", ">\n\n#include \"include/" + class_name + ".h\"\n", 1
	)

	with open(file_path, 'w') as f:
		f.write(build_file)

if operation == "build_inc":
	build_inc()
if operation == "add_class":
	add_class()
