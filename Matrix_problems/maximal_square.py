""" Problem statement:
https://leetcode.com/problems/maximal-square/description/

Dynamic programming solution.
While traversing the matrix, keep track of the maximum side of the square
that's gonna end at matrix[i][j]. Square can end at this cell only if:
1) matrix[i][j] == 1
2) matrix[i - 1][j] > 0, matrix[i][j - 1] > 0, matrix[i - 1][j - 1] > 0
If the above conditions are met, then matrix[i][j] will be the minimum
of mentioned above neighboring cells plus 1, i.e.
matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1.
After finding the maximum side, return area = side ^ 2.

Space complexity is gonna be O(n * m) since we're usign matrix itself
as auxiliary matrix, and we change "boolean" values("1", "0") to 32-bit integers,
hence we increase the size of the matrix.
"""


class Solution:
    def maximalSquare(self, matrix):
        """ Time complexity: O(n * m). Space complexity: O(m * n),
        n, m are dimensions of the matrix.
        """
        if not matrix or not matrix[0]:
            return 0

        # convert 1st row and 1st column to integers
        side = 0  # use OR to set initial side to 1 if there's 1 in 1st row or column
        for i in range(len(matrix[0])):
            matrix[0][i] = int(matrix[0][i])
            side |= matrix[0][i]
        for i in range(len(matrix)):
            matrix[i][0] = int(matrix[i][0])
            side |= matrix[i][0]

        # traverse the matrix and find a side of the largest square
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])  # convert current cell to int
                if matrix[i][j]:  # if current cell != 0
                    matrix[i][j] += min(matrix[i - 1][j],
                                        matrix[i][j - 1],
                                        matrix[i - 1][j - 1])
                    if matrix[i][j] > side:  # side = max(side, matrix[i][j])
                        side = matrix[i][j]
        return side * side  # return area of a square


if __name__ == "__main__":
    sol = Solution()
    func = sol.maximalSquare

    assert func([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
                 ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]) == 4
    assert func([]) == 0
    assert func([[]]) == 0
    assert func([["0"]]) == 0
    assert func([["1"]]) == 1
    assert func([["1", "1"], ["1", "1"], ["1", "1"]]) == 4
    assert func([["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]) == 0
