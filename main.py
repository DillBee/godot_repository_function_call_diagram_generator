from os import listdir
from os.path import isfile, join

my_path = input()

only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]

