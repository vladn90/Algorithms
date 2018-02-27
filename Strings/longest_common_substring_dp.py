""" Dynamic programming algorithm to find longest common substring.
Algorithm description can be found here:
https://en.wikipedia.org/wiki/Longest_common_substring_problem.
"""
import random
import string
from time import time


def longest_common_substring_1(s1, s2):
    """ Regular dynamic programming algorithm.

    Time complexity O(len(s1) * len(s2)),
    space complexity O(len(s1) * len(s2)).
    """
    # initializing 2D table of longest common suffix
    # between prefixes of s1(rows) and s2(columns)
    suffix_matrix = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]

    max_len = 0  # length of longest commmon suffix so far
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            # current characters of s1 and s2 are equal
            if s1[i - 1] == s2[j - 1]:
                # length of previous longest common suffix of
                # prefixes of s1 and s2
                prev_len = suffix_matrix[i - 1][j - 1]
                suffix_matrix[i][j] = prev_len + 1
                max_len = max(max_len, suffix_matrix[i][j])
            # if s1[i - 1] != s2[j - 1] then suffix_matrix[i][j] = 0, i.e.
            # nothing changes if current characters of s1 and s2 are different
    return max_len


def lcs_wrapper(lcs_function, s1, s2):
    """ For the optimimal space complexity of the following dynamic
    programming algorithms, use s2 as the shortest string and s1 as the longest.
    Alternatively, use this wrapper function.
    """
    if len(s1) < len(s2):
        return lcs_function(s2, s1)
    return lcs_function(s1, s2)


def longest_common_substring_2(s1, s2):
    """ Space optimized version of dynamic programming algorithm.
    Store only previous and current arrays of results, not the whole 2-D table.

    Time complexity O(len(s1) * len(s2)),
    space complexity O(min(len(s1), len(s2))).
    """
    # creating 2 arrays to store results of longest common suffix
    # between prefixes of s1 and s2
    prev_suffixes = [0] * len(s2)
    curr_suffixes = [0] * len(s2)

    max_len = 0  # length of longest commmon suffix so far
    for i in range(len(s1)):
        # the longest suffix for 1-letter word, i.e. s2[0]
        # can have a length at most 1
        if s1[i] == s2[0]:
            curr_suffixes[0] = 1
            if max_len == 0:
                max_len = 1
        # start from the 2nd letter in s2 since we've already checked
        # the 1st letter in previous step
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                curr_suffixes[j] = prev_suffixes[j - 1] + 1
                max_len = max(max_len, curr_suffixes[j])
        prev_suffixes = curr_suffixes
        curr_suffixes = [0] * len(s2)
    return max_len


def longest_common_substring_3(s1, s2):
    """ Further space optimized version of dynamic programming algorithm.
    Store only non-zero results of previous and current arrays in a dictionary.

    Time complexity O(len(s1) * len(s2)),
    space complexity O(min(len(s1), len(s2))).
    """
    prev_suffixes = {}
    curr_suffixes = {}

    max_len = 0  # length of longest commmon suffix so far
    for i in range(len(s1)):
        # the longest suffix for 1-letter word, i.e. s2[0]
        # can have a length at most 1
        if s1[i] == s2[0]:
            curr_suffixes[0] = 1
            if max_len == 0:
                max_len = 1
        # start from the 2nd letter in s2 since we've already checked
        # the 1st letter in previous step
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                prev_len = prev_suffixes.get(j - 1, 0)
                curr_suffixes[j] = prev_len + 1
                max_len = max(max_len, curr_suffixes[j])
        prev_suffixes = curr_suffixes
        curr_suffixes = {}
    return max_len


if __name__ != "__main__":
    # simple test
    string1 = "ABAB"
    string2 = "BABA"
    assert longest_common_substring_1(string1, string2) == 3
    assert longest_common_substring_2(string1, string2) == 3
    assert longest_common_substring_2(string1, string2) == 3

    # benchmarking 3 dynamic programming algorithms
    n1, n2 = 10**4, 10**4
    letters = string.ascii_lowercase
    s1 = "".join([random.choice(letters) for i in range(n1)])
    s2 = "".join([random.choice(letters) for i in range(n2)])

    # regular dynamic programming algorithm
    start = time()
    res1 = longest_common_substring_1(s1, s2)
    end = time()
    res1_time = end - start

    # space optimized dynamic programming algorithm
    start = time()
    res2 = longest_common_substring_2(s1, s2)
    end = time()
    res2_time = end - start

    # further space optimized dynamic programming algorithm
    start = time()
    res3 = longest_common_substring_3(s1, s2)
    end = time()
    res3_time = end - start

    assert res1 == res2 == res3
    print(f"Regular dp algorithm, time spent: {res1_time}")
    print(f"Optimization using 2 arrays, time spent: {res2_time}")
    print(f"Optimization using 2 dictionaries, time spent: {res3_time}")
