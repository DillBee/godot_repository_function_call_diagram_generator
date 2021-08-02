
# imported files and packages
import constant
from os import path, walk


# functions first, main body after
#####
# this function scans a passed folder and all sub-folders for every file,
# before identifying whether a file is valid or invalid for inclusion in the returned dictionary
# returned dictionary includes the file path (as a string) and name of the file without its file extension
# this function is intended for use with the 'get_file_contents' function below but is functionally standalone
def get_valid_files(given_path, valid_extension=".gd"):
    # find everything in the given path
    full_file_list = {}
    for (directory_path, directory_names, file_names) in walk(given_path):

        # TODO >> extend this to take a passed value (extension)
        # (and split the files based on the extension, for handling non-gd files)

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


#####
# this function reads multiple files and yields their contents alongside an identifier for the file
# the given identifier
# this function can read a list of file paths, or a dict whose keys are file paths
# it is intended for use with the above 'get_valid_files' function,
# but will yield correctly given a similarly prepared input
# an optional parameter for printing file information to console is included
def get_file_contents(gd_file_list, print_instruction=False):
    # now we've separated the .gd files, open the relevant files to get contents
    for gdscript_path in gd_file_list:

        # entire contents of .gd file, split into a list by line
        with open(gdscript_path) as gdscript:
            gdscript_contents = [gd_file_list[gdscript_path]]
            gdscript_contents.extend(gdscript.readlines())

            # returns a generator of every file content
            # use this with a different function
            yield gdscript_contents

            # if passed print_instruction, print information on the current item
            if print_instruction:
                print("file name:", gd_file_list[gdscript_path])
                print("absolute path:", gdscript_path)
                print(gdscript_contents, "\n")


#####
# pass this function a body of gdscript formatted code (as a list)
# it is intended for use alongside the above 'get_file_contents' function
# without additional parameters this function will simply return the length of a list
# an optional parameter for ignoring 'null' (empty or commented) lines is included
def get_code_length(code_to_parse, remove_null_lines=False):
    # a 'null' line is a commented out (begins with '#') or empty line
    if remove_null_lines:
        for list_item_line in code_to_parse:
            if list_item_line == "\n" or list_item_line[0] == "#":
                code_to_parse.remove(list_item_line)
    # +1 for empty line at end of file not counted
    # -1 for identifier line added by get_file_contents function
    # therefore len() is correct to Godot's own IDE measurement,
    # but subtract 1 if only interested in actual lines
    return len(code_to_parse)


#######################################################################################################################

# main body
# variables for code line counting
total_lines_of_code_with_empty_lines = 0
total_lines_of_code_without_null_lines = 0
# variables for godot repository folder paths
# debug value so don't have to keep typing in whilst testing
# raw string to prevent escape sequence errors
debug_repo_path = r"C:\Users\newwb\Documents\Godot\project folders\testproj_dodgecreeps"
# else use default blank value and input
repo_path = ""

# validation for user
# make sure they can exit the program if they wish
# validate a passed folder path, make sure it is valid before continuing
# make this its own function to clean up main?
while not path.exists(repo_path):
    print("To get a code line count, enter your godot folder path.")
    print("Alternatively, type 'q', 'quit', or 'exit', to stop the program.")
    repo_path = input("Please enter an input now: ")
    if repo_path.lower() in ["q", "quit", "exit"]:
        print("Exiting!")
        break
    print("Given file path is not valid!\n")

# if repository path exists can begin running program functions on it
if path.exists(repo_path):
    print("\nFile Path:", repo_path)
    # yield/generator of the contents of every .gd file inside the folder and its sub-folders
    for code_body in get_file_contents(get_valid_files(repo_path), False):
        # if count total lines of code is enabled, must collect value of total lines
        if constant.COUNT_CODE_LINES:
            total_lines_of_code_with_empty_lines += get_code_length(code_body, False)
            total_lines_of_code_without_null_lines += get_code_length(code_body, True)

        # TODO >> (deco?) extension for get_valid_files to collect all file names
        # TODO >> introduce function for identifying 'func' lines inside gdscripts
        # TODO >> identify all function calls within every file
        # TODO >> list all function calls inside a file as a separate list

    # if count total lines of code is enabled, must print an output of the count
    if constant.COUNT_CODE_LINES:
        print("Total Lines of Code in Godot Repo (inc. all lines): "
              + str(total_lines_of_code_with_empty_lines))
        print("Total Lines of Code in Godot Repo (exc. empty or commented out lines): "
              + str(total_lines_of_code_without_null_lines))