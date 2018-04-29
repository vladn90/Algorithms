""" Problem statement:
https://leetcode.com/problems/valid-sudoku/description/
"""


class Solution:
    def isValidSudoku(self, board):
        """ Returns True if matrix represents valid sudoku board,
        False otherwise.
        """
        digits = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

        if len(board) != 9:  # sudoku board must have 9 rows
            return False
        for i in range(9):  # check each row
            if len(board[i]) != 9:  # each row must have 9 elements
                return False
            curr = set()  # digits in current row
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in digits and board[i][j] not in curr:
                    curr.add(board[i][j])
                else:
                    return False
        for j in range(9):  # check each column
            curr = set()  # digits in current column
            for i in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in digits and board[i][j] not in curr:
                    curr.add(board[i][j])
                else:
                    return False
        for x in range(0, 9, 3):  # check each 9x9 square
            for y in range(0, 9, 3):
                curr = set()  # digits in current 9x9 square
                for i in range(x, x + 3):
                    for j in range(y, y + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in digits and board[i][j] not in curr:
                            curr.add(board[i][j])
                        else:
                            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    func = sol.isValidSudoku

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(f"Is sudoku board valid? {func(board)}")

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(f"Is sudoku board valid? {func(board)}")
