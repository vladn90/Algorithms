""" Problem description can be found here:
https://leetcode.com/problems/unique-paths/description/
"""
import random


class Solution:
    def display(self, matrix):
        """ Prints out 2D array.
        """
        for row in matrix:
            for el in row:
                print(str(el).rjust(2), end=" ")
            print()

    def unique_paths_rec(self, m, n):
        """ Recursive solution. Exponential running time, not efficient.
        """
        # base case
        if m == 1 or n == 1:
            return 1
        # recursive case
        return self.unique_paths(m - 1, n) + self.unique_paths(m, n - 1)

    def unique_paths_dp(self, m, n):
        """ Dynamic programming solution using 2-D array for storing results.
        Algorithm description:
        Number of unique paths to get to this X =
        number of paths to here from up + number of paths to here from left.
        If grid has only 1 row or 1 column, then there's only 1 unique path
        hence we start from the 2nd row, 2nd column.
        Time complexity: O(m * n). Space complexity: O(m * n).
        """
        results = [[1] * n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                results[i][j] = results[i - 1][j] + results[i][j - 1]
        return results[m - 1][n - 1]

    def unique_paths_dp_opt(self, m, n):
        """ Space optimized dynamic programming solution.
        Store only previous and current row for results.
        Time complexity: O(m * n). Space complexity: O(n).
        """
        prev = [1] * n
        curr = [1] * n
        for i in range(m - 1):  # number of rows to fill
            for j in range(1, n):  # current row
                curr[j] = curr[j - 1] + prev[j]
            prev, curr = curr, [1] * n
        return prev[-1]


if __name__ == "__main__":
    s = Solution()
    # stress testing regular dynamic programming solution and space-optimized
    while True:
        m, n = random.randrange(1, 10**2), random.randrange(1, 10**2)
        dp = s.unique_paths_dp(m, n)
        dp_opt = s.unique_paths_dp_opt(m, n)
        if dp == dp_opt:
            print("OK")
            print(dp)
        else:
            print("Different results.")
            print(f"m = {m}, n = {n}")
            print(f"regular result: {dp}")
            print(f"space optimized result: {dp_opt}")
            break
