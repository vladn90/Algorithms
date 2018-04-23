""" Problem statement:
https://leetcode.com/problems/max-points-on-a-line/description/
"""
import random
import math
from collections import Counter


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x},{self.y})"


class Solution:
    def max_points(self, points):
        """ Algorithm using hash map.
        Time complexity: O(n ^ 2). Space complexity: O(n), n is len(points).
        """
        n = len(points)
        if n < 2:
            return n

        global_max = 0
        for i in range(n - 1):  # 1st point
            x1, y1 = points[i].x, points[i].y
            slopes = Counter()  # tuple(+-xdiff, ydiff): count of such slopes
            curr_max = 0  # count of most often slope
            vertical = 0  # number of points on the same vertical line
            duplicate = 0  # number of points with exactly the same coordinates as points[i]
            for j in range(i + 1, n):  # 2nd point
                x2, y2 = points[j].x, points[j].y
                xdiff, ydiff = x2 - x1, y2 - y1  # slope
                if not xdiff and not ydiff:  # duplicate point
                    duplicate += 1
                elif not xdiff:  # points lie on the vertical line
                    vertical += 1
                else:  # general case
                    if (xdiff < 0 and ydiff <= 0) or (xdiff > 0 and ydiff >= 0):
                        xdiff, ydiff = abs(xdiff), abs(ydiff)
                    else:  # slope ydiff / xdiff is negative, store sign in with xdiff
                        xdiff, ydiff = -abs(xdiff), abs(ydiff)
                    gcd = math.gcd(xdiff, ydiff)
                    xdiff, ydiff = xdiff // gcd, ydiff // gcd
                    slopes[(xdiff, ydiff)] += 1
                curr_max = max(curr_max, slopes[(xdiff, ydiff)])
            # +1 means point itself
            global_max = max(global_max,
                             curr_max + duplicate + 1,
                             vertical + duplicate + 1)
        return global_max

    def max_points_opt(self, points):
        """ Optimized version of the above algorithm. We don't have to account
        separately for points that lie on the vertical line, since we're using
        tuple(xdiff, ydiff) as key in the dictionary.
        Time complexity: O(n ^ 2). Space complexity: O(n), n is len(points).
        """
        if len(points) < 2:
            return len(points)

        global_max = 0
        for i in range(len(points) - 1):  # 1st point
            slopes = Counter()  # tuple(+-xdiff, ydiff): count of such slopes
            curr_max = 0  # count of most often slope
            duplicate = 0  # number of points with exactly the same coordinates as points[i]
            for j in range(i + 1, len(points)):  # 2nd point
                xdiff, ydiff = points[j].x - points[i].x, points[j].y - points[i].y  # slope
                if not xdiff and not ydiff:  # duplicate point
                    duplicate += 1
                else:  # general case
                    if not xdiff or (xdiff < 0 and ydiff <= 0) or (xdiff > 0 and ydiff >= 0):
                        xdiff, ydiff = abs(xdiff), abs(ydiff)
                    else:  # slope ydiff / xdiff is negative, store sign in with xdiff
                        xdiff, ydiff = -abs(xdiff), abs(ydiff)
                    gcd = math.gcd(xdiff, ydiff)
                    xdiff, ydiff = xdiff // gcd, ydiff // gcd
                    slopes[(xdiff, ydiff)] += 1
                if slopes[(xdiff, ydiff)] > curr_max:  # faster than using max
                    curr_max = slopes[(xdiff, ydiff)]
            if curr_max + duplicate + 1 > global_max:  # faster than using max
                global_max = curr_max + duplicate + 1
        return global_max

    def stress_test(self, func1, func2, n):
        """ Stress tests two functions against each other using random array
        of points of size n.
        """
        def random_point():
            x = random.randrange(-10, 10)
            y = random.randrange(-10, 10)
            return Point(x, y)

        while True:
            points = [random_point() for i in range(n)]
            res1, res2 = func1(points), func2(points)
            if res1 == res2:
                print("OK")
                print(res1)
            else:
                print(f"points = {points}")
                print("Results are different.")
                print(f"result 1: {res1}")
                print(f"result 2: {res2}")
                break


if __name__ == "__main__":
    sol = Solution()
    func = sol.max_points_opt

    # simple tests
    assert func([Point(1, 1), Point(2, 2), Point(3, 3)]) == 3
    assert func([Point(1, 1),  Point(3, 2), Point(5, 3),
                 Point(4, 1), Point(2, 3), Point(1, 4)]) == 4
    assert func([Point(1, 4), Point(2, 3), Point(4, 1), Point(3, 2)]) == 4
    assert func([Point(1, 2), Point(2, 2), Point(3, 2)]) == 3
    assert func([Point(2, 1), Point(2, 2), Point(2, 3)]) == 3
    assert func([Point(2, 2), Point(3, 3), Point(-4, -4)]) == 3
    assert func([Point(3, 3), Point(3, 3), Point(3, 3)]) == 3

    # stress testing
    func1 = sol.max_points
    func2 = sol.max_points_opt
    sol.stress_test(func1, func2, 100)
