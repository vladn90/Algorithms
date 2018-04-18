""" Problem statement:
https://leetcode.com/problems/valid-anagram/description/
"""
import random
from collections import Counter


class Solution:
    def is_anagram_sort(self, s, t):
        """ Sort the strings and compare them.
        Time complexity: O(n * lg(n) + m * lg(m)). Space complexity: O(n + m),
        n, m are lengths of strings s, t.
        """
        return sorted(s) == sorted(t)

    def is_anagram_hash(self, s, t):
        """ Count characters in each string and compare resulting hash maps.
        Time complexity: O(n + m). Space complexity: O(1),
        n, m are lengths of strings s, t.
        """
        if len(s) != len(t):  # strings of different lengths cannot be anagrams
            return False
        return Counter(s) == Counter(t)

    def stress_test(self, func1, func2):
        """ Stress tests two functions against each other. Checks the True case.
        """
        while True:
            s = [chr(random.randrange(97, 122)) for i in range(10**4)]
            t = s[:]
            random.shuffle(t)  # shuffle characters in s to generate t
            s, t = "".join(s), "".join(t)
            res1 = func1(s, t)
            res2 = func2(s, t)
            if res1 == res2:
                print("OK")
                print(s[:10])
            else:
                print("Results are different.")
                print(f"s = {s}")
                print(f"t = {t}")
                print(f"result 1 = {res1}")
                print(f"result 2 = {res2}")
                break


if __name__ == "__main__":
    sol = Solution()

    s = "aacc"
    t = "ccac"
    assert sol.is_anagram_sort(s, t) == False
    assert sol.is_anagram_hash(s, t) == False

    s = "anagram"
    t = "nagaram"
    assert sol.is_anagram_sort(s, t) == True
    assert sol.is_anagram_hash(s, t) == True

    # stress testing solutions
    sol.stress_test(sol.is_anagram_sort, sol.is_anagram_hash)
