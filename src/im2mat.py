import numpy as np


def unpackMatrix(dataMatrix):
    """
        Placeholder
    """

    h, w = dataMatrix.shape
    X, Y = np.meshgrid(range(w), range(h))
    X = X.ravel()
    Y = Y.ravel()
    Z = dataMatrix.ravel()
    return X, Y, Z
