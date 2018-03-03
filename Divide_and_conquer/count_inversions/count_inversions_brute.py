""" Count inversions in an array. Brute force algorithm.
Algorithm description:
1) Check every element i in the array with all other consecutive elements j.
2) If element i > element j, increase count of inversions by 1.

n - length of the input array
Time complexity: O(n ^ 2).
Space complexity: O(1).
"""


def count_inv_brute(array):
    """ Returns number of inversions in array. Brute force algorithm.
    """
    inv = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                inv += 1
    return inv


def count_inv_brute_2(array):
    """ Returns a list of tuples of numbers that need to be swapped in array.
    Brute force algorithm.
    """
    nums = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                nums.append((array[i], array[j]))
    return nums
