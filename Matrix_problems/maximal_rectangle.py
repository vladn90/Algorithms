""" Problem statement:
https://leetcode.com/problems/maximal-rectangle/description/

Problem can be boiled down to solving Largest Rectangle in Histogram problem:
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""


class Solution:
    def largest_rectangle(self, array):
        """ Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        array.append(0)  # add dummy height to the end
        stack = [-1]
        max_area = 0
        for i, curr in enumerate(array):
            while array[stack[-1]] > curr:
                width = (i - stack[-2] - 1)
                height = array[stack.pop()]
                area = width * height
                max_area = max(max_area, area)
            stack.append(i)
        array.pop()  # remove dummy height
        return max_area

    def maximalRectangle(self, matrix):
        """ Time complexity: O(n * m). Space complexity: O(n),
        n, m are number of rows and columns in the matrix.
        """
        if not matrix or not matrix[0]:  # special case, empty matrix
            return 0

        n, m = len(matrix), len(matrix[0])
        # modify matrix, every next row += prev row if value != 0
        for j in range(m):  # modify 1st row
            matrix[0][j] = int(matrix[0][j])
        for i in range(1, n):  # rest of the matrix, start from the 2nd row
            for j in range(m):
                if matrix[i][j] == "1":
                    matrix[i][j] = int(matrix[i][j]) + matrix[i - 1][j]
                else:
                    matrix[i][j] = int(matrix[i][j])
        # solve every row of modified matrix as Largest Rectangle in Histogram
        max_area = 0
        for i in range(n):
            max_area = max(max_area, self.largest_rectangle(matrix[i]))
        return max_area


class SolutionOptimized:
    def largest_rectangle(self, array):
        """ Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        array.append(0)  # add dummy height to the end
        stack = [-1]
        max_area = 0
        for i, curr in enumerate(array):
            while array[stack[-1]] > curr:
                height = array[stack.pop()]
                area = (i - stack[-1] - 1) * height
                if area > max_area:
                    max_area = area
            stack.append(i)
        array.pop()  # remove dummy height
        return max_area

    def maximalRectangle(self, matrix):
        """ Time complexity: O(n * m). Space complexity: O(n),
        n, m are number of rows and columns in the matrix.
        """
        if not matrix or not matrix[0]:  # special case, empty matrix
            return 0

        # modify matrix, every next row += prev row if value != 0
        for j in range(len(matrix[0])):  # modify 1st row
            matrix[0][j] = int(matrix[0][j])
        for i in range(1, len(matrix)):  # rest of the matrix, start from the 2nd row
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i - 1][j]
        # solve every row of modified matrix as Largest Rectangle in Histogram
        max_area = 0
        for i in range(len(matrix)):
            max_area = max(max_area, self.largest_rectangle(matrix[i]))
        return max_area


if __name__ == "__main__":
    sol = Solution()

    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    print(sol.maximalRectangle(matrix))
