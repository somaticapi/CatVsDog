from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from scipy.misc import imread, imresize
from os import  walk
from os.path import join


def read_images(path, classes, img_height = 128, img_width = 128, img_channels = 3):

    num_classes = len(classes)
    filenames = next(walk(path))[2]
    num_files = len(filenames)

    images = np.zeros((num_files, img_height, img_width, img_channels), dtype=np.uint8)
    labels = np.zeros((num_files, num_classes), dtype=np.uint8)
    for i, filename in enumerate(filenames):
        img = imread(join(path, filename))
        img = imresize(img, (img_height, img_width))
        images[i, :, :, :] = img

        for j, img_class in enumerate(classes):
            labels[i, j] = img_class in filename

    return images, labels
