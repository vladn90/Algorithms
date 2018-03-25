""" Problems description can be found here:
https://leetcode.com/problems/pascals-triangle/description/
https://leetcode.com/problems/pascals-triangle-ii/description/
"""


class Solution:
    def display(self, triangle):
        """ Prints out a Pascal's triangle.
        """
        for t in triangle:
            print(str(t).center(len(str(triangle[-1]))))

    def generate(self, num_rows):
        """ Returns a Pascal's triangle with num_rows rows.
        """
        # initialize a triangle with all cells equal to 1
        triangle = [[1] * (i + 1) for i in range(num_rows)]
        # loop over every row starting from the 2nd
        for i in range(1, num_rows):
            curr_len = len(triangle[i])  # current row length
            # loop over from the 2nd to one before last number in row
            for j in range(1, curr_len - 1):
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        return triangle

    def k_row(self, k_row):
        """ Returns k-th row of Pascal's triangle. Row numbers start from 0.
        """
        curr_row = [1]  # 0th row
        for row in range(1, k_row + 1):
            next_row = [1] * (len(curr_row) + 1)
            n = len(next_row)
            for j in range(1, n - 1):
                next_row[j] = curr_row[j - 1] + curr_row[j]
            curr_row = next_row
        return curr_row


if __name__ == "__main__":
    sol = Solution()
    n = 10
    triangle = sol.generate(11)
    sol.display(triangle)
    print()

    print(f"{n}th row of Pascal's triangle is:")
    print(sol.k_row(n))
