""" Problem description can be found here:
https://leetcode.com/problems/restore-ip-addresses/description/
"""


class Solution:
    def restoreIpAddresses(self, string):
        """ Returns a list of all possible addresses from string.
        Put dots in all possible places and verify the resulting address.
        Time complexity: O(1). Space complexity: O(1).
        """
        # special case, not enough or too many numbers
        if len(string) < 4 or len(string) > 12:
            return []

        result = []  # list of all possible ip addresses
        n = len(string)
        i_end = min(3, n - 3)
        for i in range(0, i_end):  # 1st dot
            num1 = string[:i + 1]  # 1st number in ip address
            if (num1[0] == "0" and len(num1) > 1) or int(num1) > 255:
                break

            j_end = min(i + 4, n - 2)
            for j in range(i + 1, j_end):  # 2nd dot
                num2 = string[i + 1:j + 1]  # 2nd number in ip address
                if (num2[0] == "0" and len(num2) > 1) or int(num2) > 255:
                    break

                k_end = min(j + 4, n - 1)
                for k in range(j + 1, k_end):  # 3rd dot
                    # composing possible ip address
                    num3 = string[j + 1:k + 1]  # 3rd number in ip address
                    if (num3[0] == "0" and len(num3) > 1) or int(num3) > 255:
                        break
                    num4 = string[k + 1:]  # 4th number in ip address
                    if (num4[0] == "0" and len(num4) > 1) \
                            or len(num4) > 4 or int(num4) > 255:
                        continue
                    result.append([num1, num2, num3, num4])

        if result:
            result = list(map(".".join, result))
            result.sort()
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.restoreIpAddresses("255255192168") == ["255.255.192.168"]
    assert sol.restoreIpAddresses("1234") == ["1.2.3.4"]
    assert sol.restoreIpAddresses("25525511135") == ['255.255.11.135', '255.255.111.35']
    assert sol.restoreIpAddresses("0000") == ["0.0.0.0"]
    assert sol.restoreIpAddresses("25505011535") == []
