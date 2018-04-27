""" Problem statement:
https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
https://www.interviewbit.com/problems/letter-phone/
"""


class SolutionLeetCode:
    def letterCombinations(self, digits):
        if not digits:
            return []

        def helper(digits, i, curr, digit_to_letters, result):
            if len(curr) == len(digits):
                result.append(curr)
                return
            for x in range(i, len(digits)):
                chars = digit_to_letters[digits[x]]
                for j in range(len(chars)):
                    letter = chars[j]
                    helper(digits, x + 1, curr + letter, digit_to_letters, result)

        digit_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        helper(digits, 0, "", digit_to_letters, result)
        return result


class SolutionInterviewBit:
    def letterCombinations(self, digits):
        if not digits:
            return []

        def helper(digits, i, curr, digit_to_letters, result):
            if len(curr) == len(digits):
                result.append(curr)
                return
            for x in range(i, len(digits)):
                chars = digit_to_letters[digits[x]]
                for j in range(len(chars)):
                    letter = chars[j]
                    helper(digits, x + 1, curr + letter, digit_to_letters, result)

        digit_to_letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
                            "0": "0", "1": "1"}
        result = []
        helper(digits, 0, "", digit_to_letters, result)
        return result


if __name__ == "__main__":
    sol = SolutionInterviewBit()
    func = sol.letterCombinations

    digits = "0123"
    res = func(digits)
    for string in res:
        print(string)
