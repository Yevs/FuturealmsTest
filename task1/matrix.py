import random
from functools import reduce
import operator

import numpy as np


def generate_matrix(upper_bound, length, width, height):
    """
    generates 3-dimensional array filled with random numbers greater than 0
    """

    return np.random.rand(length, width, height) * upper_bound



def get_faces(matrix):
    """
    returns faces of 3-dimensional matrix which
    contain products of elements projected on them
    """

    length, width, height = matrix.shape
    facelw = np.ones((length, width))
    facelh = np.ones((length, height))
    facewh = np.ones((width, height))
    for i in range(length):
        for j in range(width):
            facelw[i, j] = np.prod(matrix[i, j, :])
    for i in range(length):
        for k in range(height):
            facelh[i, k] = np.prod(matrix[i, :, k])
    for j in range(width):
        for k in range(height):
            facewh[j, k] = np.prod(matrix[:, j, k])
    return facelw, facelh, facewh


def get_min_coords(face):
    """
    returns coordinates of minimum element in face (2-dimensional list)
    """

    min_index = np.argmin(face)  # flattened
    return np.floor_divide(min_index, face.shape[0]), min_index % face.shape[0]


def get_rows(matrix):
    """
    returns rows whose product is minimum
    """

    faces = get_faces(matrix)
    coordslw, coordslh, coordswh = [get_min_coords(face) for face in faces]
    length, width, height = matrix.shape
    i, j = coordslw
    yield matrix[i, j, :]
    i, k = coordslh
    yield matrix[i, :, k]
    j, k = coordswh
    yield matrix[:, j, k]

def main():
    UPPER_BOUND = 10
    LENGTH = WIDTH = HEIGHT = 10
    a = generate_matrix(UPPER_BOUND, LENGTH, WIDTH, HEIGHT)
    for index, row in enumerate(get_rows(a)):
        print("row#{} {}".format(index, row))

if __name__ == '__main__':
    main()