""" Problem description can be found here:
https://leetcode.com/problems/set-matrix-zeroes/description/
Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in place using constant space.
"""
import copy
import random


def display(matrix):
    for row in matrix:
        for element in row:
            print(str(element).rjust(2), end=" ")
        print()


def setZeroes_1(matrix):
    """ Doesn't return anything. Modifies matrix in-place.
    Time complexity: O(n * m). Space complexity: O(m),
    where n and m are height and length of the matrix.
    """
    columns = set()
    n, m = len(matrix), len(matrix[0])
    zero_row = [0] * m
    for i in range(n):
        set_row_zero = False  # current row have zeroes
        for j in range(m):
            if matrix[i][j] == 0:
                set_row_zero = True
                columns.add(j)
        # set whole row to zeroes
        if set_row_zero:
            matrix[i] = zero_row
    # set column j to zeroes
    for j in columns:
        for i in range(n):
            matrix[i][j] = 0


def setZeroes_2(matrix):
    """ Doesn't return anything. Modifies matrix in-place.
    Time complexity: O(n * m). Space complexity: O(1),
    where n and m are height and length of the matrix.

    Uses 1st column and 1st row as auxiliary arrays to remember which
    rows and columns must be set to zeroes.
    """
    n, m = len(matrix), len(matrix[0])

    # check if we should set first row to zeroes
    first_row_zero = False
    for j in range(m):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # check if we should set first column to zeroes
    first_column_zero = False
    for i in range(n):
        if matrix[i][0] == 0:
            first_column_zero = True
            break

    # use 1st column and 1st row as auxiliary arrays
    for i in range(1, n):
        for j in range(1, m):
            # all elements in row i and column j should be set to zeroes
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # set rows to zeroes
    for i in range(1, n):
        if matrix[i][0] == 0:
            for j in range(1, m):
                matrix[i][j] = 0

    # set columns to zeroes
    for j in range(1, m):
        if matrix[0][j] == 0:
            for i in range(1, n):
                matrix[i][j] = 0

    # set 1st row and 1st column to zeroes if needed
    if first_row_zero:
        for j in range(m):
            matrix[0][j] = 0
    if first_column_zero:
        for i in range(n):
            matrix[i][0] = 0


if __name__ == "__main__":
    n, m = 100, 100
    # stress testing different solutions against each other
    while True:
        matrix = [[random.randrange(0, 100) for j in range(m)] for i in range(n)]
        matrix1 = copy.deepcopy(matrix)
        matrix2 = copy.deepcopy(matrix)
        setZeroes_1(matrix1)
        setZeroes_2(matrix2)
        if matrix1 == matrix2:
            print("OK")
            display(matrix1)
        else:
            print("Results are different.")
            print("-" * 30)
            print(f"initial matrix:")
            display(matrix)
            print("-" * 30)
            print(f"result 1:")
            print("-" * 30)
            display(matrix1)
            print("-" * 30)
            print(f"result 2:")
            print("-" * 30)
            display(matrix2)
            print("-" * 30)
