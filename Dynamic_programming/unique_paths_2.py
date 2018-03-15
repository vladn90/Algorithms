""" Problem description can be found here:
https://leetcode.com/problems/unique-paths-ii/description/
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

    def unique_paths_obstacles(self, grid):
        """ Dynamic programming solution.
        Time complexity: O(m * n). Space complexity: O(m * n), where
        m, n are dimensions of the grid.
        """
        # initializing 2-D array to store results
        n, m = len(grid), len(grid[0])
        results = [[0] * m for i in range(n)]

        # if there's obstacle in 1st row or 1st column, we won't be able
        # to cross it, i.e. set results[i][j] = 1 only before obstacle
        # checking obstacles in 1st row
        for j in range(m):
            if grid[0][j] == 1:
                break
            results[0][j] = 1
        # checking obstacle in 1st column
        for i in range(n):
            if grid[i][0] == 1:
                break
            results[i][0] = 1

        # fill out the rest of the results matrix
        for i in range(1, n):
            for j in range(1, m):
                # if current cell doesn't have an obstacle, then
                # number of paths to current cell =
                # number of paths from top + number of paths from left
                # otherwise, no paths to current cell is possible, leave 0
                if grid[i][j] != 1:
                    results[i][j] = results[i - 1][j] + results[i][j - 1]
        return results[n - 1][m - 1]


if __name__ == "__main__":
    s = Solution()
    # no obstacles
    grid1 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # obstacles in 1st row
    grid2 = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    # obstacles in 1st column
    grid3 = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    # random obstacles
    grid4 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    grid5 = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    # no paths, 1st or last cell has obstacle
    grid6 = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    grid7 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]

    grids = [grid1, grid2, grid3, grid4, grid5, grid6, grid7]
    results = [6, 3, 3, 2, 1, 0, 0]
    for i, g in enumerate(grids):
        assert s.unique_paths_obstacles(g) == results[i]
