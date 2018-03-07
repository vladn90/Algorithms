""" Problem description can be found here:
https://leetcode.com/problems/maximum-subarray/description/
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.
For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4],
the contiguous subarray [4, -1, 2, 1] has the largest sum = 6.
"""
import random
from time import time
from maximum_subarray_brute import max_subarray_brute_2 as max_subarray_brute


def max_between(arr1, arr2):
    """ Returns maximum subarray sum that lies between two arrays.
    Calculates maximum sum for arr1(left array) going from right to left.
    Calculates maximum sum for arr2(right array) going from left to right.
    """
    if len(arr1) > 1:
        s1 = arr1[-1]
        current = s1
        start = len(arr1) - 2
        for i in range(start, -1, -1):
            current += arr1[i]
            if current > s1:
                s1 = current
    else:
        s1 = arr1[0]
    if len(arr2) > 1:
        s2 = arr2[0]
        current = s2
        end = len(arr2)
        for i in range(1, end):
            current += arr2[i]
            if current > s2:
                s2 = current
    else:
        s2 = arr2[0]
    return s1 + s2


def max_subarray_dc(array):
    """ Returns the sum of maximum subarray.
    Divide and conquer algorithm.
    Time complexity: O(n * lg(n)). Space complexity: O(n).
    """
    # base case, array has 1 element
    if len(array) == 1:
        return array[0]

    mid = len(array) // 2
    left_arr = array[:mid]
    right_arr = array[mid:]
    max_left = max_subarray_dc(left_arr)  # maximum subarray sum in left half
    max_right = max_subarray_dc(right_arr)  # maximum subarray sum in right half
    # maximum subarray sum in array between left and right arrays
    max_cross = max_between(left_arr, right_arr)
    return max(max_left, max_right, max_cross)


if __name__ == "__main__":
    # simple tests
    tests = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
             ([-1, -2, -3, -4], -1),
             ([25, 35, 15, 45, 85], 205)
             ]
    for test in tests:
        assert max_subarray_dc(test[0]) == test[1]

    # testing divide and conquer algorithm against brute force algorithm
    # and benchmarking it
    brute_time, dc_time = 0, 0
    for j in range(10**3):
        array = [random.randrange(-10**6, 10**6) for i in range(10**2)]

        start = time()
        brute_result = max_subarray_brute(array)
        brute_time += time() - start

        start = time()
        dc_result = max_subarray_dc(array)
        dc_time += time() - start

        if brute_result == dc_result:
            print("OK")
            print(f"{brute_result}")
        else:
            print("Results are different.")
            print(f"array: {array}")
            print(f"brute force result: {brute_result}")
            print(f"divide and conquer result: {dc_result}")
            break
    print(f"brute force: {brute_time}")
    print(f"divide and conquer: {dc_time}")
