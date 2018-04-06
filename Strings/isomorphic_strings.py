""" Problem statement:
https://leetcode.com/problems/isomorphic-strings/description/
"""


class Solution:
    def is_isomorphic(self, s1, s2):
        """ Algorithm based on encoding two strings and comparing resulted
        encodings. Encoding is following: each new character receives a unique
        index, starting from 0. We keep track of already used characters.
        If we see the character again, we take index from a dictionary,
        otherwise we assign a new index.

        Time complexity: O(n). Space complexity: O(n), n is len(s1) == len(s2).
        """
        # encode strings
        enc1, enc2 = [], []
        count1, count2 = 0, 0
        dict1, dict2 = dict(), dict()
        for i in range(len(s1)):
            char1, char2 = s1[i], s2[i]
            if char1 in dict1:
                enc1.append(dict1[char1])
            else:
                count1 += 1
                dict1[char1] = count1
                enc1.append(dict1[char1])
            if char2 in dict2:
                enc2.append(dict2[char2])
            else:
                count2 += 1
                dict2[char2] = count2
                enc2.append(dict2[char2])
        return enc1 == enc2  # compare encodings

    def is_isomorphic_fast(self, s1, s2):
        """ Optimized version of the above algorithm.
        Time complexity: O(n). Space complexity: O(1), n is len(s1) == len(s2).
        """
        # encode strings
        count1, count2 = 0, 0
        dict1, dict2 = dict(), dict()
        for i in range(len(s1)):
            char1, char2 = s1[i], s2[i]  # current characters
            if char1 in dict1:
                curr1 = dict1[char1]  # current index of character in s1
            else:
                count1 += 1
                dict1[char1] = count1
                curr1 = dict1[char1]
            if char2 in dict2:
                curr2 = dict2[char2]  # current index of character in s2
            else:
                count2 += 1
                dict2[char2] = count2
                curr2 = dict2[char2]
            if curr1 != curr2:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    func = sol.is_isomorphic_fast

    assert func("egg", "add") == True
    assert func("foo", "bar") == False
    assert func("paper", "title") == True
    assert func("aba", "baa") == False
