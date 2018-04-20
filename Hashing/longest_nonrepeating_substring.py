""" Problem statement:
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
https://www.interviewbit.com/problems/longest-substring-without-repeat/
"""
import random


class Solution:
    def longest_nonrepeat_brute(self, string):
        """ Returns length of longest nonrepeating substring. Brute force algorithm.
        Time complexity: O(n ^ 2). Space complexity: O(1), n is len(string).
        """
        max_len = 0
        for i in range(len(string)):
            for j in range(i, len(string)):
                curr = string[i:j + 1]  # current substring
                if len(curr) == len(set(curr)):  # check if it has only unique chars
                    max_len = max(max_len, j - i + 1)
        return max_len

    def longest_nonrepeat(self, string):
        """ Returns length of longest nonrepeating substring.
        Use a sliding window to move along the string, use a hash table(set) to
        keep track of unique characters in sliding window.
        Time complexity: O(n). Space complexity: O(1), n is len(string).
        """
        letters = set()  # letters that we've previously seen
        max_len = 0
        i = 0  # start index of current substring
        for j, char in enumerate(string):  # j is end index of current substring
            while letters and char in letters:
                letters.remove(string[i])  # remove 1st char from the left
                i += 1
            letters.add(char)
            if j - i + 1 > max_len:  # update max length
                max_len = j - i + 1
        return max_len

    def longest_nonrepeat_2(self, string):
        """ Returns length of longest nonrepeating substring. Optimized sliding window.
        Time complexity: O(n). Space complexity: O(1), n is len(string).
        """
        letters = dict()  # letters that we've previously seen and their index
        max_len = 0
        i = 0  # start index of current substring
        for j, char in enumerate(string):  # j is end index of current substring
            if char in letters and letters[char] >= i:
                i = letters[char] + 1
            letters[char] = j
            if j - i + 1 > max_len:  # update max length
                max_len = j - i + 1
        return max_len

    def stress_test(self, func1, func2, n):
        """ Stress testing two functions against each other using randomly
        generated string of length n.
        """
        while True:
            string = "".join(map(chr, [random.randrange(97, 123) for i in range(n)]))
            res1, res2 = func1(string), func2(string)
            if res1 == res2:
                print("OK")
                print(res1)
            else:
                print("Results are different.")
                print(f"string = {string}")
                print(f"result 1: {res1}")
                print(f"result 2: {res2}")
                break


if __name__ == "__main__":
    sol = Solution()

    string = "abcabcbb"
    assert sol.longest_nonrepeat_brute(string) == 3
    assert sol.longest_nonrepeat(string) == 3
    assert sol.longest_nonrepeat_2(string) == 3

    func1 = sol.longest_nonrepeat
    func2 = sol.longest_nonrepeat_2
    sol.stress_test(func1, func2, 100)
