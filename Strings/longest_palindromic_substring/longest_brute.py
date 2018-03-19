""" Problem description can be found here:
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, find the longest palindromic substring in s.
"""


class Solution:
    def is_palindrome(self, string, i, j):
        """ Returns True if string from index i to index j is a palindrome,
        False otherwise.
        Time complexity: O(n). Space complexity: O(1),
        where is the length of the string[i:j].
        """
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True

    def longest_palindrome(self, string):
        """ Brute force algorithm. Algorithm description:
        1) Look over at all possible substrings with length >= 2.
        2) Check if current substring is a palindrome.
        3) Choose the longest one or in case the lengths are equal
        the one that comes first.
        4) Stop the loop if it's not possible to make longer substring from
        the left over characters than the one we already found.

        Time complexity: O(n ^ 3). Space complexity: O(1),
        where n is the length of the string.
        """
        # start and end index of current longest palindromic substring
        a, b = 0, 0
        n = len(string)
        for i in range(n - 1):
            # it's not possible to find longer substring than already found
            if i > n - (b - a + 1):
                break
            # check if current substring is a palindrome
            # and if it's longer than already found palindromic substring
            for j in range(i + 1, n):
                if self.is_palindrome(string, i, j) and (j - i) > (b - a):
                    a, b = i, j
        return string[a:b + 1]


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
