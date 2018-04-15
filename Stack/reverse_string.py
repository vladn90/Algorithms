class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, string):
        """ Reverses a string using stack.
        Time complexity: O(n). Space complexity: O(n), n is len(string).
        """
        # push character to the stack
        stack = []
        for char in string:
            stack.append(char)

        # pop characters from the stack
        rev = []
        while stack:
            rev.append(stack.pop())
        return "".join(rev)
