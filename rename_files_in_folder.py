import os
import glob
from tqdm import tqdm

path_folder = "/Users/margauxmforstyhe/Desktop/workspace/Pytorch-UNet-master/data/imgs"
file_extension = ".png"
string_to_delete_in_name_files = ["[", "]", " ", ",", "."]

paths_files = glob.glob(path_folder + "/*{}".format(file_extension))

files_to_rename = []
for path in paths_files:
    print(path)
    new_name = path[:].split(file_extension)[0]
    for string in string_to_delete_in_name_files:
        if string in path:
            # new_name = path.split(string_to_delete_in_name_files)[0] + path.split(string_to_delete_in_name_files)[1]
            new_name = new_name.replace(string, "")
    new_name = new_name + file_extension
    print(new_name)
    os.rename(path, new_name)
    files_to_rename.append(path)

print("{} files were renamed".format(len(files_to_rename)))
print("Done!")
