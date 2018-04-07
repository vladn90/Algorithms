""" Problem statement:
https://leetcode.com/problems/trapping-rain-water/description/
"""
import random


class Solution:
    def trap_brute_1(self, height):
        """ Brute force algorithm. Loop over elevations. If the next elevation
        is lower than previous one, calculate difference between two heights.
        For every height in this difference check if there's an elevation to the
        right that is >= current height. If there's such an elevation, then
        horizontal line of water is the amount of water that's gonna be trapped
        between this two points.

        Time complexity: O(n ^ 2). Space complexity: O(1), n is len(height).
        """
        n = len(height)
        # special case, water can't be trapped if we have 2 or less elevations
        if n < 3:
            return 0

        prev = height[0]  # previous height
        water = 0
        for i in range(1, n):
            curr = height[i]  # current height
            if curr < prev:  # possible water trapping
                # loop over gap between current and next height
                for d in range(prev, curr, -1):
                    # find next greater or equal height elevation
                    # for every height in the gap
                    for j in range(i + 1, n):
                        if height[j] >= d:  # found it
                            # calculate current water segment length
                            # and adjust total trapped water
                            water += (j - i)
                            break
            prev = height[i]
        return water

    def trap_brute_2(self, height):
        """ Different brute force algorithm. Check every elevation, find highest
        elevation to the left and to the right, take the minimum height of both,
        calculate difference between current elevation and minimum height from
        left and right. That's gonna be amount of water trapped in this elevation.

        Time complexity: O(n ^ 2). Space complexity: O(1), n is len(height).
        """
        n = len(height)
        # special case, water can't be trapped if we have 2 or less elevations
        if n < 3:
            return 0

        water = 0  # total amount of trapped water
        for i in range(n):
            # find highest elevation to the left
            left = 0
            j = i - 1
            while j > -1:
                left = max(left, height[j])
                j -= 1
            # find highest elevation to the right
            right = 0
            j = i + 1
            while j < n:
                right = max(right, height[j])
                j += 1
            # find the min height among left and right elevations and
            # calculate the difference with current height, adjust water
            min_height = min(left, right)
            diff = min_height - height[i]
            if diff > 0:  # some water has been trapped
                water += diff
        return water

    def trap_fast(self, height):
        """ Improved algorithm, based on 2nd brute force solution. We precompute
        highest elevation to the left of current elevation and to the right.
        Time complexity: O(n). Space complexity: O(n), n is len(height).
        """
        n = len(height)
        # special case, water can't be trapped if we have 2 or less elevations
        if n < 3:
            return 0

        # precompute array of highest elevation to the left of i
        left = [0] * n
        max_left = 0  # highest elevation so far
        # start with 2nd elevation, since there's nothing to the left of 1st
        for i in range(1, n):
            max_left = max(max_left, height[i - 1])
            left[i] = max_left

        # precompute array of highest elevation to the right of i
        right = [0] * n
        max_right = 0
        for i in range(n - 2, -1, -1):
            max_right = max(max_right, height[i + 1])
            right[i] = max_right

        # calculate amount of water trapped in each elevation
        water = 0
        for i in range(1, n):  # no water can be trapped in 1st elevation
            min_height = min(left[i], right[i])
            diff = min_height - height[i]
            if diff > 0:
                water += diff
        return water

    def trap_fast_opt(self, height):
        """ Optimized improved algorithm.
        Time complexity: O(n). Space complexity: O(n), n is len(height).
        """
        n = len(height)
        # special case, water can't be trapped if we have 2 or less elevations
        if n < 3:
            return 0

        # precompute array of highest elevation to the left of i
        # start with 2nd elevation, since there's nothing to the left of 1st
        left = [0]
        for i in range(1, n):
            left.append(max(left[i - 1], height[i - 1]))

        # precompute array of highest elevation to the right of i
        # and calculate amount of water trapped in current elevation
        water = 0
        max_right = 0
        for i in range(n - 2, -1, -1):
            max_right = max(max_right, height[i + 1])
            diff = min(max_right, left[i]) - height[i]
            if diff > 0:
                water += diff
        return water

    def trap_fast_2pointers(self, height):
        """ Space optimized version using two pointers technique.
        Time complexity: O(n). Space complexity: O(1), n is len(height).
        """
        water = 0  # total amount of trapped water
        left_max, right_max = 0, 0  # highest elevation to left and right
        i, j = 0, len(height) - 1  # left, right pointers
        while i < j:
            if height[i] <= height[j]:
                if height[i] > left_max:  # trapping water is not possible
                    left_max = height[i]
                else:
                    water += (left_max - height[i])
                i += 1
            else:
                if height[j] >= right_max:  # trapping water is not possible
                    right_max = height[j]
                else:
                    water += (right_max - height[j])
                j -= 1
        return water

    def generate_data(self, n):
        """ Generates random array of n integers and writes it to the
        standard output as [a1, a2, a3...an].
        """
        height = [random.randrange(1, 10) for i in range(n)]
        print(f"[{height[0]}", end=",")
        for i in range(1, len(height) - 1):
            print(height[i], end=",")
        print(f"{height[-1]}]")

    def read_data(self):
        """ Reads data from the standard input and converts it to array of int.
        """
        height = input().strip()
        height = list(map(int, height[1:len(height) - 1].split(",")))
        return height

    def stress_test(self, func1, func2):
        """ Stress tests two functions against each other using random input.
        """
        while True:
            height = [random.randrange(1, 10) for i in range(10**2)]
            func1_result, func2_result = func1(height), func2(height)
            if func1_result == func2_result:
                print("OK")
                print(func1_result)
            else:
                print("Results are different.")
                print(f"height = {height}")
                print(f"func1 result: {func1_result}")
                print(f"func2 result: {func2_result}")
                break


if __name__ == "__main__":
    sol = Solution()
    func = sol.trap_fast_2pointers
    # func1 = sol.trap_fast_opt
    # func2 = sol.trap_fast_2pointers

    # tests
    assert func([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert func([5, 1, 2, 3, 4, 5]) == 10
    assert func([5, 4, 3, 2, 1, 5]) == 10
    assert func([1, 1, 1, 2]) == 0
    assert func([2, 1, 1, 1]) == 0
    assert func([1, 1, 1, 1]) == 0
    assert func([1, 1, 10, 1]) == 0

    # sol.stress_test(func1, func2)
