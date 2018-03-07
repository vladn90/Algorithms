""" Problem description can be found here:
https://leetcode.com/problems/maximum-subarray/description/
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.
For example, given the array [-2, 1, -3, 4, -1, 2, 1, -5, 4],
the contiguous subarray [4, -1, 2, 1] has the largest sum = 6.
"""
import random
from maximum_subarray_brute import max_subarray_brute_2, max_subarray_brute_3


def max_subarray_kadane_1(array):
    """ Kadane's algorithm for finding sum of maximum subarray.
    Time complexity: O(n). Space complexity: O(1).
    """
    max_sum = array[0]  # sum of max subarray so far
    curr_sum = array[0]  # max sum of subarray ending at index i
    for i in range(1, len(array)):
        curr_sum = max(array[i], curr_sum + array[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum


def max_subarray_kadane_2(array):
    """ Kadane's algorithm with tracking the maximum subarray.
    Returns maximum subarray sum and subarray itself.
    If there're several max subarray sums, returns the first and the longest
    max subarray.
    Time complexity: O(n). Space complexity: O(1).
    """
    max_sum = array[0]  # sum of max subarray so far
    curr_sum = array[0]  # max sum of subarray ending at index i
    start, end = 0, 0  # start and end index of max subarray
    curr_start, curr_end = 0, 0  # start and end index of current subarray
    for i in range(1, len(array)):
        # choosing current max subarray ending at index i
        if curr_sum + array[i] > array[i]:
            curr_sum += array[i]
            curr_end += 1
        # using this if condition will return longest max subarray
        # delete it to return shortest max subarray
        elif curr_sum + array[i] == array[i]:
            curr_sum += array[i]
            curr_end += 1
        else:
            curr_sum = array[i]
            curr_start, curr_end = i, i
        # choosing max subarray
        if curr_sum > max_sum:
            max_sum = curr_sum
            start, end = curr_start, curr_end
    return max_sum, array[start:end + 1]


if __name__ == "__main__":
    # simple tests
    tests = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
             ([-1, -2, -3, -4], -1),
             ([25, 35, 15, 45, 85], 205)
             ]
    for test in tests:
        result = max_subarray_kadane_2(test[0])
        assert result[0] == sum(result[1]) == test[1]
        assert max_subarray_kadane_1(test[0]) == test[1]

    # stress testing dynamic programming algorithm against brute force algorithm
    while True:
        array = [random.randrange(-10**2, 10**2) for i in range(10**2)]

        # testing simple solutions without tracking of the subarray
        kadane_1 = max_subarray_kadane_1(array)
        brute_1 = max_subarray_brute_2(array)
        if kadane_1 == brute_1:
            print("OK")
            print(kadane_1)
            print()
        else:
            print("results are different")
            print(f"initial array: {array}")
            print(f"kadane 1 result: {kadane_1}")
            print(f"brute 1 result: {brute_1}")
            break

        # testing solutions with tracking the max subarray itself
        kadane_2 = max_subarray_kadane_2(array)
        brute_2 = max_subarray_brute_3(array)
        if kadane_2 == brute_2:
            assert kadane_1 == kadane_2[0] == sum(kadane_2[1])
            assert brute_1 == brute_2[0] == sum(brute_2[1])
            print("OK")
            print(kadane_2)
            print()
        else:
            print("results are different")
            print(f"initial array: {array}")
            print(f"kadane 2 result: {kadane_2}")
            print(f"brute 2 result: {brute_2}")
            break
