""" Problem statement:
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""


class Solution:
    def find_min(self, array):
        """ Returns minimum element in a sorted rotated array.
        Works only for array with unique elements.
        Time complexity: O(lg(n)). Space complexity: O(1), n is len(array).
        """
        n = len(array)
        start, end = 0, n - 1
        # special case, array hasn't been rotated or it has only 1 element
        if array[start] <= array[end]:
            return array[start]

        # binary search
        while start <= end:
            mid = (start + end) // 2
            if array[mid - 1] > array[mid] < array[(mid + 1) % n]:
                return array[mid]
            elif array[mid] <= array[end]:
                end = mid - 1
            else:
                start = mid + 1


if __name__ == "__main__":
    sol = Solution()
    func = sol.find_min

    assert func([1, 2, 3, 4, 5]) == 1
    assert func([2, 3, 4, 5, 1]) == 1
    assert func([3, 4, 5, 1, 2]) == 1
    assert func([2, 1]) == 1
    assert func([1, 2]) == 1
    assert func([1]) == 1
