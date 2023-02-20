from math import sqrt, acos, atan, pi

class Point():
    """2D Points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def dot_product(p1, p2):
        return p1.x*p2.x + p1.y*p2.y

    def norm(self):
        return sqrt(self.x**2 + self.y**2)

    def polar_angle(self):
        """Angle of the vector that points to self
        with respect to the origin. From 0 to pi
        in order to be used in the graham scan
        algorithm"""
        if(self.x != 0):
            angle = atan(self.y / self.x)
            if(angle < 0):
                angle = 0.5 * pi - angle
        else:
            angle = 0.5 * pi
        
        return angle
    
    def angle_between_segments(p1, p2, p3):
        """Angle between segments p2p1 and p2p3"""
        # Translate segments to the origin
        p1_prim = p1 - p2
        p3_prim = p3 - p2
        numerator = Point.dot_product(p1_prim, p3_prim)
        denominator = p1_prim.norm() * p3_prim.norm()
        return acos(numerator / denominator)

    def min_y_coordinate(set_of_points):
        min_y = set_of_points[0].y
        index_of_min = 0

        for i in range(len(set_of_points)):
            if(set_of_points[i].y < min_y):
                min_y = set_of_points[i].y
                index_of_min = i
            elif(set_of_points[i].y == min_y \
                and set_of_points[i].x < set_of_points[index_of_min].x):
                min_y = set_of_points[i].y
                index_of_min = i

        return index_of_min

    def sort_by_angle(p0, set_of_points):
        """Sort the set of points by polar angle
        with respect to p0"""
        set_of_points.sort(key = lambda x: (x - p0).polar_angle())
        return set_of_points
        
    def non_left_turn(p0, p1, p2):
        """Answer the question: if we walk along the
        segment p0p1 and then along the segment p1p2,
        is it true that we don't turn left?"""
        cross_product = (p2-p0).x*(p1-p0).y - (p2-p0).y*(p1-p0).x
        return cross_product >= 0
    
    def graham_scan(set_of_points):
        """Convex hull"""
        i = Point.min_y_coordinate(set_of_points)
        p0 = set_of_points[i]
        del set_of_points[i]
        set_of_points.sort(key = lambda x: (x - p0).polar_angle())
        return set_of_points
