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
target_filepath_list.append('/etc/group')

result_filedata_list = []

for target_filepath in target_filepath_list:
    filepath = path + '/file' + target_filepath
    if os.path.isfile(filepath):
        with open(filepath) as file_object:
            lines = file_object.readlines()
            for line in lines:
                filedata_table = {}
                params = line.split(':', 4)
                if len(params) == 4:
                    filedata_table['action'] = 'present'
                    filedata_table['group_name'] = params[0]
                    filedata_table['group_id'] = params[2]
                    filedata_table['user_name'] = params[3].rstrip()
                    result_filedata_list.append(filedata_table) 

result = {}
target_parameter_root_key = 'VAR_RH_group'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))
