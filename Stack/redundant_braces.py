""" Problem statement:
https://www.interviewbit.com/problems/redundant-braces/
"""


class Solution:
    # @param expr : string
    # @return an integer
    def is_redundant(self, expr):
        """ Returns 1 if expr has redundant braces, 0 otherwise.
        Time complexity: O(n). Space complexity: O(n), n is len(expr).
        """
        stack = []  # brackets' stack
        operators = {"+", "-", "*", "/"}
        for char in expr:
            if char == "(":  # push current bracket to the stack
                stack.append(False)  # since we don't know yet if there's an operator
            elif char in operators:
                if not stack:  # no brackets on the stack, just skip it
                    continue
                stack[-1] = True  # found an operator, so last brackets on the stack are valid
            elif char == ")":
                if stack[-1]:  # if the last brackets are valid
                    stack.pop()  # take them off the stack
                else:  # last brackets didn't have an operator inside
                    return 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    func = sol.is_redundant

    assert func("(a)") == 1
    assert func("a") == 0
    assert func("a+b") == 0
    assert func("((a+b))") == 1
    assert func("(a+(a+b))") == 0
    assert func("((a+b)+(c+d))") == 0
    assert func("((a+d)+(c+d)+(a+b))+x") == 0
    assert func("(((a+d)+(c+d)+(a+b)))") == 1
