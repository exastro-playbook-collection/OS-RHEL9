import re
import json
import sys
import os

result_filedata_table = {}

args = sys.argv
if (len(args) < 2):
    sys.exit(1)

path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]

target_filepath_list = []
target_filepath_list.append('/etc/sysctl.conf')
result_filedata_list = []

for target_filepath in target_filepath_list:
    filepath = path + '/file' + target_filepath
    if os.path.isfile(filepath):
        with open(filepath) as file_object:
            filedata_table = {}
            lines = file_object.readlines()
            for line in lines:
                if line[0]=="#":
                    continue
                params = line.split('=', 1)
                if len(params) == 2:
                    filedata_table[params[0].strip()] = params[1].strip()
            result_filedata_table['path'] = target_filepath
            result_filedata_table['properties'] = filedata_table
            result_filedata_table['file'] = ''
            result_filedata_list.append(result_filedata_table)

result = {}
target_parameter_root_key = 'VAR_RH_sysctl'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

