""" Problem description can be found here:
https://leetcode.com/problems/maximum-subarray/description/
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.
For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4],
the contiguous subarray [4, -1, 2, 1] has the largest sum = 6.
"""
import random
from time import time


def max_subarray_brute_1(array):
    """ Returns the sum of maximum subarray.
    Brute force algorithm.
    Time complexity: O(n ^ 3). Space complexity: O(n).
    """
    n = len(array)
    max_sum = -float("inf")
    for i in range(n):
        for j in range(i, n):
            curr_sum = sum(array[i:j + 1])
            max_sum = max(max_sum, curr_sum)
    return max_sum


def max_subarray_brute_2(array):
    """ Returns the sum of maximum subarray.
    Improved brute force algorithm using prefix sums.
    Time complexity: O(n ^ 2). Space complexity: O(n).
    """
    n = len(array)
    # creating array of prefix sums
    prefix_sums = [0] * n
    prefix_sums[0] = array[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i - 1] + array[i]
    # for convinience, when checking sum of all elements before first element
    prefix_sums.append(0)

    # looking for the maximum sum
    max_sum = -float("inf")
    for i in range(n):
        for j in range(i, n):
            curr_sum = prefix_sums[j] - prefix_sums[i - 1]
            max_sum = max(max_sum, curr_sum)
    return max_sum


def max_subarray_brute_3(array):
    """ Returns the sum of maximum subarray and subarray itself
    Improved brute force algorithm using prefix sums.
    If there're several max subarray sums, returns the first and the longest
    max subarray.
    Time complexity: O(n ^ 2). Space complexity: O(n).
    """
    n = len(array)
    # creating array of prefix sums
    prefix_sums = [0] * n
    prefix_sums[0] = array[0]
    for i in range(1, n):
        prefix_sums[i] = prefix_sums[i - 1] + array[i]
    # for convinience, when checking sum of all elements before first element
    prefix_sums.append(0)

    # looking for the maximum sum
    max_sum = -float("inf")
    a, b = 0, 0  # start and end indices of max subarray
    for i in range(n):
        for j in range(i, n):
            curr_sum = prefix_sums[j] - prefix_sums[i - 1]
            if curr_sum > max_sum:
                max_sum = curr_sum
                a, b = i, j
    return max_sum, array[a:b + 1]


if __name__ == "__main__":
    # simple tests
    tests = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
             ([-1, -2, -3, -4], -1),
             ([25, 35, 15, 45, 85], 205)
             ]
    for test in tests:
        assert max_subarray_brute_1(test[0]) == test[1]
        assert max_subarray_brute_2(test[0]) == test[1]

    # testing brute force solutions against each other and benchmarking it
    brute1_time, brute2_time = 0, 0
    for j in range(10**3):
        array = [random.randrange(-10**6, 10**6) for i in range(10**2)]

        start = time()
        brute1 = max_subarray_brute_1(array)
        brute1_time += time() - start

        start = time()
        brute2 = max_subarray_brute_2(array)
        brute2_time += time() - start

        brute3 = max_subarray_brute_3(array)

        if brute1 == brute2:
            assert brute3[0] == brute1 == sum(brute3[1])
            print("OK")
            print(f"{brute1}")
        else:
            print("Results are different.")
            print(f"array: {array}")
            print(f"brute 1 result: {brute1}")
            print(f"brute 2 result: {brute2}")
            break
    print(f"simple brute force: {brute1_time}")
    print(f"improved brute force: {brute2_time}")
