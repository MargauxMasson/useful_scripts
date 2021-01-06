import os
import glob

# Path to directory with the files that need a new extension
path_to_directory = './path_to_directory_with_files_that_need_new_extension'
current_extension = '.png'
new_extension = '.jpg'

list_files = glob.glob(path_to_directory + '/*' + current_extension)

for path_to_file in list_files:
    pre, ext = os.path.splitext(path_to_file)
    path_renamed = pre + new_extension
    os.rename(path_to_file, path_renamed)
    print("File {} renamed {}".format(path_to_file, path_renamed))
