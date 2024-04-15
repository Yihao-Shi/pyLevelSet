import numpy as np
import math

_min = np.minimum
_max = np.maximum

def _length(a):
    return np.linalg.norm(a, axis=1)

def _normalize(a):
    return a / np.linalg.norm(a)

def _dot(a, b):
    return np.sum(a * b, axis=1)

def _vec(*arrs):
    return np.stack(arrs, axis=-1)

def _perpendicular(v):
    if v[1] == 0 and v[2] == 0:
        if v[0] == 0:
            raise ValueError('zero vector')
        else:
            return np.cross(v, [0, 1, 0])
    return np.cross(v, [1, 0, 0])

def linearize(xInd, yInd, zInd, nGPx, nGPy):
    return xInd + yInd * nGPx + zInd * nGPx * nGPy

def vectorize(i, nGPx, nGPy):
    xInd = (i % (nGPx * nGPy)) % nGPx 
    yInd = (i % (nGPx * nGPy)) // nGPx 
    zInd = i // (nGPx * nGPy)
    return xInd, yInd, zInd

def heaviside_function(epsilon, phi):
    h = 0.
    ieps = 1. / epsilon
    return np.select([phi > epsilon, np.logical_and(phi > -epsilon, phi < epsilon)], [1., 0.5 * (1 + phi * ieps + np.sin(math.pi * phi * ieps) / math.pi)], default=0.)

def Sphere2Certesian(vector):
    return vector[0] * np.array([np.sin(vector[1]) * np.cos(vector[2]), np.sin(vector[1]) * np.sin(vector[2]), np.cos(vector[1])])

def Certesian2Sphere(vector):
    vec = np.zeros(3)
    r = np.linalg.norm(vector)
    if r != 0.:
        theta = np.arccos(vector[2] / r)
        vecProj = np.array([vector[0], vector[1], 0])
        normProj = np.linalg.norm(vecProj)

        phi = 0.
        if normProj != 0.:
            cosVal = vecProj[0] / normProj
            phi = np.arccos(cosVal) if vec[1] > 0. else 2 * math.pi - np.arccos(cosVal)
        vec = np.array([r, theta, phi])
    return vec

def transformation_matrix_coordinate_system(axis1, axis2):
    '''
    Return a transformation matrix from axis1 to axis2
    axis1 [nxn]: the old coordinate system
    axis2 [nxn]: the new coordinate system
    '''
    # reference: https://ocw.mit.edu/courses/16-07-dynamics-fall-2009/dd277ec654440f4c2b5b07d6c286c3fd_MIT16_07F09_Lec26.pdf
    return np.array([[np.dot(axis1[0, :], axis2[0, :]), np.dot(axis1[0, :], axis2[1, :]), np.dot(axis1[0, :], axis2[2, :]), 0],
                        [np.dot(axis1[1, :], axis2[0, :]), np.dot(axis1[1, :], axis2[1, :]), np.dot(axis1[1, :], axis2[2, :]), 0],
                        [np.dot(axis1[2, :], axis2[0, :]), np.dot(axis1[2, :], axis2[1, :]), np.dot(axis1[2, :], axis2[2, :]), 0],
                        [0., 0., 0., 1.]])

def generate_grid(x0, y0, z0, x1, y1, z1, resolution, order="z"):
    X = np.linspace(x0, x1, resolution+1)
    Y = np.linspace(y0, y1, resolution+1)
    Z = np.linspace(z0, z1, resolution+1)
    P = cartesian_product(X, Y, Z, order=order)
    return X, Y, Z, P

def cartesian_product(*arrays, **order):
    la = len(arrays)
    order = order.get("order", "z")
    if order == "x":
        arrays = (arrays[2], arrays[1], arrays[0])
    elif order == "y":
        arrays = (arrays[0], arrays[2], arrays[1])
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[...,i] = a
    arr = arr.reshape(-1, la)
    if order == "x":
        arr[:,0], arr[:,2] = arr[:,2].copy(), arr[:,0].copy()
    elif order == "y":
        arr[:,1], arr[:,2] = arr[:,2].copy(), arr[:,1].copy()
    return arr

def biInterpolate(pt, xExtr, yExtr, knownVal):
    # Performs interpolation in a 2D space that is denoted (x,y) just for the purpose of the present function, with
    # pt the point where we want to know the value through interpolation
    # knownVal, known values at (x0,y0), (x1,y0), (x0,y1), (x1,y1) with eg knownVal[0][1] = value at (x0,y1)
    # xExtr = (x0,x1) and yExtr = (y0,y1)
    x0 = xExtr[:, 0]
    y0 = yExtr[:, 0]
    gx = xExtr[:, 1] - x0
    gy = yExtr[:, 1] - y0
    f00 = knownVal[:, 0, 0] 
    f01 = knownVal[:, 0, 1] 
    f10 = knownVal[:, 1, 0] 
    f11 = knownVal[:, 1, 1]
    bracket = (pt[:, 1] - y0) / gy * (f11 - f10 - f01 + f00) + f10 - f00
    return (pt[:, 0] - x0) / gx * bracket + (pt[:, 1] - y0) / gy * (f01 - f00) + f00

def ndot(array1, array2):
    return array1[0] * array2[0] - array1[1] * array2[1]