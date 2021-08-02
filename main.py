
from os import walk

# given_path = input()
given_path = r"C:\Users\newwb\Documents\Godot\project folders\1gamJam_june21_projectptp"

# find everything in the given path
gd_file_list = {}
for (directory_path, directory_names, file_names) in walk(given_path):

    for file in file_names:
        # we're only interested in files that follow this format
        file_name = file[:-3]
        file_extension = file[-3:]
        # if the extension (ending characters) isn't a three character sequence of '.gd', ignore it
        if file_extension == ".gd":
            # escape the backslash or it is treated as an escape sequence (causing EOF error)
            file_path = directory_path + "\\" + file
            gd_file_list[file_path] = file_name
            # gd_file_list.append(file_path)

# now we've separated the .gd files, open the relevant files to get contents
for gdscript_path in gd_file_list:
    print("file name: ", gd_file_list[gdscript_path])
    print("absolute path: ", gdscript_path)
    # print(item)
    with open(gdscript_path) as gdscript:
        gdscript_contents = gdscript.readlines()
        # entire contents of .gd file, split into a list by line
        print(gdscript_contents)
    # linebreak
    print()
