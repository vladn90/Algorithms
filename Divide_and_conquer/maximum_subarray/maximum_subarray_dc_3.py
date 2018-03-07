""" Problem description can be found here:
https://leetcode.com/problems/maximum-subarray/description/
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.
For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4],
the contiguous subarray [4, -1, 2, 1] has the largest sum = 6.
"""
import random
from maximum_subarray_dc_2 import max_subarray_dc_main as dc_simple


def max_between(arr1, arr2):
    """ Returns maximum subarray sum that lies between two arrays.
    Calculates maximum sum for arr1(left array) going from right to left.
    Calculates maximum sum for arr2(right array) going from left to right.
    """
    if len(arr1) > 1:
        s1 = arr1[-1]
        subarr1 = [s1]
        current = s1
        start = len(arr1) - 2
        for i in range(start, -1, -1):
            current += arr1[i]
            if current > s1:
                s1 = current
                subarr1 = arr1[i:]
    else:
        s1 = arr1[0]
        subarr1 = [s1]
    if len(arr2) > 1:
        s2 = arr2[0]
        subarr2 = [s2]
        current = s2
        end = len(arr2)
        for i in range(1, end):
            current += arr2[i]
            if current > s2:
                s2 = current
                subarr2 = arr2[:i + 1]
    else:
        s2 = arr2[0]
        subarr2 = [s2]
    return s1 + s2, subarr1 + subarr2


def max_subarray_dc(array):
    """ Returns the sum of maximum subarray and subarray itself.
    Divide and conquer algorithm.
    Time complexity: O(n * lg(n)). Space complexity: O(n).
    """
    # base case, array has 1 element
    if len(array) == 1:
        return array[0], [array[0]]

    mid = len(array) // 2
    left_arr = array[:mid]
    right_arr = array[mid:]
    max_left, left_subarr = max_subarray_dc(left_arr)
    max_right, right_subarr = max_subarray_dc(right_arr)

    # choosing max subarray sum and max subarray between left and right halves
    if max_left > max_right:
        max_subsum, max_subarr = max_left, left_subarr
    else:
        max_subsum, max_subarr = max_right, right_subarr
    # choosing max between max(left_subarr, right_subarr) and cross_subarr
    max_cross, cross_subarr = max_between(left_arr, right_arr)
    if max_cross > max_subsum:
        max_subsum, max_subarr = max_cross, cross_subarr
    return max_subsum, max_subarr


if __name__ == "__main__":
    # simple tests
    tests = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
             ([-1, -2, -3, -4], -1),
             ([25, 35, 15, 45, 85], 205)
             ]
    for test in tests:
        result = max_subarray_dc(test[0])
        assert result[0] == test[1] == sum(result[1])

    # stress testing updated divide and conquer algorithm against itself
    # and simple divide and conquer algorithm
    dc_updated = max_subarray_dc

    while True:
        array = [random.randrange(-10**6, 10**6) for i in range(10**2)]
        simple_result = dc_simple(array)
        updated_result = dc_updated(array)

        # self-checking
        if updated_result[0] == sum(updated_result[1]):
            print("Self-check is good.")
        else:
            print("Wrong result on the self-check.")
            print(f"array: {array}")
            break

        # testing against simple divide and conquer
        if updated_result[0] == simple_result:
            print("OK")
            print(f"result: {simple_result}")
        else:
            print("Results are different.")
            print(f"array: {array}")
            print(f"simple result: {simple_result}")
            print(f"updated result: {updated_result}")
            break
