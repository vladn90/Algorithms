""" Problem statement:
https://www.interviewbit.com/problems/anagrams/
"""


class Solution:
    def anagrams(self, strings):
        """ Groups strings by their unique key.
        """
        str_dict = dict()  # sorted string: its anagrams indices
        order = []  # order in which we added keys to the dictionary
        for i, word in enumerate(strings, start=1):
            curr = "".join(sorted(word))  # current key
            if curr in str_dict:
                str_dict[curr].append(i)
            else:  # we don't have this anagram in the dictionary yet
                order.append(curr)
                str_dict[curr] = [i]

        result = []  # build the resulting array based on str_dict and order
        for key_word in order:
            result.append(str_dict[key_word])
        return result


if __name__ == "__main__":
    sol = Solution()

    strings = ["cat", "dog", "god", "tca"]
    strings = ["a", "b", "c", "d"]
    strings = ["abc", "acb", "bca", "cba"]
    strings = []
    strings = ["aba"]
    print(sol.anagrams(strings))
