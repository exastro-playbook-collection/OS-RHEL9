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
target_filepath_list.append('/etc/mptcpd/mptcpd.conf')
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

result = {}
target_parameter_root_key = 'VAR_RH_mptcpd'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

