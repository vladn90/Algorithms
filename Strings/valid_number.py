""" Problem description can be found here:
https://leetcode.com/problems/valid-number/description/
"""


class Solution:
    def isNumber(self, string):
        """ Returns True if string is a valid number, False otherwise.
        Time complexity: O(n). Space complexity: O(1), where n is len(string).
        """
        # special case, empty string
        if not string:
            return False

        found = False
        special_char = {"e", "."}  # only 1 "e" and 1 "." can be in the string
        n = len(string)
        for i, char in enumerate(string):
            # checking leading spaces before the digit character
            if not found and char == " " and i < (n - 1):
                continue

            # check trailing spaces after the last digit character
            elif found and char == " ":
                i += 1
                while i < n:
                    if string[i] != " ":
                        return False
                    i += 1
                break

            # character is digit
            elif char.isdigit():
                found = True

            # handle the dot
            elif not found and char == "." and i < (n - 1) \
                    and string[i + 1].isdigit():
                special_char.remove(char)
                found = True
            elif found and char == "." \
                    and string[i - 1].isdigit() \
                    and char in special_char \
                    and "e" in special_char:
                special_char.remove(char)
                continue

            # handle the e
            elif found and char == "e" \
                    and char in special_char \
                    and (string[i - 1].isdigit() or string[i - 1] == ".") \
                    and i < (n - 1) \
                    and (string[i + 1].isdigit()
                         or string[i + 1] == "+"
                         or string[i + 1] == "-"):
                special_char.remove(char)

            # handle the sign before number
            elif not found and (char == "+" or char == "-") and i < (n - 1)\
                    and (string[i + 1].isdigit() or string[i + 1] == "."):
                continue

            # handle the sign of "e"
            elif found and (char == "+" or char == "-") and i < (n - 1) \
                    and string[i - 1] == "e" \
                    and string[i + 1].isdigit():
                continue
            # all other cases
            else:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()

    assert sol.isNumber("1e+2") == True
    assert sol.isNumber("1e-2") == True

    assert sol.isNumber("") == False
    assert sol.isNumber("     ") == False
    assert sol.isNumber(" 000000  ") == True
    assert sol.isNumber(" 0") == True

    assert sol.isNumber("23   ") == True
    assert sol.isNumber("   23") == True
    assert sol.isNumber("  23   ") == True
    assert sol.isNumber("  23 23   ") == False

    assert sol.isNumber("0.12") == True
    assert sol.isNumber("  0.12 ") == True
    assert sol.isNumber("0.1.2") == False

    assert sol.isNumber(".") == False
    assert sol.isNumber(".  ") == False
    assert sol.isNumber("  .") == False
    assert sol.isNumber(".3") == True
    assert sol.isNumber("3.") == True

    assert sol.isNumber("+") == False
    assert sol.isNumber("  +") == False
    assert sol.isNumber("+  ") == False
    assert sol.isNumber("-") == False
    assert sol.isNumber("  -") == False
    assert sol.isNumber("-  ") == False
    assert sol.isNumber("  -.  ") == False
    assert sol.isNumber("  +. ") == False

    assert sol.isNumber("+0.12") == True
    assert sol.isNumber("-0.12") == True
    assert sol.isNumber("   0.12  ") == True
    assert sol.isNumber("   -0.2  ") == True
    assert sol.isNumber("   +0.2  ") == True

    assert sol.isNumber("   -23") == True
    assert sol.isNumber("   +23") == True
    assert sol.isNumber("   23-") == False
    assert sol.isNumber("   23+") == False
    assert sol.isNumber("   --23") == False
    assert sol.isNumber("   ++23") == False
    assert sol.isNumber("   2-3") == False
    assert sol.isNumber("   2+3") == False

    assert sol.isNumber("1e1") == True
    assert sol.isNumber("   1e1   ") == True
    assert sol.isNumber("1e-1") == True
    assert sol.isNumber("  1e-1   ") == True
    assert sol.isNumber("0.1234e10") == True
    assert sol.isNumber("-00001.1e-10") == True
    assert sol.isNumber("46.e3") == True

    assert sol.isNumber("1e.1") == False
    assert sol.isNumber("1e0.1") == False
    assert sol.isNumber("1e-.1") == False
    assert sol.isNumber("1e-0.1") == False
    assert sol.isNumber("1e") == False
    assert sol.isNumber("e") == False
    assert sol.isNumber("e1") == False
    assert sol.isNumber(" +0e-  ") == False

    assert sol.isNumber("ffff") == False
    assert sol.isNumber("   12 abc") == False
