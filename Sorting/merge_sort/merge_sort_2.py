""" Merge sort algorithm description,
where n is a length of the input array:
1) Divide the array into two parts: left and right.
2) Sort recursively each part.
3) Combine sorted arrays.

Time complexity: O(n * log(n)).
Space complexity: O(n).
"""
import random


def combine(array, a1, a2, b1, b2):
    i, j = a1, b1
    result = []
    # chooose the minimum element from left or right part of the array
    # and add it to result
    while i <= a2 and j <= b2:
        if array[i] <= array[j]:
            result.append(array[i])
            i += 1
        else:
            result.append(array[j])
            j += 1
    # add to result whatever is left from left or right parts of the array
    if i > a2:
        while j <= b2:
            result.append(array[j])
            j += 1
    else:
        while i <= a2:
            result.append(array[i])
            i += 1
    # override original array with the sorted array
    array[a1:b2 + 1] = result


def merge_s(array, start, end):
    """ Improved implementation using pointers to start and end of the array.
    Overrides original array.
    """
    # recursive case
    if end > start:
        mid = (end + start) // 2
        merge_s(array, start, mid)
        merge_s(array, mid + 1, end)
        combine(array, start, mid, mid + 1, end)


def merge_sort(array):
    """ Wrapper function for merge_s.
    """
    return merge_s(array, 0, len(array) - 1)


if __name__ == "__main__":
    # stress testing merge_sort against built-in sorting algorithm
    while True:
        array = [random.randrange(10**6, 10**12)
                 for i in range(random.randrange(10**3, 10**4))]
        arr1, arr2 = array[:], array[:]
        arr1.sort()
        merge_sort(arr2)
        if arr1 == arr2:
            print("OK")
            print(len(array))
        else:
            print("Something went wrong.")
            print(f"array: {array}")
            print(f"built-in sort result: {arr1}")
            print(f"merge sort result: {arr2}")
            break
