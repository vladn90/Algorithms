""" Problem description can be found here:
https://leetcode.com/problems/search-a-2d-matrix/description/
Write an efficient algorithm that searches for a value in an m x n matrix.
The integers in matrix row are sorted in non-descending order,
and integers in matrix columns are sorted in non-descending order, i.e.
1st integer of the row is the smallest in the row, the last one is the largest;
1st integer of the column is the smallest in the column,
the last one is the largest.
"""


def search_matrix_brute(matrix, value):
    """ Returns True if value is in the matrix, False otherwise.
    Brute force algorithm.
    Time complexity: O(n * m). Space complexity: O(1),
    where m and n are length and height of the matrix.
    """
    for row in matrix:
        for element in row:
            if element == value:
                return True
    return False


def search_matrix_binary(matrix, value):
    """ Returns True if value is in the matrix, False otherwise.
    Binary search algorithm. Algorithm description:
    1) Move diagonally from top left corner to bottom right.
    2) Binary search each row and column along the way.

    Time complexity: O(m * lg(n) + n * lg(m)). Space complexity: O(1),
    where m and n are length and height of the matrix.
    """
    # special case, empty array
    if not matrix:
        return False

    m, n = len(matrix[0]), len(matrix)
    i, j = 0, 0
    while i < n and j < m:

        # binary search in a row
        start, end = 0, m - 1
        while start <= end:
            mid = (start + end) // 2
            # found the number
            if matrix[i][mid] == value:
                return True
            # search in left half
            elif matrix[i][mid] > value:
                end = mid - 1
            # search in right half
            else:
                start = mid + 1

        # binary search in a column
        start, end = 0, n - 1
        while start <= end:
            mid = (start + end) // 2
            # found the number
            if matrix[mid][j] == value:
                return True
            # search in top half
            elif matrix[mid][j] > value:
                end = mid - 1
            # search in bottom half
            else:
                start = mid + 1

        i += 1
        j += 1
    return False


def search_matrix_fast(matrix, value):
    """ Returns True if value is in the matrix, False otherwise.
    Diagonal search fast algorithm.
    ALgorithm description:
    1) Move diagonally from top right to bottom left corner.
    2) Compare value with starting and ending element in each row or column.
    3) If element is larger or smaller than the largest or smallest element
    in current row or column, then we can completely eliminate that
    row or column.

    Time complexity: O(m + n). Space complexity: O(1),
    where m and n are length and height of the matrix.
    """
    # special case, empty array
    if not matrix:
        return False

    i, j = 0, len(matrix[0]) - 1
    while i < len(matrix) and j > -1:
        # found element
        if value == matrix[i][j]:
            return True
        # check row
        if value < matrix[i][0] or value > matrix[i][j]:
            i += 1
        # check column
        elif value < matrix[i][j] or value > matrix[len(matrix) - 1][j]:
            j -= 1
    return False


if __name__ == "__main__":
    # simple test
    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    functions = [search_matrix_brute, search_matrix_binary, search_matrix_fast]
    for func in functions:
        assert func(matrix, 23) == True
        assert func(matrix, 21) == False
        assert func([], 99) == False
