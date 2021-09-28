# USING CNN
from imagededup.methods import CNN
from imagededup.utils import plot_duplicates

from pathlib import Path, PurePath
from typing import Dict, List, Optional, Union

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
plt.rcParams['figure.figsize'] = (15, 10)


def image_dir(image_dir):
    return image_dir

def name_image(filename):
    return filename

def encodings_and_duplicates_images_dir(image_dir) -> Dict:
    encodings = CNN().encode_images(image_dir= image_dir)
    duplicates = CNN().find_duplicates(encoding_map=encodings, scores=True)
    return duplicates

def find_name_duplicated_image(duplicates, filename):
    score_arr = []
    image_detect_arr = []

    # Name of Image had max score
    for key, value in duplicates.items():
        if key == filename:
            for i in value:
                score_arr.append(i[1])
                image_detect_arr.append(i[0])
            index_max_score = score_arr.index(max(score_arr))

    return (image_detect_arr[index_max_score]) #Image has max score: ảnh có xác suất giống lớn nhất

def find_position_duplicated_image(duplicates, filename):
    score_arr = []
    image_detect_arr = []

    # Name of Image had max score
    for key, value in duplicates.items():
        if key == filename:
            for i in value:
                score_arr.append(i[1])
                image_detect_arr.append(i[0])
            index_max_score = score_arr.index(max(score_arr))
            #print(image_detect_arr[index_max_score]) #Image has max score: ảnh có xác suất giống lớn nhất

    # Extract position
    split_position = image_detect_arr[index_max_score].split('-').pop()
    position = split_position[:split_position.index('.jpg')]
    return (int(position))

    # Display original image and image had max score
def display_images_to_compare(filename, duplicated_filename, image_dir):
    original_img = mpimg.imread(image_dir+'/'+filename)
    original_img_plot = plt.imshow(original_img)
    plt.title('Original image' + ':' + filename)
    plt.show()

    img_had_max_score = mpimg.imread(image_dir+'/'+ duplicated_filename)
    imgplot = plt.imshow(img_had_max_score)
    plt.title('Image had max score' + ':' + duplicated_filename)
    plt.show()

    
