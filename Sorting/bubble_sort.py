""" Bubble sort algorithm description,
where n is a length of the input array:
1) Compare consecutive elements in the list.
2) Swap elements if next element < current element.
4) Stop when no more swaps are needed.

Time complexity: O(n^2).
Space complexity: O(1).
"""
import random


def bubble_sort(array):
    """ Sorts array in-place.
    """
    need_swap = True
    while need_swap:
        need_swap = False
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                array[i], array[i + 1] = array[i + 1], array[i]
                need_swap = True


if __name__ == "__main__":
    # stress testing bubble_sort by comparing with built-in sort()
    while True:
        nums = [random.randrange(10**3, 10**12)
                for i in range(random.randrange(10**2, 10**3))]
        nums_bubble = nums[:]
        nums.sort()
        bubble_sort(nums_bubble)
        if nums == nums_bubble:
            print("OK")
            print(f"size of the sorted array: {len(nums)}")
        else:
            print("Something went wrong.")
            print(f"bult-in sort result: {nums}")
            print(f"bubble sort result: {nums_bubble}")
            break
