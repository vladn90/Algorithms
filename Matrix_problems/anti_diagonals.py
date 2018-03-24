""" Problem description can be found here:
https://www.interviewbit.com/problems/anti-diagonals/
"""


class Solution:
    def display(self, matrix):
        """ Prints out 2-D matrix.
        """
        for row in matrix:
            for num in row:
                print(num, end=" ")
            print()

    def anti_diagonals(self, matrix):
        """ Returns a new matrix(array of arrays) consisting of anti diagonals.
        Time complexity: O(n ^ n). Space complexity: O(n).
        """
        n = len(matrix)
        result = []
        # 1st half of the matrix
        for j in range(n):  # loop over 1st row starting from the 1st num
            curr = []
            i = 0
            while i < n and j > -1:  # loop in opposite diagonal direction
                curr.append(matrix[i][j])
                i += 1
                j -= 1
            result.append(curr)
        # 2nd half
        for i in range(1, n):  # loop over right side starting from the 2nd num
            curr = []
            j = n - 1
            while i < n and j > -1:  # loop in opposite diagonal direction
                curr.append(matrix[i][j])
                i += 1
                j -= 1
            result.append(curr)
        return result


if __name__ == "__main__":
    sol = Solution()

    # test 1
    print("original matrix")
    matrix = [[1]]
    sol.display(matrix)
    print("modified matrix")
    result = sol.anti_diagonals(matrix)
    for arr in result:
        print(arr)

    # test 2
    print("original matrix")
    matrix = [[1, 2], [3, 4]]
    sol.display(matrix)
    print("modified matrix")
    result = sol.anti_diagonals(matrix)
    for arr in result:
        print(arr)

    # test 3
    print("original matrix")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.display(matrix)
    print("modified matrix")
    result = sol.anti_diagonals(matrix)
    for arr in result:
        print(arr)
