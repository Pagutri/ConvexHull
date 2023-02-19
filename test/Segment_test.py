import unittest
import sys
sys.path.append('../app')
from Point import Point
from Segment import Segment

class Segment_test(unittest.TestCase):
    def test_segment_class_works(self):
    	p1 = Point(1.0, 2.0)
    	p2 = Point(3.4, 6)
    	my_segment = Segment(p1, p2)
    	self.assertEqual(1.0, my_segment.p1.x)
    	self.assertEqual(2.0, my_segment.p1.y)
    	self.assertEqual(3.4, my_segment.p2.x)
    	self.assertEqual(6, my_segment.p2.y)

if __name__ == '__main__':
    unittest.main()
