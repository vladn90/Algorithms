""" Problem description can be found here:
https://leetcode.com/problems/container-with-most-water/description/

Very good and detailed algorithm description is here:
https://leetcode.com/articles/container-most-water/
"""
import random


class Solution:
    def max_area_brute(self, coord):
        """ Brute force algorithm.
        Time complexity: O(n ^ 2). Space complexity: O(1), n is len(coord).
        """
        max_area = 0
        n = len(coord)
        for x1 in range(n - 1):
            for x2 in range(x1 + 1, n):
                y1, y2 = coord[x1], coord[x2]
                curr_area = (x2 - x1) * min(y1, y2)
                max_area = max(max_area, curr_area)
        return max_area

    def max_area_2p(self, coord):
        """ Two pointers algorithm.
        Time complexity: O(n). Space complexity: O(1), n is len(coord).
        """
        n = len(coord)
        i, j = 0, n - 1
        max_area = 0
        while i < j:
            # area = (x2 - x1) * min(y2, y1)
            curr_area = (j - i) * min(coord[i], coord[j])
            max_area = max(max_area, curr_area)
            if coord[i] < coord[j]:  # move left line
                i += 1
            else:  # move right line
                j -= 1
        return max_area


if __name__ == "__main__":
    sol = Solution()
    func = sol.max_area_2p

    # simple tests
    assert func([1, 5, 4, 3]) == 6
    assert func([1, 3, 4, 3]) == 6
    assert func([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    # stress testing brute force algorithm against two pointers algorithm
    while True:
        coord = [random.randrange(1, 10) for i in range(10**2)]
        result_brute = sol.max_area_brute(coord)
        result_2p = sol.max_area_2p(coord)
        if result_brute == result_2p:
            print("OK")
            print(result_brute)
        else:
            print("Results are different.")
            print(f"coordinates = {coord}")
            print(f"brute force result: {result_brute}")
            print(f"two pointers result: {result_2p}")
            break
