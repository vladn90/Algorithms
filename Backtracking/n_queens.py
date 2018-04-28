""" Problem statement:
https://leetcode.com/problems/n-queens/description/
https://www.interviewbit.com/problems/nqueens/

Backtracking recursive algorithm. Idea is the following. We start with an empty
board. We traverse board(matrix) row by row, and in each row we do this:
1) We check if we can place the queen at current square, i.e. will it threaten
other queens at current column, row and diagonals.
2) If we can, we place it there, and move on to the next row.
3) If we can't, we just move on to the next square.
4) Now the interesting part is when we've placed queen in every row, i.e. we've
traversed the whole board, we just add a copy of this board to the result.
5) And then after we exit the current function, we backtrack, meaning that
we remove already placed queen from row i, then from row i - 1...etc.
6) And after that we move on to the next square and repeat all above.

So by doing this, we're doing exhaustive search and trying all possibilities
where we can place queen in current row, then in the next row and so on.

The function is_safe checks if we can place queen ar current square. To do that
we keep track of which columns already have queens, we number columns from
0 to n - 1, from left to right. And we divide diagonals into two groups:
1) top-left to bottom-right     2) top-right to bottom-left.
 0 1 2 3 4 ...                   ... 4 3 2 1 0
-1 \                                       /-1
-2  Q                                     Q -2
-3   \                                   /  -3
-4    Q                                 Q   -4
...    \                               /    ...
We use sets to keep track of which columns and diagonals already have queens.

Time complexity of the algorithm is O(n!).
"""


class Solution:
    def place_queen(self, board, n, i, j, cols, left_diags, right_diags):
        """ Places queen on the board at square(i, j). Modifies board in-place.
        """
        cols.add(j)
        left_diags.add(j - i)
        right_diags.add(n - 1 - j - i)
        board[i][j] = "Q"

    def remove_queen(self, board, n, i, j, cols, left_diags, right_diags):
        """ Removes queen from the square(i, j). Modifies board in-place.
        """
        cols.remove(j)
        left_diags.remove(j - i)
        right_diags.remove(n - 1 - j - i)
        board[i][j] = "."

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

    def find_places(self, board, n, row, result, cols, left_diags, right_diags):
        """ Finds all possible board n x n board combinations with n queens on it.
        Backtracking recursive algorithm.
        """
        if row == n:  # base case, we reached the end of the board
            result.append(list(map(("").join, board)))
            return
        for j in range(n):  # moving in current row
            if self.is_safe(n, row, j, cols, left_diags, right_diags):
                self.place_queen(board, n, row, j,
                                 cols, left_diags, right_diags)  # put queen at current square
                self.find_places(board, n, row + 1, result,
                                 cols, left_diags, right_diags)  # go to the next row
                self.remove_queen(board, n, row, j,
                                  cols, left_diags, right_diags)  # backtracking step

    def solveNQueens(self, n):
        """ Returns a list of boards, where each board represents a valid
        placement of n queens.
        """
        result = []
        # columns and diagonals that already have queen
        cols, left_diags, right_diags = set(), set(), set()
        board = [["."] * n for i in range(n)]  # empty n x n board
        self.find_places(board, n, 0, result, cols, left_diags, right_diags)
        return result


class SolutionShort:
    """ Short and optimized version of the above algorithm.
    """

    def find_places(self, board, n, i, result, cols, left_diags, right_diags):
        """ Finds all possible board n x n board combinations with n queens on it.
        Backtracking recursive algorithm.
        """
        if i == n:  # base case, we reached the end of the board
            result.append(list(map(("").join, board)))
            return
        for j in range(n):  # moving in current row
            if j not in cols and j - i not in left_diags and n - 1 - j - i not in right_diags:
                cols.add(j)
                left_diags.add(j - i)
                right_diags.add(n - 1 - j - i)
                board[i][j] = "Q"
                self.find_places(board, n, i + 1, result, cols, left_diags, right_diags)
                cols.remove(j)
                left_diags.remove(j - i)
                right_diags.remove(n - 1 - j - i)
                board[i][j] = "."

    def solveNQueens(self, n):
        """ Returns a list of boards, where each board represents a valid
        placement of n queens.
        """
        result = []
        self.find_places([["."] * n for i in range(n)], n, 0, result, set(), set(), set())
        return result


if __name__ == "__main__":
    sol = SolutionShort()
    func = sol.solveNQueens

    # testing
    result = func(4)
    for board in result:
        for row in board:
            for cell in row:
                print(cell.rjust(2), end=" ")
            print()
        print("-" * 20)
