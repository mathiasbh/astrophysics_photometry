import numpy as np
import scipy.optimize as opt
from src.im2mat import unpackMatrix


def gauss_2d(XY, ampl, x0, y0, sigmax, sigmay, z0):
    """
        Placeholder
    """

    X, Y = XY

    x0 = float(x0)
    y0 = float(y0)

    g = z0 + ampl*np.exp(-0.5*(((X-x0)/sigmax)**2 + ((Y-y0)/sigmay)**2))
    return g.ravel()


def gauss_fit(dataMatrix, initial_guess):
    """
        Placeholder
    """

    X, Y, Z = unpackMatrix(dataMatrix)

    popt, pcov = opt.curve_fit(gauss_2d, (X, Y), Z, p0=initial_guess)
    predictionfit = gauss_2d((X, Y), *popt)

    # Return fitted pixel coordinates (x, y)
    return predictionfit, np.round(popt[1]), np.round(popt[2])
