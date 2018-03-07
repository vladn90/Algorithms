""" Problem description can be found here:
https://leetcode.com/problems/spiral-matrix/description/
Given a matrix of m x n elements,
return all elements of the matrix in spiral order.
For example, given the following matrix:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1, 2, 3, 6, 9, 8, 7, 4, 5].
"""


def spiral_order(matrix):
    result = []
    n = len(matrix) * len(matrix[0])
    right = len(matrix[0])
    left = -1
    bottom = len(matrix)
    top = 0
    i, j = 0, -1
    while len(result) < n:
        j += 1
        while j < right and len(result) < n:
            result.append(matrix[i][j])
            j += 1
        j -= 1
        right -= 1

        i += 1
        while i < bottom and len(result) < n:
            result.append(matrix[i][j])
            i += 1
        i -= 1
        bottom -= 1

        j -= 1
        while j > left and len(result) < n:
            result.append(matrix[i][j])
            j -= 1
        j += 1
        left += 1

        i -= 1
        while i > top and len(result) < n:
            result.append(matrix[i][j])
            i -= 1
        i += 1
        top += 1
    return result


def display_matrix(matrix):
    x = len(matrix) // 2
    for i in matrix:
        for j in i:
            print(str(j).rjust(3), end=" ")
        print()


if __name__ == "__main__":
    # 3 x 3 matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    display_matrix(matrix)
    result = spiral_order(matrix)
    assert result == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(f"result: {result}")
    print()

    # 5 x 5 matrix
    matrix = []
    for i in range(1, 26, 5):
        matrix.append(list(range(i, i + 5)))
    display_matrix(matrix)
    result = spiral_order(matrix)
    print(f"result: {result}")
    print()

    # 10 x 10 matrix
    matrix = []
    for i in range(1, 101, 10):
        matrix.append(list(range(i, i + 10)))
    display_matrix(matrix)
    result = spiral_order(matrix)
    print(f"result: {result}")
