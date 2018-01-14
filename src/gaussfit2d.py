import numpy as np

def unpackMatrix(dataMatrix):

    return data_tuple

def gauss_2d(dataMatrix, amplitude, xo, yo, sigmax, sigmay, theta, offset):
    """
        Placeholder
    """

    (X, Y) = unpackMatrix(dataMatrix)

    cos2 = np.cos(theta)**2
    sin2 = np.sin(theta)**2
    sin_arg2 = np.sin(2*theta)

    a = cos2/(2*sigmax**2) + sin2/(2*sigma_y**2)
    b = -sin_arg2/(4*sigmax**2) + sin_arg2/(4*sigmay**2)
    c = sin2/(2*sigmax**2) + cos2/(2*sigmay**2)

    f = amplitude*np.exp(-(a*(X-x0)**2 + 2*b*(X-x0)**(Y-y0) + c*(Y-y0)**2))

    return f.ravel()
