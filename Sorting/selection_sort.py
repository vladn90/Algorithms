""" Selection sort algorithm description,
where n is a length of the input array:
1) Select the element i in the array, i from 0 to n - 1.
2) Compare it with element j, j from i + 1 to n.
3) If element j is less than the element i, swap them.
4) Repeat for the rest of the elements.

Time complexity: O(n^2).
Space complexity: O(1).
"""
import random


def selection_sort(array):
    """ Sorts array in-place.
    """
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]


if __name__ == "__main__":
    # stress testing selection_sort by comparing with built-in sort()
    while True:
        nums = [random.randrange(10**3, 10**12)
                for i in range(random.randrange(10**2, 10**3))]
        nums_select = nums[:]
        nums.sort()
        selection_sort(nums_select)
        if nums == nums_select:
            print("OK")
            print(f"size of the sorted array: {len(nums)}")
        else:
            print("Something went wrong.")
            print(f"bult-in sort result: {nums}")
            print(f"selection sort result: {nums_select}")
            break
