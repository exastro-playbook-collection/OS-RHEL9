import re
import json
import sys
import os

args = sys.argv
if (len(args) < 2):
    sys.exit(1)

path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]

target_filepath_list = []
target_filepath_list.append('/0/stdout.txt')

result_filedata_list = []

for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath):
        with open(filepath) as file_object:
            lines = file_object.readlines()
            for line in lines:
                filedata_table = {}
                params = line.split('/')
                if len(params) == 4:
                    # arch is (none) not installed
                    if params[3].rstrip() == '(none)':
                        continue
                    filedata_table['action'] = 'present'
                    filedata_table['pkg_name'] = params[0]
                    filedata_table['version'] = params[1]
                    filedata_table['release'] = params[2]
                    filedata_table['arch'] = params[3].rstrip()
                    result_filedata_list.append(filedata_table)

result = {}
target_parameter_root_key = 'VAR_RH_rpm'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))
