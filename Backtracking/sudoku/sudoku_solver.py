""" Problem statement:
https://leetcode.com/problems/sudoku-solver/description/
https://www.interviewbit.com/problems/sudoku/
"""
from valid_sudoku import Solution as SolutionValid


sol_valid = SolutionValid()
is_valid = sol_valid.isValidSudoku


class Solution:
    def find_square(self, i, j):
        """ Returns a number of a square(0 - 8), in which cell(i, j) is located.
        """
        if 0 <= i <= 2:
            if 0 <= j <= 2:
                return 0
            elif 3 <= j <= 5:
                return 1
            else:
                return 2
        elif 3 <= i <= 5:
            if 0 <= j <= 2:
                return 3
            elif 3 <= j <= 5:
                return 4
            else:
                return 5
        else:
            if 0 <= j <= 2:
                return 6
            elif 3 <= j <= 5:
                return 7
            else:
                return 8

    def is_good(self, num, i, j, rows, cols, squares):
        """ Returns True if we can place num in cell(i, j), False otherwise.
        """
        if num in rows[i] or num in cols[j] or num in squares[self.find_square(i, j)]:
            return False
        return True

    def place_num(self, num, board, i, j, rows, cols, squares):
        """ Puts num on the board.
        """
        board[i][j] = num
        rows[i].add(num)
        cols[j].add(num)
        squares[self.find_square(i, j)].add(num)

    def remove_num(self, num, board, i, j, rows, cols, squares):
        """ Puts dot "." instead of num on the board.
        """
        board[i][j] = "."
        rows[i].remove(num)
        cols[j].remove(num)
        squares[self.find_square(i, j)].remove(num)

    def solve(self, board, i, j, rows, cols, squares):
        """ Solves sudoku using recursive backtracking algorithm.
        """
        if i == 9:  # base case, sudoku is solved
            return True

        if board[i][j] != ".":
            if j + 1 == 9:
                return self.solve(board, i + 1, 0, rows, cols, squares)
            else:
                return self.solve(board, i, j + 1, rows, cols, squares)

        for num in "123456789":
            if self.is_good(num, i, j, rows, cols, squares):
                self.place_num(num, board, i, j, rows, cols, squares)
                if j + 1 == 9:
                    result = self.solve(board, i + 1, 0, rows, cols, squares)
                else:
                    result = self.solve(board, i, j + 1, rows, cols, squares)
                if result:  # result == True, sudoku was solved
                    return True
                else:  # backtrack
                    self.remove_num(num, board, i, j, rows, cols, squares)
        return False  # base case wasn't triggered, hence sudoku wasn't solved

    def solveSudoku(self, board):
        """ Doesn't return anything. Modifies board in-place.
        """
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]
        # check the board and see what rows, columns and squares are filled
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[self.find_square(i, j)].add(board[i][j])
        self.solve(board, 0, 0, rows, cols, squares)


def display_board(board):
    """ Prints out sudoku board.
    """
    for row in board:
        for num in row:
            print(num, end=" ")
        print()


def main(func, board):
    print("-" * 17)
    display_board(board)
    func(board)
    assert is_valid(board) == True
    print("Sudoku is solved!")
    print()
    display_board(board)
    print("-" * 17)


if __name__ == "__main__":
    sol = Solution()
    func = sol.solveSudoku

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    main(func, board)

    board = [["7", ".", "2", "5", "3", ".", ".", "8", "."],
             [".", "1", "3", ".", ".", "7", ".", "6", "."],
             [".", ".", "4", "1", ".", ".", ".", ".", "9"],
             ["4", ".", "8", "6", ".", "1", ".", ".", "."],
             [".", "3", "7", ".", ".", ".", "1", "4", "."],
             [".", ".", ".", "3", ".", "4", "6", ".", "2"],
             ["3", ".", ".", ".", ".", "5", "8", ".", "."],
             [".", "4", ".", "2", ".", ".", "9", "1", "."],
             [".", "9", ".", ".", "1", "8", "3", ".", "4"]]
    main(func, board)
