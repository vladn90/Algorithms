""" Problem description can be found here:
https://leetcode.com/problems/longest-palindromic-substring/description/
Given a string s, find the longest palindromic substring in s.

Very detailed description of Manacher's algorithm can be found here:
https://articles.leetcode.com/longest-palindromic-substring-part-ii/
This implementation is based on that description.
"""


class Solution:
    def longest_palindrome(self, string):
        """ Manacher's Algorithm.
        Time complexity: O(n). Space complexity: O(n), where n is len(string).
        """
        # preprocess string, i.e. "aba" > "^#a#b#a#$"
        new_str = ["^"]
        for char in string:
            new_str.append("#")
            new_str.append(char)
        new_str.append("#")
        new_str.append("$")

        n = len(new_str)
        # each result[i] = length of the longest palindrome centered at i
        result = [0] * n
        centre, right = 0, 0
        for i in range(1, n - 1):
            mirror = centre - (i - centre)  # mirrored index of index i
            if i < right:
                result[i] = min(right - i, result[mirror])
            # try to expand palindrome centered at index i
            while new_str[i - result[i] - 1] == new_str[i + result[i] + 1]:
                result[i] += 1
            # adjust the centre and the right edge if needed
            if result[i] > right - i:
                centre = i
                right = i + result[i]

        # find the longest palindrome
        max_index, max_len = 0, 0
        for i, num in enumerate(result):
            if num > max_len:
                max_index, max_len = i, num
        start = (max_index - 1 - max_len) // 2
        end = start + max_len
        return string[start:end]


if __name__ == "__main__":
    sol = Solution()
    # simple tests
    assert sol.longest_palindrome("babad") == "bab"
    assert sol.longest_palindrome("abacdfgdcaba") == "aba"
    assert sol.longest_palindrome("ababa") == "ababa"
    assert sol.longest_palindrome("abcddabc") == "dd"
    assert sol.longest_palindrome("a") == "a"
    assert sol.longest_palindrome("aa") == "aa"
    assert sol.longest_palindrome("baaaa") == "aaaa"
    assert sol.longest_palindrome("") == ""
