""" Problem statement:
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
"""
import math


class Solution:
    def eval_expr(self, a, b, op):
        """ Returns a result of evaluating an expression "a op b".
        input: a, b, op as strings
        Time complexity: O(1). Space complexity: O(1).
        """
        a, b = int(a), int(b)
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        else:  # operator == "/"
            return int(a / b)  # int(-6 / 4) != -6 // 4

    def evalRPN(self, tokens):
        """ Evaluates postfix expression from left to right.
        Time complexity: O(n). Space complexity: O(n), n is len(tokens).
        """
        stack = []
        for token in tokens:
            if token[-1].isdigit():  # current token is an operand
                stack.append(token)
            else:  # current token is an operator
                b = stack.pop()  # 2nd operand
                a = stack.pop()  # 1st operand
                res = self.eval_expr(a, b, token)
                stack.append(str(res))
        return int(stack.pop())  # pop the result from the stack


if __name__ == "__main__":
    sol = Solution()
    func = sol.evalRPN

    # tests
    assert func(["2", "1", "+", "3", "*"]) == 9
    assert func(["4", "13", "5", "/", "+"]) == 6
    assert func(["1", "2", "+"]) == 3
    assert func(["1", "3", "2", "*", "+"]) == 7
    assert func(["3", "2", "+", "5", "*"]) == 25
    assert func(["3", "4", "5", "*", "+", "6", "+"]) == 29
    assert func(["3", "4", "+", "5", "6", "+", "*"]) == 77
    assert func(["3", "4", "*", "5", "6", "*", "+"]) == 42
    assert func(["3", "4", "+", "5", "+", "6", "+"]) == 18
    assert func(["-6", "4", "/"]) == -1
