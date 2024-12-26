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

result_filedata_table = {}

for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath):
        result_filedata_table['command'] = '/usr/bin/systemctl get-default'
        with open(filepath) as file_object:
            lines = file_object.readlines()
            for line in lines:
                result_filedata_table['default_mode'] = line.rstrip()

result = {}
target_parameter_root_key = 'VAR_RH_default_target'
result[target_parameter_root_key] = result_filedata_table
print(json.dumps(result))
