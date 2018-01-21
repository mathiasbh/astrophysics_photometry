import numpy as np
import src.constants as c

# TODO: Solve case 1 (object close to edge)

def sliceMatrix(dataMatrix, x_centroid, y_centroid):
    """
        Select square slice of image around centroid coordinates.
    """

    height, width = dataMatrix.shape

    # Coordinates are mixed up
    x_centroid, y_centroid = y_centroid, x_centroid

    # Check if input coordinateas are integer
    try:
        x_centroid = int(x_centroid)
        y_centroid = int(y_centroid)
    except ValueError:
        print("Input coordinates must be integers")
        x_centroid = int(width/2)
        y_centroid = int(height/2)

    # Case 1: object close to edges
    if ((x_centroid - c.c_Slice) < 0) or \
        ((x_centroid + c.c_Slice + 1) > width) or \
        ((y_centroid - c.c_Slice) < 0) or \
        ((y_centroid + c.c_Slice + 1) > height):
        dataSlice = 1
    else:
        # Case 2: slice specification OK
        dataSlice = dataMatrix[x_centroid - c.c_Slice:x_centroid + c.c_Slice + 1,
                               y_centroid - c.c_Slice:y_centroid + c.c_Slice + 1]

    print(dataSlice.shape)
    return dataSlice
