import random
from functools import reduce
import operator


def generate_matrix(upper_bound, length, width, height):
    """
    generates 3-dimensional array filled with random numbers greater than 0
    """

    return [[[random.random()*upper_bound
           for i in range(length)]
               for j in range(width)]
                   for k in range(height)]


def get_size(matrix):
    """
    returns size of 3-dimensional matrix: length, width, height
    """

    height = len(matrix)
    width = len(matrix[0])
    length = len(matrix[0][0])
    return length, width, height


def prod(iterable):
    """
    returns product of elements in iterable
    """

    return reduce(operator.mul, iterable, 1)


def get_faces(matrix):
    """
    returns faces of 3-dimensional matrix which
    contain products of elements projected on them
    """

    length, width, height = get_size(matrix)
    facelw = [[1 for i in range(length)] for j in range(width)]
    facelh = [[1 for i in range(length)] for k in range(height)]
    facewh = [[1 for j in range(width)] for k in range(height)]
    for i in range(length):
        for j in range(width):
            facelw[i][j] = prod(matrix[i][j][k] for k in range(height))
    for i in range(length):
        for k in range(height):
            facelh[i][k] = prod(matrix[i][j][k] for j in range(width))
    for j in range(width):
        for k in range(height):
            facewh[j][k] = prod(matrix[i][j][k] for i in range(length))
    return facelw, facelh, facewh


def get_min_coords(face):
    """
    returns coordinates of minimum element in face (2-dimensional list)
    """

    i_min, j_min = 0, 0
    for i, row in enumerate(face):
        for j, elem in enumerate(row):
            if face[i_min][j_min] > face[i][j]:
                i_min, j_min = i, j
    return i_min, j_min


def get_rows(matrix):
    """
    returns rows whose product is minimum
    """

    faces = get_faces(matrix)
    coordslw, coordslh, coordswh = [get_min_coords(face) for face in faces]
    length, width, height = get_size(matrix)
    i, j = coordslw
    yield [matrix[i][j][k] for k in range(height)]
    i, k = coordslh
    yield [matrix[i][j][k] for j in range(width)]
    j, k = coordswh
    yield [matrix[i][j][k] for i in range(length)]

def main():
    UPPER_BOUND = 10
    LENGTH = WIDTH = HEIGHT = 10
    a = generate_matrix(UPPER_BOUND, LENGTH, WIDTH, HEIGHT)
    for index, row in enumerate(get_rows(a)):
        print("row#{} {}".format(index, row))

if __name__ == '__main__':
    main()