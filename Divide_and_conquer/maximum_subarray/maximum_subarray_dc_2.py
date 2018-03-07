""" Problem description can be found here:
https://leetcode.com/problems/maximum-subarray/description/
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.
For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4],
the contiguous subarray [4, -1, 2, 1] has the largest sum = 6.
"""
import random
from time import time
from maximum_subarray_dc_1 import max_subarray_dc as dc_simple


def max_between(array, left_start, left_end, right_start, right_end):
    """ Returns maximum subarray sum that lies between two arrays.
    Calculates maximum sum for arr1(left array) going from right to left.
    Calculates maximum sum for arr2(right array) going from left to right.
    """
    if left_start != left_end:
        s1 = array[left_end]
        current = s1
        for i in range(left_end - 1, left_start - 1, -1):
            current += array[i]
            if current > s1:
                s1 = current
    else:
        s1 = array[left_start]
    if right_start != right_end:
        s2 = array[right_start]
        current = s2
        for i in range(right_start + 1, right_end + 1):
            current += array[i]
            if current > s2:
                s2 = current
    else:
        s2 = array[right_start]
    return s1 + s2


def max_subarray_dc(array, start, end):
    """ Returns the sum of maximum subarray.
    Divide and conquer algorithm. Optimized by using pointers to start and end
    of subarrays instead of array slices.
    Time complexity: O(n * lg(n)). Space complexity: O(lg(n)).
    """
    # base case, array has 1 element
    if start == end:
        return array[start]

    mid = (start + end + 1) // 2
    max_left = max_subarray_dc(array, start, mid - 1)  # maximum subarray sum in left half
    max_right = max_subarray_dc(array, mid, end)  # maximum subarray sum in right half
    # maximum subarray sum in array between left and right arrays
    max_cross = max_between(array, start, mid - 1, mid, end)
    return max(max_left, max_right, max_cross)


def max_subarray_dc_main(array):
    return max_subarray_dc(array, 0, len(array) - 1)


if __name__ == "__main__":
    # simple tests
    tests = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
             ([-1, -2, -3, -4], -1),
             ([25, 35, 15, 45, 85], 205)
             ]
    for test in tests:
        assert max_subarray_dc_main(test[0]) == test[1]

    # testing optimized divide and conquer algorithm against
    # simple divide and conquer algorithm, benchmarking it
    dc_fast = max_subarray_dc_main

    dc_simple_time, dc_fast_time = 0, 0
    for j in range(10**3):
        array = [random.randrange(-10**6, 10**6) for i in range(10**2)]

        start = time()
        dc_simple_result = dc_simple(array)
        dc_simple_time += time() - start

        start = time()
        dc_fast_result = dc_fast(array)
        dc_fast_time += time() - start

        if dc_simple_result == dc_fast_result:
            print("OK")
            print(f"{dc_simple_result}")
        else:
            print("Results are different.")
            print(f"array: {array}")
            print(f"simple dc result: {dc_simple_result}")
            print(f"fast dc result: {dc_fast_result}")
            break
    print(f"simple dc time: {dc_simple_time}")
    print(f"fast dc time: {dc_fast_time}")
