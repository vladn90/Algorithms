""" Problem statement:
https://www.interviewbit.com/problems/window-string/
https://leetcode.com/problems/minimum-window-substring/description/
"""
from collections import Counter


class Solution:
    def window(self, string, pattern):
        """ Returns minimum length substring from string that contains all
        characters of pattern, returns an empty string if such string doesn't exist.
        Time complexity: O(n). Space complexity: O(1), n is len(s).
        """
        if len(string) < len(pattern):  # string cannot have pattern
            return ""
        if string and not pattern:  # pattern is an empty string
            return string[0]

        pattern_dict = Counter(pattern)  # hash map of characters count in pattern
        string_dict = Counter()  # characters count in current sliding window
        matched = 0  # number of characters matched in current window
        i, j = 0, 0  # start, end of sliding window
        x, y = -1, len(string)  # start, end of minimum substring
        while j < len(string):
            # expand window to the right while we don't have the full match
            while j < len(string) and matched < len(pattern):
                if string[j] in pattern_dict:
                    string_dict[string[j]] += 1
                    if string_dict[string[j]] <= pattern_dict[string[j]]:
                        matched += 1
                j += 1
            # narrow window from the left while we have the full match
            while matched == len(pattern):
                if j - i < y - x + 1:  # choose min substring
                    x, y = i, j - 1
                if string[i] in string_dict:
                    string_dict[string[i]] -= 1
                    # we don't have the full match anymore
                    if string_dict[string[i]] < pattern_dict[string[i]]:
                        matched -= 1
                i += 1
        if x != -1:  # minimum substring containining pattern was found
            return string[x:y + 1]
        return ""  # wasn't found


if __name__ == "__main__":
    sol = Solution()

    s = "ADOBECODEBANC"
    t = "ABC"
    print(sol.window(s, t))
