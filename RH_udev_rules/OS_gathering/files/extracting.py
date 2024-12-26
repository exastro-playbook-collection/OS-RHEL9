import re
import json
import sys
import os

result_filedata_list = []

args = sys.argv
if (len(args) < 2):
    sys.exit(1)

path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]
path_len = len(path)

target_filepath = path + '/file/etc/udev/rules.d'
for dir_path, dir_names, file_names in os.walk(target_filepath):
    for file_name in file_names:
        filepath = os.path.join(dir_path, file_name)
        if os.path.isfile(filepath):
            with open(filepath) as file_object:
                result_filedata_table = {}
                result_filedata_text = []
                lines = file_object.readlines()
                for line in lines:
                    result_filedata_text.append(line.replace('\n',''))
                filepath_len = len(filepath)
                result_filedata_table['path'] = filepath[path_len+5:filepath_len]
                result_filedata_table['text'] = result_filedata_text
                result_filedata_table['file'] = ''
                result_filedata_list.append(result_filedata_table)

result = {}
target_parameter_root_key = 'VAR_RH_udev_rules'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

