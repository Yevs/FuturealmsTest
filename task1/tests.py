import unittest

import numpy as np

from matrix import get_faces, get_min_coords, get_rows

class Test(unittest.TestCase):

    def test_get_faces(self):
        a = np.array([[[1, 1],
                       [1, 1]],
                      [[1, 1],
                       [1, 1]]])
        faces = get_faces(a)
        for face in faces:
            for row in face:
                for elem in row:
                    self.assertEqual(elem, 1)
        a = np.array([[[2, 2],
                       [2, 2]],
                      [[2, 2],
                       [2, 2]]])
        faces = get_faces(a)
        for face in faces:
            for row in face:
                for elem in row:
                    self.assertEqual(elem, 4)

    def test_get_min_coords(self):
        a = np.array([[1]])
        self.assertEqual(get_min_coords(a), (0, 0))
        a = np.array([[5, 2], [1, 3]])
        self.assertEqual(get_min_coords(a), (1, 0))

    def test_get_rows(self):
        a = np.array([[[1]]])
        rows = get_rows(a)
        for row in rows:
            for elem in row:
                self.assertEqual(elem, 1)
        a = np.array([[[1, 1],
                      [1, 2]],
                     [[1, 2],
                      [2, 2]]])
        rows = get_rows(a)
        for row in rows:
            for elem in row:
                self.assertEqual(elem, 1)

if __name__ == '__main__':
    unittest.main()