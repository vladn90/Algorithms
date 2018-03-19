""" Problem description can be found here:
https://leetcode.com/problems/rotate-string/description/
"""
import random


class Solution:
    def rotateString_1(self, a, b):
        """ Returns True if string b is a rotation of string a, False otherwise.

        Brute force solution. Algorithm description:
        Check if any substring of string a matches string b,
        substring of a = a[i:last character] + a[first character:i - 1].
        Use modulo operation to loop over the string a in circle.

        Time complexity: O(n ^ 2). Space complexity: O(1),
        where n is the length of string a and length of string b.
        """
        # special case, strings have different lengths
        if len(a) != len(b):
            return False

        # special case, empty strings
        if not a:
            return True

        n = len(a)
        for i in range(n):  # choose starting index for string a
            # loop over from current character till previous character
            # use modulo not to exceed length of the string
            for j in range(i, i + n):
                k = j - i  # current index of string b
                if a[j % n] != b[k]:
                    break
            else:  # no break occured, all characters have matched
                return True
        return False

    def rotateString_2(self, a, b):
        """ Returns True if string b is a rotation of string a, False otherwise.

        Improved algorithm. Concatenate string b with itself and check
        if string a is a substring of new string.

        Time complexity: O(n). Space complexity: O(n),
        where n is the length of string a and length of string b.
        """
        return a in (b + b) and len(a) == len(b)


if __name__ == "__main__":
    sol = Solution()
    # simple tests
    a, b = "abcde", "cdeab"
    assert sol.rotateString_1(a, b) == True
    assert sol.rotateString_2(a, b) == True
    a, b = "abcde", "cdeaa"
    assert sol.rotateString_1(a, b) == False
    assert sol.rotateString_2(a, b) == False

    # testing True case against randomly generated strings
    n = 10**2
    while True:
        a = "".join(map(chr, [random.randrange(65, 91) for i in range(n)]))
        i = random.randrange(n)
        b = a[i:] + a[:i]
        assert sol.rotateString_1(a, b) == True
        assert sol.rotateString_2(a, b) == True
        print(a[:10], b[:10])
