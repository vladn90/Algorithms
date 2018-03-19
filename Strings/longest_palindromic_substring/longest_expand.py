""" Problem description can be found here:
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, find the longest palindromic substring in s.
"""


class Solution:
    def expand(self, string, i, j):
        """ Returns start, end indices of longest palindromic substring
        expanded from i, j.
        """
        n = len(string)
        while i >= 0 and j < n and string[i] == string[j]:
            i -= 1
            j += 1
        return i + 1, j - 1

    def longest_palindrome(self, string):
        """ Algorithm is based on idea to expand palindrome from the center.
        Algorithm description:
        1) Choose a 1-letter or 2-letter center in the string.
        2) Keep decreasing left index i and increasing right index j, while
        substring is a palindrome and while we're in the boundaries of string.

        Time complexity: O(n ^ 2). Space complexity: O(1), where
        n is the length of the string.
        """
        n = len(string)
        x, y = 0, 0  # start, end of the longest palindromic substring so far
        for i in range(n - 1):
            res1 = self.expand(string, i, i)  # 1-letter center
            res2 = self.expand(string, i, i + 1)  # 2-letter center

            # compare the length of two results with current length
            length_1 = res1[1] - res1[0]
            length_2 = res2[1] - res2[0]
            if length_1 > y - x:
                x, y = res1
            if length_2 > y - x:
                x, y = res2

        return string[x:y + 1]


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
