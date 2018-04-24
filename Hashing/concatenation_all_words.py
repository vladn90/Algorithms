""" Problem statement:
https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
https://www.interviewbit.com/problems/substring-concatenation/
"""
from collections import Counter


class Solution:
    def find_substring(self, string, words):
        """ Algorithm is based on using sliding window and hashing.
        Sliding window is not static in this case, we stretch it to the right,
        and when needed narrow from the left.
        Time complexity: O(k * n). Space complexity: O(m).
        """
        if not string or not words:  # edge cases
            return []

        n = len(string)
        m = len(words)  # total number of words
        k = len(words[0])  # length of each word
        if n < k * m:  # string is shorter than substring we're looking for
            return []

        result = []  # resulting array with indices
        words_count = Counter(words)  # count word frequency in words
        for i in range(k):  # possible start of a substring
            # if curr[word] > 0, we still have to find this word, expand window to the right
            # if curr[word] == 0, we found this word in a substring
            # if curr[word] < 0, we gotta get rid of this word, narrow window from the left
            curr = words_count.copy()
            start = i  # start of the current window
            for j in range(start, n - k + 1, k):  # start of the next word we're gonna add
                word = string[j:j + k]  # word of length k
                curr[word] -= 1  # see comments above for explanation
                while curr[word] < 0:  # wrong word, narrow window from the left
                    prev = string[start:start + k]  # one of the previously added words
                    curr[prev] += 1  # "remove" this word from the dictionary
                    start += k  # move to the start of the next word
                # check if we have the right substring ..|start|substr|j|ing..
                if j + k - start == k * m:  # k * m is a total length of a substring we're looking for
                    result.append(start)
        return result


if __name__ == "__main__":
    sol = Solution()
    func = sol.find_substring

    # edge cases
    assert func("", []) == []
    assert func("foobar", []) == []
    assert func("", ["foo", "bar"]) == []

    string = "barfoothefoobarman"
    words = ["foo", "bar"]
    assert func(string, words) == [0, 9]

    string = "wordgoodstudentgoodword"
    words = ["word", "student"]
    assert func(string, words) == []

    string = "catbatatecatatebat"
    words = ["cat", "ate", "bat"]
    assert func(string, words) == [0, 3, 9]

    string = "abcdababcd"
    words = ["ab", "ab", "cd"]
    assert func(string, words) == [0, 2, 4]

    string = "abcdababcd"
    words = ["ab", "ab"]
    assert func(string, words) == [4]

    string = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo", "barr", "wing", "ding", "wing"]
    assert func(string, words) == [13]

    string = "aaaaaa"
    words = ["aaa", "aaa"]
    assert func(string, words) == [0]

    string = "abaababbaba"
    words = ["ab", "ba", "ab", "ba"]
    assert func(string, words) == [1, 3]
