""" Problem statement:
https://leetcode.com/problems/generate-parentheses/description/
https://www.interviewbit.com/problems/generate-all-parentheses-ii/

Time and space complexity are exponential. For more details see this article:
https://leetcode.com/problems/generate-parentheses/solution/
"""


class Solution:
    def generate(self, open_count, close_count, n, curr, result):
        if close_count == n:
            result.append("".join(curr))
            return
        if open_count > close_count:
            curr.append(")")
            self.generate(open_count, close_count + 1, n, curr, result)
            curr.pop()  # backtracking
        if open_count < n:
            curr.append("(")
            self.generate(open_count + 1, close_count, n, curr, result)
            curr.pop()  # backtracking

    def generateParenthesis(self, n):
        result = []
        self.generate(0, 0, n, [], result)
        # result.sort()  # used for interviewbit
        return result


if __name__ == "__main__":
    sol = Solution()
    func = sol.generateParenthesis

    result = func(3)
    for r in result:
        print(r)
