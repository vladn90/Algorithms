""" Problem description can be found here:
https://leetcode.com/problems/rotate-image/description/

You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise) using constant space.

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""
import random
import copy


def build_matrix(n):
    """ Returns a square matrix n x n.
    """
    matrix = [[0] * n for i in range(n)]
    x = 1
    for i in range(n):
        for j in range(n):
            matrix[i][j] = x
            x += 1
    return matrix


def display_matrix(matrix):
    """ Prints out matrix to the console.
    """
    for row in matrix:
        for value in row:
            print(str(value).rjust(2), end=" ")
        print()


def rotate_matrix_1(matrix):
    """ Rotates square matrix clockwise.
    Time complexity: O(n ^ 2). Space complexity: O(n ^ 2).
    """
    n = len(matrix)
    rotated_matrix = [[0] * n for i in range(n)]
    for j in range(n):
        for i in range(n - 1, -1, -1):
            rotated_matrix[j][n - i - 1] = matrix[i][j]
    return rotated_matrix


def flip_array(array):
    """ Flips array in-place.
    Time complexity: O(n). Space complexity: O(1).
    """
    n = len(array)
    i, j = 0, n - 1
    while i < j:
        array[i], array[j] = array[j], array[i]
        i += 1
        j -= 1


def rotate_matrix_2(matrix):
    """ Rotates square matrix clockwise in-place.
    Time complexity: O(n ^ 2). Space complexity: O(1).
    """
    n = len(matrix)
    # swap elements starting from the last in each row and column,
    # start from the 1st column and 1st row
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # mirror the matrix, i.e. flip each row in matrix
    for i in range(n):
        flip_array(matrix[i])


if __name__ == "__main__":
    # stress testing O(n) space algorithm against O(1) space algorithm
    while True:
        n = 4
        matrix = [[random.randrange(1, 10) for j in range(n)]
                  for i in range(n)]
        original_matrix = copy.deepcopy(matrix)

        rotated_1 = rotate_matrix_1(matrix)

        rotate_matrix_2(matrix)
        rotated_2 = matrix

        if rotated_1 == rotated_2:
            print("OK")
            print(matrix[0])
        else:
            print("Results are different.")
            print(f"original matrix: {original_matrix}")
            print(f"result 1: {rotated_1}")
            print(f"result 2: {rotated_2}")
            break
