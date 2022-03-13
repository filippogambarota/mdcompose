import re

def get_pattern(txt):
    pattern = re.search("(?<=<!-- )(.*)(?=-->)", txt)
    if pattern is not None:
        pattern = pattern[0].replace(" ", "")
    return pattern

def read_lines(file):
    with open(file) as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def md_comment(txt):
    comment = "<!-- {} -->".format(txt)
    return comment

def flat_list(list):
    return [i for list in list for i in list]

from_file = {
    '@todo': "todo.md",
    '@note': "note.md"
}

actual_dict = {key:read_lines(value) for key, value in from_file.items()}

readme = read_lines("readme.md")

actual_dict_index = [i for i, x in enumerate(readme) if get_pattern(x) is not None]
start = actual_dict_index[::2]
end = actual_dict_index[1::2]
to_remove = [list(range(start + 1, end)) for start, end in zip(start, end)] # get index to remove
to_remove = flat_list(to_remove) # flattening the list

readme = [x for i, x in enumerate(readme) if i not in to_remove]

for i, line in enumerate(readme):
    pattern_line = get_pattern(line)
    if pattern_line in actual_dict.keys():
        readme[i] = [md_comment(pattern_line)] + actual_dict[pattern_line]

with open("readme.md", "w") as f:
    for i, line in enumerate(readme):
        if type(line) == list:
            f.write(flat_list(line)[0])
        else:
            f.write(line)
        f.write("\n")