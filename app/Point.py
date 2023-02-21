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
                angle = pi + angle
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
        
        convex_hull = []
        convex_hull.append(p0)
        convex_hull.append(set_of_points[0])
        convex_hull.append(set_of_points[1])
        
        for i in range(2, len(set_of_points)):
            while(Point.non_left_turn(convex_hull[-2], convex_hull[-1], set_of_points[i])):
                convex_hull.pop()
            convex_hull.append(set_of_points[i])
        
        return convex_hull

    def distance_point_segment(s1, s2, p):
        """Distance between segment s1s2 and point p"""
        A = 1.0 / (s2.x - s1.x)
        B = 1.0 / (s1.y - s2.y)
        C = s1.x * s1.y / ((s1.x - s2.x) * (s2.y - s1.y))
        numerator = abs(A * p.x + B * p.y + C)
        denominator = sqrt(A**2 + B**2)
        return numerator / denominator

    def min_x_coordinate(set_of_points):
        min_x = set_of_points[0].x
        index_of_min = 0

        for i in range(len(set_of_points)):
            if(set_of_points[i].x < min_x):
                min_x = set_of_points[i].x
                index_of_min = i

        return index_of_min

    def max_x_coordinate(set_of_points):
        max_x = set_of_points[0].x
        index_of_max = 0

        for i in range(len(set_of_points)):
            if(set_of_points[i].x > max_x):
                max_x = set_of_points[i].x
                index_of_max = i

        return index_of_max

    def farthest_point(S, P, Q):
        """The farthest point from segment PQ
        contained in set S"""
        max_p = Point.distance_point_segment(P, Q, S[0])
        index_of_max = 0

        for i in range(len(S)):
            if(Point.distance_point_segment(P, Q, S[i]) > max_p):
                max_p = Point.distance_point_segment(P, Q, S[i])
                index_of_max = i

        return index_of_max

    def find_hull(CH, Sk, P, Q):
        if(Sk == []): # Set of points is empty
            return
        i = Point.farthest_point(Sk, P, Q)
        C = Sk[i]
        Sk.pop(i)
        S1 = [] # Points to the right of PC
        S2 = [] # Points to the right of CQ
        CH.append(C)

        for p in Sk:
            if(Point.non_left_turn(P, C, p)):
                S1.append(p)
            elif(Point.non_left_turn(C, Q, p)):
                S2.append(p)

        print("PC=", P.x, P.y, C.x, C.y)
        print("Derecha PC")
        Point.print_set_of_points(S1)
        print("CQ=", C.x, C.y, Q.x, Q.y)
        print("Derecha CQ")
        Point.print_set_of_points(S2)

        Point.find_hull(CH, S1, P, C)
        #CH.append(C)
        Point.find_hull(CH, S2, C, Q)
        
    def print_set_of_points(S):
        for p in S:
            print(p.x, p.y)

    def quick_hull(S):
        convex_hull = []
        S1 = [] # Points to the right of AB
        S2 = [] # Points to the left of AB
        i = Point.min_x_coordinate(S)
        A = S[i]
        S.pop(i)
        convex_hull.append(A)
        i = Point.max_x_coordinate(S)
        B = S[i]
        S.pop(i)
        convex_hull.append(B)

        for p in S:
            if(Point.non_left_turn(A, B, p)):
                S1.append(p)
            else:
                S2.append(p)

        Point.find_hull(convex_hull, S1, A, B)
        #convex_hull.append(B)
        Point.find_hull(convex_hull, S2, B, A)

        return convex_hull