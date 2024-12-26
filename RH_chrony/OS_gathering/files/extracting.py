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

result_filedata_list = []

target_filepath_list = []
target_filepath_list.append('/etc/chrony.conf')
target_filepath_list.append('/etc/chrony.keys')

for target_filepath in target_filepath_list:
    filepath = path + '/file' + target_filepath
    if os.path.isfile(filepath):
        with open(filepath) as file_object:
            result_filedata_table = {}
            result_filedata_text = []
            lines = file_object.readlines()
            for line in lines:
                result_filedata_text.append(line.replace('\n',''))
            result_filedata_table['path'] = target_filepath
            result_filedata_table['text'] = result_filedata_text
            result_filedata_table['file'] = ''
            result_filedata_list.append(result_filedata_table)

result = {}
target_parameter_root_key = 'VAR_RH_chrony'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

