
import sys
import datetime
import re

operation = sys.argv[1]
file_path = sys.argv[2]

now = datetime.datetime.now()
date = now.strftime("%m-%d-%Y %H:%M:%S")

def sortByColumn(A,*args):
    import operator
    A.sort(key=operator.itemgetter(*args))
    return A

def build_inc():
	print "going through " + file_path
	build_file = None

	with open(file_path, 'r') as f:
		build_file = f.read()

	build_file = build_file.split('\n')

	loc_includes = {}
	loc_includes_lines = []
	ext_includes = {}
	ext_includes_lines = []

	matches = {
		'prototype': r'.* .*\(.*\);',
		'contructor': r'^[a-zA-Z0-9~]*\(.*\);'
	}

	for i, line in enumerate(build_file):
		if "#include <" in line:
			ext_includes[line] = i
			ext_includes_lines.append(i)
		if "#include \"" in line:
			loc_includes[line] = i
			loc_includes_lines.append(i)
		if "@version" in line:
			temp_line = build_file[i].split(' ')
			version = temp_line[1].split('.')
			version[2] = str(int(version[2]) + 1)
			version = '.'.join(version)
			temp_line[1] = version
			build_file[i] = ' '.join(temp_line)
		
		if "@updated" in line:
			build_file[i] = "\t@updated " + date

	loc_includes = loc_includes.keys()
	ext_includes = ext_includes.keys()

	loc_includes.sort()
	loc_includes_lines.sort()
	ext_includes.sort()
	ext_includes_lines.sort()

	countA = 0
	for i, include in enumerate(loc_includes):
		build_file[loc_includes_lines[i]] = include
		countA = i

	countB = 0
	for i, include in enumerate(ext_includes):
		build_file[ext_includes_lines[i]] = include
		countB = i

	for i in loc_includes_lines[countA + 1:]:
		build_file[i] = "// REMOVE THIS LINE"

	for i in ext_includes_lines[countB + 1:]:
		build_file[i] = "// REMOVE THIS LINE"

	while "// REMOVE THIS LINE" in build_file:
		build_file.remove("// REMOVE THIS LINE")

	# reg_build_file = list(build_file)
	# for i, item in enumerate(reg_build_file): reg_build_file[i] = item.strip()

	# func_stack = []
	# func_line_nums = []
	# func_temp_line_nums = []

	# doc_stack = []
	# doc_line_nums = []
	# doc_temp_line_nums = []

	# for i, line in enumerate(reg_build_file):
	# 	func_should_append_line = False
	# 	doc_should_append_line = False

	# 	for char in line:
	# 		if "{" in char:
	# 			if len(func_stack) == 0:
	# 				func_should_append_line = True
	# 				func_stack.append("{")
	# 		elif "}" in char:
	# 			func_stack.pop()
	# 			if len(func_stack) == 0:
	# 				doc_temp_line_nums.append(i + 1)
	# 				doc_should_append_line = False
	# 				func_line_nums.append(func_temp_line_nums)
	# 				func_temp_line_nums = []
	# 		elif len(func_stack) > 0:
	# 			func_should_append_line = True

	# 		if "/**" in char:
	# 			if len(doc_stack) == 0:
	# 				doc_should_append_line = True
	# 				doc_stack.append("*")
	# 		elif "*/" in char:
	# 			doc_stack.pop()
	# 			if len(doc_stack) == 0:
	# 				doc_should_append_line = True
	# 				doc_line_nums.append(doc_temp_line_nums)
	# 				doc_temp_line_nums = []
	# 		elif len(doc_stack) > 0:
	# 			doc_should_append_line = True
		
	# 	if func_should_append_line:
	# 		func_temp_line_nums.append(i + 1)

	# 	if doc_temp_line_nums:
	# 		doc_temp_line_nums.append(i + 1)


	# print func_line_nums
	# print doc_line_nums

	# reg_build_file = '\n'.join(reg_build_file)

	# for name, match in matches.items():
	# 	search = re.findall(match, reg_build_file, re.I | re.M)
	# 	if search:
	# 		print name + ": ", search

	with open(file_path, 'w') as f:
		f.write('\n'.join(build_file))

def add_class():
	build_file = None

	class_name = sys.argv[3]
	namespace = sys.argv[4]

	with open(file_path, 'r') as f:
		build_file = f.read()

	build_file = build_file.replace(
		">\n\n", ">\n\n#include \"" + namespace + "/include/" + class_name + ".h\"\n", 1
	)

	with open(file_path, 'w') as f:
		f.write(build_file)

if operation == "build_inc":
	build_inc()
if operation == "add_class":
	add_class()
