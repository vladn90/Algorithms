""" Problem description can be found here:
https://leetcode.com/problems/decode-string/description/
"""


class Solution:
    def decodeString(self, string):
        """ Returns decoded string.
        Time complexity: O(n). Space complexity: O(n), where n is len(string).
        """
        stack = []
        curr_string = ""
        curr_num = 0
        for char in string:
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
            elif char == "[":
                stack.append(curr_string)
                stack.append(curr_num)
                curr_string = ""
                curr_num = 0
            elif char == "]":
                curr_num = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + curr_num * curr_string
                curr_num = 0
            else:  # character is alphabetic
                curr_string += char
        return curr_string


if __name__ == "__main__":
    sol = Solution()

    # tests
    assert sol.decodeString("") == ""
    assert sol.decodeString("0[abc]") == ""
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
    assert sol.decodeString("3[a2[c]]") == "accaccacc"
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert sol.decodeString("11[a2[d]]") == "addaddaddaddaddaddaddaddaddaddadd"
    assert sol.decodeString("1[a1[b1[c1[d]]]]") == "abcd"
