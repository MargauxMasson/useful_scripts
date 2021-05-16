import os
import glob
from tqdm import tqdm

path_folder = "path_to_folder"
file_extension = "tif"
key_name_files_to_delete = "2015-01-01_2016-01-01 copy 3"

paths_files = glob.glob(path_folder + "/*.{}".format(file_extension))

files_to_delete = []
for path in paths_files:
    if key_name_files_to_delete in path:
        print(path)
        files_to_delete.append(path)
        os.remove(path)

print("{} files were deleted".format(len(files_to_delete)))
print("Done!")
