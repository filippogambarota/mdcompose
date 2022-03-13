"""
UTILS functions for printing messages
"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def tick():
    return '\u2713'

def text_green(msg):
    out = bcolors.OKGREEN + msg + bcolors.ENDC
    return out

def text_blue(msg):
    out = bcolors.OKBLUE + msg + bcolors.ENDC
    return out

# Readlines and remove newline chr
def read_lines(file):
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

# put txt into md comment

def md_comment(txt):
    comment = "<!-- {} -->".format(txt)
    return comment

# flatten a list

def flat_list(list):
    return [i for list in list for i in list]