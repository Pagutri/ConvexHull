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

    def test_sort_by_angle_method(self):
        p1 = Point(1.0, 3.0)
        p2 = Point(3.0, 3.0)
        p5 = Point(1.0, 1.0)
        p3 = Point(0.0, 2.0)
        p4 = Point(4.0, 2.0)
        p6 = Point(3.0, 2.0)
        p7 = Point(2.0, 4.0)
        p8 = Point(5.0, 3.0)
        set_of_points = [p1, p2, p3, p4, p6, p7, p8]
        new_set = Point.sort_by_angle(p5, set_of_points)
        #for i in range(len(set_of_points)):
         #   print(set_of_points[i].x, set_of_points[i].y)
            
    def test_non_left_turn(self):
        p1 = Point(1.0, 3.0)
        p2 = Point(3.0, 3.0)
        p5 = Point(1.0, 1.0)
        p3 = Point(0.0, 2.0)
        p4 = Point(4.0, 2.0)
        p6 = Point(3.0, 2.0)
        p7 = Point(2.0, 4.0)
        p8 = Point(5.0, 3.0)
        self.assertEqual(False, Point.non_left_turn(p5, p4, p2))
        self.assertEqual(True, Point.non_left_turn(p5, p6, p8))
        self.assertEqual(True, Point.non_left_turn(p5, p2, p4))

    def test_distance_point_segment(self):
        p1 = Point(1, 1)
        p2 = Point(2, 2)
        p3 = Point(2, 1)
        print(Point.distance_point_segment(p1, p2, p3))


if __name__ == '__main__':
    unittest.main()
