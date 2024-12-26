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
target_filepath_list.append('/etc/passwd')

result_filedata_list = []

for target_filepath in target_filepath_list:
    filepath = path + '/file' + target_filepath
    if os.path.isfile(filepath):
        with open(filepath) as file_object:
            lines = file_object.readlines()
            for line in lines:
                filedata_table = {}
                params = line.split(':', 6)
                if len(params) == 7:
                    filedata_table['action'] = 'present'
                    filedata_table['user_name'] = params[0]
                    filedata_table['user_id'] = params[2]
                    filedata_table['group_id'] = params[3]
                    filedata_table['comment'] = params[4]
                    filedata_table['home_dir'] = params[5]
                    filedata_table['login_shell'] = params[6].rstrip()
                    filedata_table['password'] = ''
                    filedata_table['password_apply'] = False
                    if params[1] == 'x' or params[1] == '*' or params[1] == '':
                        filedata_table['password_info'] = params[1]
                    result_filedata_list.append(filedata_table) 

result = {}
target_parameter_root_key = 'VAR_RH_user'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))
