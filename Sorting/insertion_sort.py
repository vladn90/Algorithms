""" Insertion sort algorithm description,
where n is a length of the input array:
1) Let array[0] be the sorted array.
2) Choose element i, where i from 1 to n.
3) Insert element i in the sorted array, which goes from i - 1 to 0.

Time complexity: O(n^2).
Space complexity: O(1).
"""
import random


def insertion_sort(array):
    """ Sorts array in-place.
    """
    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    # stress testing insertion_sort by comparing with built-in sort()
    while True:
        nums = [random.randrange(10**3, 10**12)
                for i in range(random.randrange(10**2, 10**3))]
        nums_insert = nums[:]
        nums.sort()
        insertion_sort(nums_insert)
        if nums == nums_insert:
            print("OK")
            print(f"size of the sorted array: {len(nums)}")
        else:
            print("Something went wrong.")
            print(f"bult-in sort result: {nums}")
            print(f"insertion sort result: {nums_insert}")
            break
