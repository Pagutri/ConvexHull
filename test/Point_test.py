import unittest
from ../app/Point import Point

class Point_test(unittest.TestCase):
    def test_point_class_works(self):
        my_point = Point(0.1, 16)
        self.assertEqual(0.1, my_point.x)
        self.assertEqual(16, my_point.y)

if __name__ == '__main__':
    unittest.main()
