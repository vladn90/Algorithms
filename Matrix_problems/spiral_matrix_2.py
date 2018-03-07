""" Problem description can be found here:
https://leetcode.com/problems/spiral-matrix-ii/description/
Given an integer n, generate a square matrix filled with elements
from 1 to n ^ 2 in spiral order.
For example, given n = 3, you should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


def generate_matrix(n):
    """ Returns a square matrix n x n with numbers in spiral order.
    Time complexity: O(n ^ 2). Space complexity: O(n ^ 2).
    """
    matrix = [[0] * n for i in range(n)]
    end_num = n ** 2
    right = n
    left = -1
    bottom = n
    top = 0
    i, j = 0, -1
    num = 1
    while num <= end_num:
        j += 1
        while j < right and num <= end_num:
            matrix[i][j] = num
            num += 1
            j += 1
        j -= 1
        right -= 1

        i += 1
        while i < bottom and num <= end_num:
            matrix[i][j] = num
            num += 1
            i += 1
        i -= 1
        bottom -= 1

        j -= 1
        while j > left and num <= end_num:
            matrix[i][j] = num
            num += 1
            j -= 1
        j += 1
        left += 1

        i -= 1
        while i > top and num <= end_num:
            matrix[i][j] = num
            num += 1
            i -= 1
        i += 1
        top += 1
    return matrix


def display_matrix(matrix):
    x = len(matrix) // 2
    just_width = len(str(matrix[x][x]))
    for i in matrix:
        for j in i:
            print(str(j).rjust(just_width), end=" ")
        print()


if __name__ == "__main__":
    # simple test
    for n in range(1, 21):
        print(f"matrix {n} x {n}:")
        matrix = generate_matrix(n)
        display_matrix(matrix)
        print()
