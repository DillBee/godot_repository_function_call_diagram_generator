# from os import listdir
# from os.path import isfile, join
#
# my_path = input()
#
# #debug_path = "C:\Users\newwb\Documents\Godot\project folders\1gamJam_june21_projectptp"
#
# only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
#
# print(only_files)

from os import walk

my_path = r"C:\Users\newwb\Documents\Godot\project folders\1gamJam_june21_projectptp"

gd_file_list = {}
for (dirpath, dirnames, filenames) in walk(my_path):

    for file in filenames:
        file_name = file[:-3]
        file_extension = file[-3:]
        if file_extension == ".gd":
            # escape the backslash or it is treated as an escape sequence (causing EOF error)
            file_path = dirpath + "\\" + file
            gd_file_list[file_path] = file_name
            # gd_file_list.append(file_path)

for gdscript_path in gd_file_list:
    print("file name: ", gd_file_list[gdscript_path])
    print("absolute path: ", gdscript_path)
    # print(item)
    with open(gdscript_path) as gdscript:
        gdscript_contents = gdscript.readlines()
        print(gdscript_contents)
    print()