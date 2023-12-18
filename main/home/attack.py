import os
from shutil import copy2
from PIL import Image

def copyimages(input_dir, output_dir='testfolder'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            ################
            #adversarial attack here
            
            #test to copy files
            copy2(os.path.join(input_dir, filename), os.path.join(output_dir, filename))

copyimages('pet_images/')