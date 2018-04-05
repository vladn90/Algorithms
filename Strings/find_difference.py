""" Problem statement:
https://leetcode.com/problems/find-the-difference/description/
"""
import random
from collections import Counter


class Solution:
    def find_diff_1(self, s, t):
        """ Sort the strings and find first different letter.
        Time complexity: O(n * lg(n)). Space complexity: O(n), n is len(s).
        """
        s, t = sorted(s), sorted(t)
        n = len(s)
        for i in range(n):
            if s[i] != t[i]:  # compare current letters
                return t[i]
        # all letters up to the last one were equal,
        # then the last letter is the one we're looking for
        return t[-1]

    def find_diff_2(self, s, t):
        """ Use hash map to count the characters in string s, then compare it
        with characters in string t.
        Time complexity: O(n). Space complexity: O(n), n is len(s).
        """
        char_count = Counter(s)
        for char in t:
            if not char_count[char] or char not in char_count:
                return char
            char_count[char] -= 1

    def find_diff_3(self, s, t):
        """ XOR all ord value of letters of both strings, the value left after
        all XOR operations would be the ord of letter we're looking for.
        """
        value = 0
        n = len(s)
        for i in range(n):
            value = value ^ ord(s[i]) ^ ord(t[i])
        value ^= ord(t[-1])  # XOR extra letter from t
        return chr(value)


if __name__ == "__main__":
    sol = Solution()
    func = sol.find_diff_3

    # simple test
    s = "babc"
    t = "baebc"
    assert func(s, t) == "e"

    while True:  # test stress func
        s = [chr(random.randrange(97, 123)) for i in range(10)]
        char = chr(random.randrange(97, 123))
        t = s[:] + [char]
        random.shuffle(t)
        assert func(s, t) == char
        print("OK")
        print(f"{''.join(s)}")
        print(f"{''.join(t)}")
        print(f"found character: {char}")
