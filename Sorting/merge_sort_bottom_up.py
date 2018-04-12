""" Python implementation of bottom-up, or iterative, Merge Sort.
Pseudocode can be found here:
https://en.wikipedia.org/wiki/Merge_sort#Bottom-up_implementation
"""
import random


def merge(array, start, mid, end):
    """ Merges two sorted arrays into a new array. Updates original array.
    left array[start:mid], right array[mid + 1:end]

    Time complexity: O(n). Space complexity: O(n), n is len(array[start:end]).
    """
    result = []  # temporary auxiliary array
    i, j = start, mid + 1  # starting indices of left and right arrays
    while i <= mid and j <= end:  # choose min element from both arrays
        if array[i] <= array[j]:
            result.append(array[i])
            i += 1
        else:
            result.append(array[j])
            j += 1
    while i <= mid:  # add whatever is from left array
        result.append(array[i])
        i += 1
    while j <= end:  # add whatever is left from right array
        result.append(array[j])
        j += 1
    array[start:end + 1] = result  # update original array


def merge_sort(array):
    """ Uses iterative merge sort to sort the array. Sorts array in-place.
    Time complexity: O(n * lg(n)). Space complexity: O(n), n is len(array).
    """
    n = len(array)
    size = 1  # size of currently merged arrays
    while size < n:
        start = 0
        while start < n - size:
            # start >> start index of the left array
            # start + size -  1 >> end index of the left array
            # (start + size -  1) + 1 >> start index of the right array
            # start + size * 2 - 1 >> end index of the right array
            # n - 1 >> end index of the right array, when array length is not power of two
            merge(array, start, start + size - 1, min(start + size * 2 - 1, n - 1))
            start += size * 2
        size *= 2  # double the size on each step


if __name__ == "__main__":
    # stress testing against built-in sort
    while True:
        array = [random.randrange(-10**3, 10**3) for i in range(random.randrange(10**2, 10**4))]
        arr1 = array[:]
        arr2 = array[:]
        arr1.sort()
        merge_sort(arr2)
        assert arr1 == arr2
        print("All good!")
        print(arr1[:10], arr2[:10])
