import unittest
import sys
sys.path.append('../app')
from Point import Point

class Point_test(unittest.TestCase):
    def test_point_class_works(self):
        my_point = Point(0.1, 16)
        self.assertEqual(0.1, my_point.x)
        self.assertEqual(16, my_point.y)

    def test_sub_method(self):
        p2 = Point(5.0, 2.0)
        p3 = Point(3.5, 6.0)
        diff = p2 - p3
        self.assertEqual(1.5, diff.x)
        self.assertEqual(-4.0, diff.y)

    def test_dot_product_method(self):
        p1 = Point(2.0, 1.0)
        p2 = Point(5.0, 2.0)
        p3 = Point(3.5, 6.0)
        self.assertEqual(12.0, Point.dot_product(p2,p1))
        self.assertEqual(29.5, Point.dot_product(p2,p3))

    def test_norm(self):
        p3 = Point(3.5, 6.0)
        self.assertEqual(69462, int(p3.norm() * 1e4))

    def test_angle_between_segments_method(self):
        p1 = Point(2.0, 1.0)
        p2 = Point(5.0, 2.0)
        p3 = Point(3.5, 6.0)
        self.assertEqual(9575, int(Point.angle_between_segments(p2,p1,p3) * 1e4))

    def test_min_y_coordinate(self):
        p1 = Point(2.0, 1.0)
        p2 = Point(5.0, 2.0)
        p5 = Point(1.0, 1.0)
        p3 = Point(3.5, 6.0)
        p4 = Point(0.1, 16)
        set_of_points = [p4, p2, p1, p3, p5]
        self.assertEqual(4, Point.min_y_coordinate(set_of_points))

    def test_graham_scan(self):
        p1 = Point(1.0, 3.0)
        p2 = Point(3.0, 3.0)
        p5 = Point(1.0, 1.0)
        p3 = Point(0.0, 2.0)
        p4 = Point(4.0, 2.0)
        p6 = Point(3.0, 2.0)
        p7 = Point(2.0, 4.0)
        set_of_points = [p1, p2, p3, p4, p5, p6, p7]
        new_set = Point.graham_scan(set_of_points)
        for i in range(len(set_of_points)):
            print(set_of_points[i].x, set_of_points[i].y)

if __name__ == '__main__':
    unittest.main()
