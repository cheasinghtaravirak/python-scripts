import sys #for grabbing args.
import os #for file path
from PIL import Image #for image conversion

#grab first and and second arg.
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, else create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through the image folder
for image in os.listdir(image_folder):
    # convert each image to png and save to new folder
    original_image = Image.open(f'{image_folder}{image}') #pokemon/pikachu.jpg
    #extract only filename without extension
    clean_name = os.path.splitext(image)[0] #pikachu
    png_image = original_image.save(f'{output_folder}{clean_name}.png', 'png')
    print('success')


