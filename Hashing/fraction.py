""" Problem statement:
https://leetcode.com/problems/fraction-to-recurring-decimal/description/
https://www.interviewbit.com/problems/fraction/
"""


class Solution:
    def fractional(self, rem, den):
        """ Helper function for fraction_to_decimal, returns fractional part.
        """
        result = []
        rem_dict = dict()  # remainders that we've seen already
        i = 0  # current remainder's index
        while True:
            if rem == 0:  # doesn't have a repeating part
                return "".join(map(str, result))
            if rem in rem_dict:  # repeating part was found
                j = rem_dict[rem]  # starting index of a repeating cycle
                nonrepeat = "".join(map(str, result[:j]))
                cycle = "".join(map(str, result[j:]))
                return nonrepeat + "(" + cycle + ")"
            rem_dict[rem] = i  # save current remainder in a dictionary
            i += 1  # index of the next remainder
            rem *= 10
            result.append(rem // den)
            rem %= den

    def fraction_to_decimal(self, num, den):
        """ Converts fraction to decimal, takes into account repeating part.
        """
        if den == 0:
            raise ZeroDivisionError
        if num == 0:
            return "0"
        if (num < 0 and den > 0) or (num > 0 and den < 0):
            sign = "-"
        else:
            sign = ""
        num, den = abs(num), abs(den)

        int_part = str(num // den)
        fract_part = self.fractional(num % den, den)
        if not fract_part:
            return sign + int_part
        return sign + int_part + "." + fract_part


if __name__ == "__main__":
    sol = Solution()
    func = sol.fraction_to_decimal

    # simple tests
    assert func(1, 2) == "0.5"
    assert func(2, 1) == "2"
    assert func(1, 2) == "0.5"
    assert func(10000, 2048) == "4.8828125"
    assert func(1, 2147483648) == "0.0000000004656612873077392578125"

    # testing repeat
    assert func(2, 3) == "0.(6)"
    assert func(1, 9) == "0.(1)"
    assert func(1, 3) == "0.(3)"
    assert func(2, 3) == "0.(6)"
    assert func(9, 11) == "0.(81)"
    assert func(7, 12) == "0.58(3)"
    assert func(1, 7) == "0.(142857)"
    assert func(1, 81) == "0.(012345679)"
    assert func(22, 7) == "3.(142857)"
    assert func(1, 29) == "0.(0344827586206896551724137931)"
    assert func(1, 24) == "0.041(6)"

    # testing negative
    assert func(22, -7) == "-3.(142857)"
    assert func(-22, 7) == "-3.(142857)"
    assert func(-22, -7) == "-3.(142857)"
