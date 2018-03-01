""" Merge sort algorithm description,
where n is a length of the input array:
1) Divide the array into two parts: left and right.
2) Sort recursively each part.
3) Combine sorted arrays.

Time complexity: O(n * log(n)).
Space complexity: O(n).
"""
import random


def combine(array1, array2):
    i, j = 0, 0
    result = []
    # chooose the minimum element from array1 and array2 and add it to result
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    # add to result whatever is left of array1 or array2
    if i == len(array1):
        while j < len(array2):
            result.append(array2[j])
            j += 1
    else:
        while i < len(array1):
            result.append(array1[i])
            i += 1
    return result


def merge_sort(array):
    """ Simple implementation. Creates a copy of an input array in each call.
    """
    # base case
    if len(array) <= 1:
        return array

    # recursive case
    mid = len(array) // 2
    left = merge_sort(array[:mid])  # sort the left part of the array
    right = merge_sort(array[mid:])  # sort the right part of the array
    return combine(left, right)  # combine sorted arrays


if __name__ == "__main__":
    # stress testing merge_sort against built-in sorting algorithm
    while True:
        array = [random.randrange(10**3, 10**6)
                 for i in range(random.randrange(10**3, 10**4))]
        if sorted(array) == merge_sort(array):
            print("OK")
            print(len(array))
        else:
            print("Something went wrong.")
            print(f"array: {array}")
            break
