import os
import glob
from tqdm import tqdm
from PIL import Image
import numpy as np
import cv2

output_size = (600, 600)
binary_image = False
path_folder = "/Users/margauxmforstyhe/Desktop/task_flat_rooftop_batch-1-2021_05_02_15_51_00-segmentation mask 1.1/JPEGImages"
output_dir = path_folder + "/resized_600x600"
file_extension = ".png"

# Creating output directory if does not exist
if not os.path.isdir(output_dir):
    os.mkdir(output_dir)
    os.mkdir(output_dir + "/test")
    output_dir = output_dir + "/test"

print(path_folder + f"/*{file_extension}")
imgs_paths = glob.glob(path_folder + f"/*{file_extension}")
print(f"There are {len(imgs_paths)} images to be resized")
firs_image = np.array(Image.open(imgs_paths[0]))
print(f"Original shape is {firs_image.shape}")

count_images = 0

for img_path in tqdm(imgs_paths):
    print(img_path)
    name = output_dir + "/" + img_path.split("/")[-1]
    img = np.array(Image.open(img_path))
    new_img = cv2.resize(img, output_size, cv2.INTER_NEAREST)
    # if binary image (segmentation mask)
    if binary_image:
        new_img = cv2.threshold(np.array(new_img), 0, 255, cv2.THRESH_BINARY)
    # cv2.imshow(np.array(new_img))
    cv2.imwrite(name, new_img)
    count_images = count_images + 1
    print(f"{name} saved")

print(f"{count_images} files were resized and saved in {output_dir}")
print("Done!")
