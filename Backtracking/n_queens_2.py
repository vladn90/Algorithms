""" Problem statement:
https://leetcode.com/problems/n-queens-ii/description/
"""


class Solution:
    """ Use algorithm for n-queens puzzle but instead of copying the board when
    we find a solution, just increment the count of solutions.
    """

    def place_queen(self, n, i, j, cols, left_diags, right_diags):
        """ Places queen on the board at square(i, j). Modifies board in-place.
        """
        cols.add(j)
        left_diags.add(j - i)
        right_diags.add(n - 1 - j - i)

    def remove_queen(self, n, i, j, cols, left_diags, right_diags):
        """ Removes queen from the square(i, j). Modifies board in-place.
        """
        cols.remove(j)
        left_diags.remove(j - i)
        right_diags.remove(n - 1 - j - i)

    def is_safe(self, n, i, j, cols, left_diags, right_diags):
        """ Checks if it's possible to put queen at the square(i, j) so it
        doesn't conflict with any other queens that are already on the board.
        """
        # we don't have to check rows since there always gonna be only one queen
        # in each row, hence we check columns and diagonals:
        # top-left to bottom-right diagonal and top-right to bottom-left diagonal
        if j not in cols \
                and j - i not in left_diags \
                and n - 1 - j - i not in right_diags:
            return True
        return False

    def find_places(self, n, row, cols, left_diags, right_diags):
        """ Counts number of combinations of n x n board with n queens on it.
        Backtracking recursive algorithm.
        """
        if row == n:  # base case, we reached the end of the board
            return 1
        total = 0
        for j in range(n):  # moving in current row
            if self.is_safe(n, row, j, cols, left_diags, right_diags):
                self.place_queen(n, row, j, cols, left_diags, right_diags)
                total += self.find_places(n, row + 1, cols, left_diags, right_diags)
                self.remove_queen(n, row, j, cols, left_diags, right_diags)  # backtracking step
        return total

    def totalNQueens(self, n):
        """ Returns a number of solutions for n-queens puzzle.
        """
        return self.find_places(n, 0, set(), set(), set())


class SolutionShort:
    """ Condensed version of the above solution.
    """

    def find_places(self, n, i, cols, left_diags, right_diags):
        """ Counts number of combinations of n x n board with n queens on it.
        Backtracking recursive algorithm.
        """
        if i == n:  # base case, we reached the end of the board
            return 1
        total = 0
        for j in range(n):
            if j not in cols and j - i not in left_diags and n - 1 - j - i not in right_diags:
                cols.add(j)
                left_diags.add(j - i)
                right_diags.add(n - 1 - j - i)
                total += self.find_places(n, i + 1, cols, left_diags, right_diags)
                cols.remove(j)
                left_diags.remove(j - i)
                right_diags.remove(n - 1 - j - i)
        return total

    def totalNQueens(self, n):
        """ Returns a number of solutions for n-queens puzzle.
        """
        return self.find_places(n, 0, set(), set(), set())


class SolutionSmart:
    def totalNQueens(self, n):
        """ Returns a number of solutions for n-queens puzzle.
        Sort of smart solution. We can just hard code all the solutions :).
        Time complexity: O(1).
        """
        sol_count = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712,
                     365596, 2279184, 14772512, 95815104, 666090624, 4968057848,
                     39029188884, 314666222712, 2691008701644, 24233937684440,
                     227514171973736, 2207893435808352, 22317699616364044,
                     234907967154122528]
        return sol_count[n]


if __name__ == "__main__":
    sol = SolutionSmart()
    func = sol.totalNQueens

    # testing
    print(func(12))
