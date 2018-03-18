""" Problem description can be found here:
    https://leetcode.com/problems/count-and-say/description/
"""


class Solution:
    def count_and_say_1(self, n):
        """ Returns count-and-say sequence up to the nth term included.

        Algorithm description to find the next term:
        1) Count repeated numbers of current term till 1st non-repeated number.
        2) Add str(count as a number) + str(number) to the resulting string.
        3) Repeat till the end of current term.

        Time complexity: O(n * m). Space complexity: O(m),
        where m is the length of the largest term in sequence.
        """
        sequence = ["1"]
        for i in range(2, n + 1):
            prev = sequence[-1]
            curr_number = prev[0]  # current repeated digit in previous term
            curr_count = 1  # count of repeated digit
            result = []  # resulting array for current term
            for j in range(1, len(prev)):
                if prev[j] == curr_number:
                    curr_count += 1
                else:
                    result.append(str(curr_count))
                    result.append(curr_number)
                    curr_number = prev[j]
                    curr_count = 1

            # add the last count + digit
            result.append(str(curr_count))
            result.append(curr_number)
            # append new term to the sequence
            sequence.append("".join(result))

        return sequence

    def count_and_say_2(self, n):
        """ Returns n-th term of count and say sequence.

        Algorithm description to find next term:
        1) Count repeated numbers of current term till 1st non-repeated number.
        2) Add str(count as a number) + str(number) to the resulting string.
        3) Repeat till the end of current term.

        Time complexity: O(n * m). Space complexity: O(m),
        where m is the length of the largest term in sequence,
        space used for output sequence doesn't count.
        """
        prev = "1"  # 1st element of the sequence
        for i in range(2, n + 1):
            curr_number = prev[0]  # current repeated digit in previous term
            curr_count = 1  # count of repeated digit
            result = []  # resulting array
            for j in range(1, len(prev)):
                if prev[j] == curr_number:
                    curr_count += 1
                else:
                    result.append(str(curr_count))
                    result.append(curr_number)
                    curr_number = prev[j]
                    curr_count = 1

            # add the last count + digit
            result.append(str(curr_count))
            result.append(curr_number)
            # update previous term, i.e. previous = current
            prev = "".join(result)

        return prev


if __name__ == "__main__":
    s = Solution()

    # testing
    n = 15
    seq = s.count_and_say_1(n)  # generating count-and-say sequence up to n
    for i, element in enumerate(seq):
        # checking each element with n-th term generator algorithm
        assert element == s.count_and_say_2(i + 1)
        print(element)
