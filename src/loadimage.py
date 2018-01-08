
# Load image
# USAGE:
#

import os
import pyfits

def checkformat(filenamepath):
    # Allowed format (currently implemented)

    formatlist = ('.fits', '.jpeg', '.jpg', '.png')

    # Determine file format
    filename, file_extension = os.path.splitext(filenamepath)

    # Is file format allowed?
    if file_extension not in formatlist:
        raise NotImplementedError('File extention: ' + str(file_extension) + ' currently not implemented.')

    return


def loadimage(filenamepath):
    # Check if file format Allowed
    checkformat(filenamepath)
