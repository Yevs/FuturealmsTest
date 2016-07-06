import unittest
from matrix import get_size, prod, get_faces, get_min_coords, get_rows

class Test(unittest.TestCase):

    def test_get_size(self):
        a = [[[0]]]
        self.assertEqual(get_size(a), (1, 1, 1))
        a = [[[1, 2],
              [1, 2]],
             [[1, 2],
              [1, 2]]]
        self.assertEqual(get_size(a), (2, 2, 2))

    def test_prod(self):
        self.assertEqual(prod([0, 1, 2]), 0)
        self.assertEqual(prod([1, 1, 1]), 1)
        self.assertEqual(prod([1, 2, 3]), 6)

    def test_get_faces(self):
        a = [[[1, 1],
              [1, 1]],
             [[1, 1],
              [1, 1]]]
        faces = get_faces(a)
        for face in faces:
            for row in face:
                for elem in row:
                    self.assertEqual(elem, 1)
        a = [[[2, 2],
              [2, 2]],
             [[2, 2],
              [2, 2]]]
        faces = get_faces(a)
        for face in faces:
            for row in face:
                for elem in row:
                    self.assertEqual(elem, 4)

    def test_get_min_coords(self):
        a = [[1]]
        self.assertEqual(get_min_coords(a), (0, 0))
        a = [[5, 2], [1, 3]]
        self.assertEqual(get_min_coords(a), (1, 0))

    def test_get_rows(self):
        a = [[[1]]]
        rows = get_rows(a)
        for row in rows:
            for elem in row:
                self.assertEqual(elem, 1)
        a = [[[1, 1],
              [1, 2]],
             [[1, 2],
              [2, 2]]]
        rows = get_rows(a)
        for row in rows:
            for elem in row:
                self.assertEqual(elem, 1)

if __name__ == '__main__':
    unittest.main()