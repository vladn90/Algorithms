""" Problem description can be found here:
https://www.interviewbit.com/problems/count-element-occurence/
"""


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def find_count_linear(self, array, target):
        """ Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        target_count = 0
        for num in array:
            if num == target:
                target_count += 1
            elif num > target:
                break
        return target_count

    def find_count_binary(self, array, target):
        """ Time complexity: O(lg(n)). Space complexity: O(1), n is len(array).
        """
        # find 1st occurence using binary search
        start, end = 0, len(array) - 1
        while start < end:
            mid = (start + end) // 2
            if array[mid] < target:
                start = mid + 1
            else:
                end = mid

        left = start
        if array[left] != target:  # target is not in the array
            return 0

        # find last occurence using binary search
        start, end = left, len(array) - 1
        while start < end:
            mid = (start + end + 1) // 2
            if array[mid] > target:
                end = mid - 1
            else:
                start = mid
        right = start
        return right - left + 1


if __name__ == "__main__":
    sol = Solution()
    array = [1, 1, 3, 3, 5, 5, 5, 9, 9, 11]
    target = 5
    print(sol.find_count_binary(array, target))
