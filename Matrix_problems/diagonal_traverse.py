""" Problem description can be found here:
https://leetcode.com/problems/diagonal-traverse/description/

Algorithm description.
An observation. We always start moving in upwards diagonal direction from the
left or bottom of the matrix. And likewise we start moving in downwards
diagonal direction from top or right of the matrix.
That's why we need to keep track of direction we're currently moving in,
and update starting point for the next move in this direction.
"""


class Solution:
    def display(self, matrix):
        for row in matrix:
            for el in row:
                print(str(el).rjust(2), end=" ")
            print()

    def flatten(self, matrix, n, m):
        """ Flattens the matrix and returns an array.
        """
        result = []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                result.append(matrix[i][j])
        return result

    def findDiagonalOrder(self, matrix):
        """ Returns a new array.
        """
        # special case, empty array
        if not matrix:
            return []

        n, m = len(matrix), len(matrix[0])
        # special case, matrix has 1 row or less or 1 column or less
        if n <= 1 or m <= 1:
            return self.flatten(matrix, n, m)

        result = []  # resulting array
        up = True  # current direction
        up_i, up_j = 0, 0  # starting point for moving upwards
        down_i, down_j = 0, 1  # starting point for moving downwards
        max_steps = n * m
        steps = 0

        while steps < max_steps:
            if up:  # moving upwards
                i, j = up_i, up_j
                while i > -1 and j < m:
                    result.append(matrix[i][j])
                    steps += 1
                    i -= 1
                    j += 1
                # set new coordinates for the next move in upwards direction
                if up_i == n - 1:
                    up_j += 2
                elif up_i + 2 <= n - 1:
                    up_i += 2
                else:  # up_i + 2 > n - 1:
                    up_i += 1
                    up_j += 1

            else:  # moving downwards
                i, j = down_i, down_j
                while i < n and j > -1:
                    result.append(matrix[i][j])
                    steps += 1
                    i += 1
                    j -= 1
                # set new coordinates for the next move in downwards direction
                if down_j == m - 1:
                    down_i += 2
                elif down_j + 2 <= m - 1:
                    down_j += 2
                else:
                    down_j += 1
                    down_i += 1
            up = not up  # change direction

        return result


if __name__ == "__main__":
    sol = Solution()

    # square matrices
    matrix = [[1, 2], [3, 4]]
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

    # different matrices
    matrix = [[1, 2, 3]]
    matrix = [[1], [2], [3]]
    matrix = [[1, 2], [3, 4], [5, 6]]

    sol.display(matrix)
    print(sol.findDiagonalOrder(matrix))
