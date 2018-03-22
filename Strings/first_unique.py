""" Problem description can be found here:
https://leetcode.com/problems/first-unique-character-in-a-string/description/
"""


class Solution:
    def firstUniqChar(self, string):
        """ Returns 1st unique character in the string.
        Time complexity: O(n). Space complexity: O(1), where n is len(string).
        """
        # tuple: character in order we first see it in the string and its index
        order = []
        # frequency of each character in the string, character: boolean
        # True if it's unique, False otherwise
        unique_freq = {}
        unique_index = -1
        for i, char in enumerate(string):
            if char in unique_freq:
                unique_freq[char] = False
            else:
                unique_freq[char] = True
                order.append((char, i))

        # find index of 1st unique character
        for char_tuple in order:
            char, i = char_tuple
            if unique_freq[char]:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()

    # tests
    assert sol.firstUniqChar("") == -1
    assert sol.firstUniqChar("abcdef") == 0
    assert sol.firstUniqChar("aabbccd") == 6
    assert sol.firstUniqChar("leetcode") == 0
    assert sol.firstUniqChar("loveleetcode") == 2
    assert sol.firstUniqChar("azzzbzzzabzzzcdd") == 13
