""" Problem statement:
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""
from collections import Counter


class Solution:
    def find_anagrams_sort(self, s, p):  # correct, but TLE
        """ Sort string p and using sliding window of size len(p), check every
        sorted substring in s.
        Time complexity: O(n * (m * lg(m)) + m * lg(m)) = O((n + 1) * (m * lg(m))),
        Space complexity: O(m), where n, m are lengths of strings s, p.
        """
        n, m = len(s), len(p)
        if n < m:  # even string s cannot be an anagram of p since it's shorter
            return []

        p = sorted(p)
        result = []
        for i in range(n - m + 1):
            substring = sorted(s[i:i + m])
            if substring == p:
                result.append(i)
        return result

    def find_anagrams_hash(self, s, p):
        """ Similar algorithm as above but optimized by using hash map.
        Use sliding window to find all substrings of length len(p) in s, but
        instead of sorting them, compare their characters' count with p's
        characters' count.
        Time complexity: O(n). Space complexity: O(1), n is len(s).
        """
        n, m = len(s), len(p)
        if n < m:  # even string s cannot be an anagram of p since it's shorter
            return []
        if not s and not p:  # empty strings are anagrams of each other
            return [0]

        p_count = Counter(p)  # count characters occurence in p
        result = []
        # creating initial sliding window count of size m - 1, since we're gonna
        # add the last character of current sliding window in each loop iteration
        curr = Counter(s[:m - 1])
        for i in range(n - m + 1):
            curr[s[i + m - 1]] += 1  # add last character of current sliding window
            if curr == p_count:  # compare sliding window count with string p count
                result.append(i)
            curr[s[i]] -= 1  # delete previous character from the dictionary
            if curr[s[i]] == 0:
                del curr[s[i]]  # delete it completely if count is 0
        return result


if __name__ == "__main__":
    sol = Solution()

    s = "cbaebabacd"
    p = "abc"
    assert sol.find_anagrams_sort(s, p) == [0, 6]
    assert sol.find_anagrams_hash(s, p) == [0, 6]

    s = "abab"
    p = "ab"
    assert sol.find_anagrams_sort(s, p) == [0, 1, 2]
    assert sol.find_anagrams_hash(s, p) == [0, 1, 2]
