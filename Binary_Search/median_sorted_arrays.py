""" Problem statement:
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""
import random


class Solution:
    def median_arrays_naive(self, nums1, nums2):
        """ Returns median of two sorted arrays. Naive algorithm.
        Time complexity: O(n + m). Space complexity: O(n + m), where
        n, m are len(nums1), len(nums2).
        """
        # use combine part of Merge Sort algorithm to merge two sorted arrays
        n, m = len(nums1), len(nums2)
        array = []  # combined sorted array
        i, j = 0, 0  # indices of current element in nums1 and nums2
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                array.append(nums1[i])
                i += 1
            else:
                array.append(nums2[j])
                j += 1
        while i < n:  # add whatever is left from nums1
            array.append(nums1[i])
            i += 1
        while j < m:  # add whatever is left from nums2
            array.append(nums2[j])
            j += 1

        # find median of combined array
        len_arr = len(array)
        if len_arr % 2 == 0:
            return (array[len_arr // 2] + array[len_arr // 2 - 1]) / 2
        return array[len_arr // 2]

    def median_arrays(self, arr1, arr2):
        """ Returns median of two sorted arrays. Algorithm based on binary search.
        Time complexity: O(lg(min(n, m))). Space complexity: O(1), where
        n, m are len(arr1), len(arr2).
        """
        if len(arr1) > len(arr2):  # always choose arr1 as array with min length
            arr1, arr2 = arr2, arr1

        x, y = len(arr1), len(arr2)
        start, end = 0, x
        while start <= end:
            px = (start + end) // 2  # partition x
            py = (x + y + 1) // 2 - px  # px + py = (x + y + 1) // 2

            # choose elements from arr1 near partition line
            if px > 0:
                left_x = arr1[px - 1]  # rightmost element in left half of arr1
            else:
                left_x = float("-inf")  # no elements, choose -inf
            if px < x:
                right_x = arr1[px]  # leftmost element in right half of arr1
            else:
                right_x = float("inf")  # no elements, choose inf

            # choose elements from arr2 near partition line
            if py > 0:
                left_y = arr2[py - 1]  # rightmost element in left half of arr2
            else:
                left_y = float("-inf")  # no elements, choose -inf
            if py < y:
                right_y = arr2[py]  # leftmost element in right half of arr2
            else:
                right_y = float("inf")  # no elements, choose inf

            # binary search decisions below
            if left_x <= right_y and left_y <= right_x:  # median is found
                if (x + y) % 2 == 0:  # merged array length is even
                    return (max(left_x, left_y) + min(right_x, right_y)) / 2
                return max(left_x, left_y)  # merged array length is odd
            elif left_x > right_y:  # move partition line to the left
                end = px - 1
            else:  # left_y > right_x, move partition line to the right
                start = px + 1


if __name__ == "__main__":
    sol = Solution()
    func = sol.median_arrays

    # tests
    arr1 = [1, 3, 8, 9, 15]
    arr2 = [7, 11, 18, 19, 21, 25]
    assert func(arr1, arr2) == 11

    arr1 = [23, 26, 31, 35]
    arr2 = [3, 5, 7, 9, 11, 16]
    assert func(arr1, arr2) == 13.5

    arr1 = [1, 2]
    arr2 = [3, 40]
    assert func(arr1, arr2) == 2.5

    arr1 = [1, 6, 8, 11]
    arr2 = [3, 5, 10]
    assert func(arr1, arr2) == 6

    arr1 = [1, 2, 3]
    arr2 = []
    assert func(arr1, arr2) == 2

    arr1 = [1, 2, 3, 4]
    arr2 = []
    assert func(arr1, arr2) == 2.5

    # stress testing naive algorithm against improved algorithm
    while True:
        arr1 = [random.randrange(1, 10**3) for i in range(10**2)]
        arr2 = [random.randrange(1, 10**3) for i in range(10**2 + random.choice([-1, 0, 1]))]
        arr1.sort()
        arr2.sort()

        func1 = sol.median_arrays_naive
        func2 = sol.median_arrays
        res1 = func1(arr1, arr2)
        res2 = func2(arr1, arr2)
        if res1 == res2:
            print("OK")
            print(res1)
        else:
            print("Results are different.")
            print(f"arr1 = {arr1}")
            print(f"arr2 = {arr2}")
            print(f"res1 = {res1}")
            print(f"res2 = {res2}")
            break
