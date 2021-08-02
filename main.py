
import constant
from os import walk

# in live version should be a given input
# should also handle incorrect input & loop until valid (with escape command)
# gui?

# given_path = input()

# raw string to prevent escape sequence errors
given_path = r"C:\Users\newwb\Documents\Godot\project folders\1gamJam_june21_projectptp"


def get_valid_files(valid_extension=".gd"):
    # find everything in the given path
    full_file_list = {}
    for (directory_path, directory_names, file_names) in walk(given_path):

        # extend this to take a passed value (extension)
        # and split the files based on the extension
        # for handling non-gd files

        for file in file_names:
            # we're only interested in files that follow this format
            file_name = file[:-3]
            file_extension = file[-3:]
            # current iteration of func only handles .gd as a valid extension, and defaults to it
            # if the extension (ending characters) isn't a three character sequence of '.gd', ignore it
            if file_extension == valid_extension:
                # escape the backslash or it is treated as an escape sequence (causing EOF error)
                file_path = directory_path + "\\" + file
                full_file_list[file_path] = file_name

    return full_file_list


def get_file_contents(gd_file_list, print_instruction=False):
    # now we've separated the .gd files, open the relevant files to get contents
    for gdscript_path in gd_file_list:

        # entire contents of .gd file, split into a list by line
        with open(gdscript_path) as gdscript:
            gdscript_contents = [gd_file_list[gdscript_path]]
            gdscript_contents.extend(gdscript.readlines())
            # gdscript_contents = gdscript.readlines()
            # returns a generator of every file content
            # use this with a different function
            yield gdscript_contents

            # if passed print_instruction, print information on the current item
            if print_instruction:
                print("file name:", gd_file_list[gdscript_path])
                print("absolute path:", gdscript_path)
                # print(gdscript_contents, "\n")
                print("lines of code in file:", len(gdscript_contents)+1)
                for list_item_line in gdscript_contents:
                    if list_item_line == "\n":
                        gdscript_contents.remove(list_item_line)
                print("lines of code in file w/o empty lines:", len(gdscript_contents))
                print(gdscript_contents, "\n")


# pass this function a body of .gd code (as a list)
def get_code_length(code_to_parse, remove_empty_lines=False):
    if remove_empty_lines:
        for list_item_line in code_to_parse:
            if list_item_line == "\n":
                code_to_parse.remove(list_item_line)
    # +1 for empty line at end of file not counted
    # -1 for identifier line added by get_file_contents function
    # therefore len() is correct to Godot's own IDE measurement,
    # but subtract 1 if only interested in actual lines
    return len(code_to_parse)


#######################################################################################################################

total_lines_of_code_with_empty_lines = 0
total_lines_of_code_without_empty_lines = 0

for code_body in get_file_contents(get_valid_files(), False):

    if constant.COUNT_CODE_LINES:
        total_lines_of_code_with_empty_lines += get_code_length(code_body, False)
        total_lines_of_code_without_empty_lines += get_code_length(code_body, True)

if constant.COUNT_CODE_LINES:
    print("Total Lines of Code in Godot Repo (inc. empty lines): " + str(total_lines_of_code_with_empty_lines))
    print("Total Lines of Code in Godot Repo (exc. empty lines): " + str(total_lines_of_code_without_empty_lines))