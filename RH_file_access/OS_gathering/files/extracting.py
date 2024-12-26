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

def mode_setting(modestr):
    ownerset = modestr[1:4].replace('-','')
    groupset = modestr[4:7].replace('-','')
    etcset = modestr[7:10].replace('-','')
    mode_set = 'u=' + ownerset + ',g=' + groupset + ',o=' + etcset
    return mode_set

count = 0
while True:
    # Decectory exist check
    dirpath = path + '/command/' + str(count)
    if os.path.isdir(dirpath):
        count +=1
    else:
        break

    filepath = dirpath + '/stdout.txt'
    set_path = ''
    if os.path.isfile(filepath):
         with open(filepath) as file_object:
            lines = file_object.readlines()
            for line in lines:
                filedata_table = {}
                params = line.split()
                if len(params) > 1:
                    check_str = params[0]
                    # total or 合計 skip
                    if check_str == 'total' or check_str == '合計': 
                        continue
                    # file link other skip
                    if check_str[0] != '-' and check_str[0] != 'l':
                        continue

                    # state setting
                    filedata_table['action'] = 'file'
                    # mode setting
                    mode_set = mode_setting(check_str)
                    filedata_table['mode'] = mode_set
                    # owner,group setting
                    filedata_table['owner'] = params[2]
                    filedata_table['group'] = params[3]
                    if check_str[0] == 'l':
                        # file path setting
                        filedata_table['file_path'] = params[9]
                        # symbolic_link setting
                        if set_path != '':
                            filedata_table['symbolic_link'] = set_path + '/' + params[7]
                        else:
                            filedata_table['symbolic_link'] = params[7]
                        # state setting
                        filedata_table['action'] = 'link'
                    else:
                        # file path setting
                        if set_path != '':
                            filedata_table['file_path'] = set_path + '/' + params[7]
                        else:
                            filedata_table['file_path'] = params[7]
                    result_filedata_list.append(filedata_table)
                elif len(params) == 1:
                    set_path = params[0].rstrip(':')

result = {}
target_parameter_root_key = 'VAR_RH_file_access'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))
