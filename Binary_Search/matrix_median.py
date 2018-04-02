""" Problem description can be found here:
https://www.interviewbit.com/problems/matrix-median/
"""


class Solution:
    def matrix_median_brute(self, matrix):
        """ Returns matrix median. Brute force algorithm.
        Time complexity: O(n * m * lg(n * m)). Space complexity: O(n * m),
        where n, m are matrix dimensions.
        """
        # flatten the matrix
        array = []
        for row in matrix:
            for num in row:
                array.append(num)
        # sort the array and find the median
        array.sort()
        return array[len(array) // 2]

    def binary_search_count(self, array, target):
        """ Returns number of elements <= target in sorted array.
        Time complexity: O(lg(n)). Space complexity: O(1), n is len(array).
        """
        # special case
        if target < array[0]:  # target is less than min element
            return 0

        n = len(array)
        start, end = 0, n - 1
        while start < end:
            mid = (start + end + 1) // 2
            if target < array[mid]:
                end = mid - 1
            else:
                start = mid
        return start + 1

    def count_target(self, matrix, target):
        """ Returns number of elements <= target in matrix.
        Time complexity: O(n * lg(m)). Space complexity: O(1),
        n, m are dimensions of the matrix.
        """
        total = 0
        for arr in matrix:
            total += self.binary_search_count(arr, target)
        return total

    def matrix_median(self, matrix):
        """ Returns matrix median.
        Time complexity: O(n * lg(m)). Space complexity: O(1),
        n, m are dimensions of the matrix.
        """
        n, m = len(matrix), len(matrix[0])
        # find min and max element in matrix
        min_num, max_num = float("inf"), float("-inf")
        for row in matrix:
            min_num = min(min_num, row[0])  # compare 1st element of each row
            max_num = max(max_num, row[-1])  # compare last element of each row

        goal = (n * m) // 2 + 1  # min count of <= elements for element to be median
        # find matrix median using binary search between min_num and max_num
        while min_num < max_num:
            mid = (min_num + max_num) // 2
            # mid = min_num + (max_num - min_num) // 2
            curr_count = self.count_target(matrix, mid)
            if curr_count < goal:
                min_num = mid + 1
            else:  # curr_count >= goal
                max_num = mid  # update the upper limit for median number
        return min_num


if __name__ == "__main__":
    sol = Solution()
    func = sol.matrix_median

    # tests
    assert func([[1]]) == 1
    assert func([[1], [2], [33]]) == 2
    assert func([[1, 2, 3, 44, 555]]) == 3
    assert func([[1, 1, 1], [1, 2, 3], [3, 3, 3]]) == 2
    assert func([[1, 10, 11], [4, 22, 30], [30, 300, 333]]) == 22
    assert func([[1, 3, 4], [2, 5, 6], [7, 8, 9]]) == 5
    assert func([[1, 3, 5], [2, 6, 9], [3, 6, 9]]) == 5
    assert func([[1, 5, 7], [4, 10, 11], [8, 11, 12]]) == 8
    assert func([[1, 3, 6], [6, 6, 9], [3, 6, 9]]) == 6
    assert func([[1, 3, 6], [6, 6, 9], [3, 6, 9]]) == 6
