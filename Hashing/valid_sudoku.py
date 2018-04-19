""" Problem statement:
https://www.interviewbit.com/problems/valid-sudoku/
"""


class Solution:
    def is_valid(self, board):
        """ Returns 1 if sudoku input board is valid, 0 otherwise.
        Time complexity: O(1). Space complexity: O(1).
        """
        if len(board) != 9:  # check number of rows in the input
            return 0

        digits = {'1', '4', '8', '2', '7', '6', '9', '3', '5'}
        for row in board:  # check each row
            if len(row) != 9:  # check number of characters in each row
                return 0
            curr = set()  # digits that we've already seen in current row
            for char in row:
                if char in digits and char not in curr:
                    curr.add(char)
                elif char == ".":
                    continue
                else:
                    return 0

        for i in range(9):  # check each column
            curr = set()  # digits that we've already seen in current column
            for row in board:
                if row[i] in digits and row[i] not in curr:
                    curr.add(row[i])
                elif row[i] == ".":
                    continue
                else:
                    return 0

        for i in range(0, 9, 3):  # check each 3 x 3 square
            for j in range(0, 9, 3):
                curr = set()
                for x in range(i, i + 3):  # square row
                    for y in range(j, j + 3):  # square column
                        char = board[x][y]
                        if char in digits and char not in curr:
                            curr.add(char)
                        elif char == ".":
                            continue
                        else:
                            return 0
        return 1


if __name__ == "__main__":
    sol = Solution()

    board = ["53..7....",
             "6..195...",
             ".98....6.",
             "8...6...3",
             "4..8.3..1",
             "7...2...6",
             ".6....28.",
             "...419..5",
             "....8..79"]

    print(sol.is_valid(board))
