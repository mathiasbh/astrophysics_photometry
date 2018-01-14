
# Load image (fits, jpeg, png)
# If you prefer to load image yourself you avoid these functions.
# Required output is a matrix of the image.

# BUGFIXES:
# 1) Generalize loading
# 2) Let user circumvent these functions and load file themselves.

import os
from astropy.io import fits
from PIL import Image
import numpy as np

def checkformat(filepath):
    """
        Placeholder
    """

    # Allowed format (currently implemented)
    formatlist = ('.fits', '.jpeg', '.jpg', '.png')
    filename, file_extension = os.path.splitext(filepath)

    if file_extension not in formatlist:
        raise NotImplementedError('File extention: ' + str(file_extension) + ' currently not implemented.')

    return file_extension

def loadfits(filepath):
    """
        Placeholder
    """

    fitsfile = fits.open(filepath)
    dataMatrix = fitsfile[0].data
    fitsfile.close()

    return dataMatrix

def loadpng(filepath):
    """
        Placeholder
    """

    image = Image.open(filepath, 'r')
    width, height = image.size
    pixel_values = list(image.getdata())

    # image.mode -> number of channels rgb, opacity
    dataMatrix = []
    for i in range(len(pixel_values)):
        dataMatrix.append(pixel_values[i][0])

    dataMatrix = np.array(dataMatrix).reshape((height, width))
    return dataMatrix

def loadimage(filepath):
    """
    Wrapper for loading images
    """

    fileext = checkformat(filepath)

    if fileext == '.fits':
        dataMatrix = loadfits(filepath)
    elif fileext == '.jpeg':
        dataMatrix = 1
    elif fileext == '.jpg':
        dataMatrix = 1
    elif fileext == '.png':
        dataMatrix = loadpng(filepath)
    else:
        dataMatrix = 1
    return dataMatrix
