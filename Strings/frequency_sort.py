""" Problem description can be found here:
https://leetcode.com/problems/sort-characters-by-frequency/description/
"""


class Solution:
    def frequencySort(self, string):
        """ Returns string with characters sorted by their frequency
        in decreasing order.
        Time complexity: O(n). Space complexity: O(n), where
        n is len(string).

        """
        freq = {}  # character frequency hash map
        for char in string:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        # convert hash map to list of tuples: (character, frequency)
        # and sort it by frequency in decreasing order
        # sort in this case is O(1) since max number of characters = 52
        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # compose resulting string
        result = []
        for element in freq:
            result.append(element[0] * element[1])
        return "".join(result)


if __name__ == "__main__":
    sol = Solution()

    # tests
    assert sol.frequencySort("") == ""
    assert sol.frequencySort("tree") == "eetr"
    assert sol.frequencySort("cccaaa") == "cccaaa"
    assert sol.frequencySort("abcdabcdaa") == "aaaabbccdd"
    assert sol.frequencySort("aaaabbbccd") == "aaaabbbccd"
