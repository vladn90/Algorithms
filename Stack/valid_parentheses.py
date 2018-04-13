""" Problem statement:
https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, string):
        """ Returns True if parentheses in string are valid, False otherwise.
        Time complexity: O(n). Space complexity: O(1), n is len(string).
        """
        brackets = {")": "(", "]": "[", "}": "{"}
        open = {"(", "[", "{"}
        closed = {")", "]", "}"}
        stack = []
        for char in string:  # loop over string, push opening brackets to the stack
            if char in open:
                stack.append(char)
            elif char in closed:
                if not stack or stack[-1] != brackets[char]:  # stack is empty
                    return False
                stack.pop()  # remove opening bracket from the stack
        return not stack  # stack should be empty
