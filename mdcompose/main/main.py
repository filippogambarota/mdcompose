import yaml
import os
import re

def init_config_file():
    skeleton_config = {
        "@todo": "",
        "@notes": ""
    }
    with open('.mdcompose', 'w') as outfile:
        yaml.dump(skeleton_config, outfile, default_flow_style=False, sort_keys=False)
        
# NOTE have a look here for the istances from dictionary https://stackoverflow.com/questions/1639174/creating-class-instance-properties-from-a-dictionary

def get_config_info(config_file):
    config_info = config_file["config"]
    return config_info

def read_config_file():
    with open('.mdcompose', 'r') as f:
        config_file = yaml.load(f, Loader=yaml.FullLoader) # also, yaml.SafeLoader
    return config_file

# return the pattern from the file lines
def get_pattern(txt):
    pattern = re.search("(?<=<!-- )(.*)(?=-->)", txt)
    if pattern is not None:
        pattern = pattern[0].replace(" ", "")
    return pattern

# return a dictionary wit key as befor but the actual file lines
def get_tagged_files(files_dict):
    return {key:read_lines(value) for key, value in from_file.items()}

def get_start_end_index(file):
    actual_dict_index = [i for i, x in enumerate(file) if get_pattern(x) is not None]
    start = actual_dict_index[::2]
    end = actual_dict_index[1::2]
    return start, end

def get_index_to_remove(start, end):
    to_remove = [list(range(start + 1, end)) for start, end in zip(start, end)] # get index to remove
    return flat_list(to_remove) # flattening the list

def remove_index_from_file(file, idx):
    return [x for i, x in enumerate(file) if i not in idx]