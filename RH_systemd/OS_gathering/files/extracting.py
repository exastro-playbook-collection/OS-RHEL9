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
path_len = len(path)

target_filepath_list = []
target_filepath_list.append('/etc/systemd/system.conf')
target_filepath_list.append('/etc/systemd/user.conf')

result_filedata_list = []

for target_filepath in target_filepath_list:
    filepath = path + '/file' + target_filepath
    if os.path.isfile(filepath):
        result_filedata_table = {}
        with open(filepath) as file_object:
            section_table = []
            section_dataset_table = {}
            section_data_table = {}
            lines = file_object.readlines()
            section_name = ''
            for line in lines:
                if line[0]=="#":
                    continue
                # section serach
                search_result = re.search('^\\s*\\[(.+)\\]\\s*$', line)
                if search_result:
                    if section_name !='':
                        section_dataset_table['section'] = section_name
                        section_dataset_table['properties'] = section_data_table
                        section_table.append(section_dataset_table)
                        section_dataset_table = {}
                        section_data_table = {}
                    section_name = search_result.group(1)
                else:
                    params = line.split('=', 1)
                    if len(params) == 2:
                        section_data_table[params[0].strip()] = params[1].strip()
            # last section exist setteing
            if section_name !='' and len(section_data_table) > 0:
                section_dataset_table['section'] = section_name
                section_dataset_table['properties'] = section_data_table
                section_table.append(section_dataset_table)
            result_filedata_table['path'] = target_filepath
            result_filedata_table['value'] = section_table
            result_filedata_table['file'] = ''
            result_filedata_list.append(result_filedata_table)

target_filepath = path + '/file/etc/systemd/system'
for dir_path, dir_names, file_names in os.walk(target_filepath):
    for file_name in file_names:
        if (".service" in file_name or ".socket" in file_name):
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
target_parameter_root_key = 'VAR_RH_systemd'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))
