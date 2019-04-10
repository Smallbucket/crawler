# -*- coding: UTF-8 -*-

import db_config
import platform

platform_os = platform.system()
config = db_config
if(platform_os == 'Linux'):
    config = db_config

data_root_path = config.data_root_path


# Load old data
def read(resources_file_path, encode='utf-8'):
    file_path = data_root_path + resources_file_path
    outputs = []
    for line in open(file_path, encoding=encode):
        if not line.startswith("//"):
            outputs.append(line.strip('\n').split(',')[-1])
    return outputs

# append new data to file from scratch
def append(resources_file_path, data, encode='utf-8'):
    file_path = data_root_path + resources_file_path
    with open(file_path, 'a', encoding=encode) as f:
        f.write(data)
    f.close

