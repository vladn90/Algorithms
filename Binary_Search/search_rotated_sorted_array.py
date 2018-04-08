""" Problem statement:
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""


class Solution:
    def binary_search(self, array, start, end, target):
        """ Helper function for search function(below).
        Binary searches array from start to end, returns index of element
        equal to target of there's one, otherwise returns -1.
        Time complexity: O(lg(n)). Space complexity: O(1), n is len(array).
        """
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1  # target wasn't found

    def search(self, array, target):
        """ Returns index of target in sorted rotated array if it's present,
        return -1 otherwise.
        Algorithm is the following. Find the pivot(minimum element) using
        modified binary search, then decide which half of the array to
        binary search for target.
        Time complexity: O(lg(n)). Space complexity: O(1), n is len(array).
        """
        # special case, empty array
        if not array:
            return -1

        # find pivot, i.e. minimum element, using modified binary search
        n = len(array)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if array[mid - 1] > array[mid] < array[(mid + 1) % n]:
                break  # found it, pivot is at index mid
            elif array[mid] <= array[end]:
                end = mid - 1
            else:  # array[mid] >= array[start]
                start = mid + 1

        # decide in which half of the array to search
        if target <= array[-1]:  # search in right half
            return self.binary_search(array, mid, n - 1, target)
        else:  # search in left half
            return self.binary_search(array, 0, mid - 1, target)

    def search_one_pass(self, array, target):
        """ Returns index of target in sorted rotated array if it's present,
        return -1 otherwise. Algorithm does binary search in one pass.
        Time complexity: O(lg(n)). Space complexity: O(1), n is len(array).
        """
        # special case, empty array
        if not array:
            return -1

        # modified binary search
        n = len(array)
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == target:  # found the target
                return mid
            elif array[mid] <= array[end]:  # pivot is in the left half
                if array[mid] < target <= array[end]:  # target is in range (mid, last]
                    start = mid + 1  # search in right half
                else:
                    end = mid - 1  # search in left half
            else:  # array[mid] >= array[start], pivot is in the right half
                if array[start] <= target < array[mid]:  # target is in range [start, mid)
                    end = mid - 1  # search in left half
                else:
                    start = mid + 1  # search in right half
        return -1


if __name__ == "__main__":
    sol = Solution()
    func = sol.search_one_pass

    assert func([4, 5, 6, 7, 0, 1, 2], 4) == 0
    assert func([5, 6, 7, 8, 9, 10, 1, 2, 3], 3) == 8
    assert func([1, 2], 2) == 1
    assert func([2, 1], 2) == 0
    assert func([11], 11) == 0

    assert func([10, 12, 1, 4, 6, 8], 11) == -1
    assert func([10, 12, 1, 4, 6, 8], 2) == -1
    assert func([5, 6, 7, 8, 9, 10, 1, 2, 3], 11) == -1
    assert func([2], 1) == -1
    assert func([1, 2], 3) == -1
    assert func([2, 1], 3) == -1
