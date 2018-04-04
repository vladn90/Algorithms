import math


class Solution:
    def power_brute_recur(self, x, n, m=1000000007):
        """ Returns x ^ n % m. Simple recursive algorithm.
        Time complexity: O(n). Space complexity: O(n).
        """
        if n == 1:
            return x % m
        return (x % m) * (self.power(x, n - 1) % m) % m

    def power_brute_iter(self, x, n, m=1000000007):
        """ Returns x ^ n % m. Simple iterative algorithm.
        Time complexity: O(n). Space complexity: O(1).
        """
        result = 1
        while n > 0:
            result = (result * (x % m)) % m
            n -= 1
        return result

    def power(self, x, n, m):
        """ Returns x ^ n % m. Exponentiation by squaring algorithm.
        input: x as integer
               n as positive integer
               m as positive integer
        output: integer

        Time complexity: O(n). Space complexity: O(1).
        """
        result = 1
        while n > 0:
            if n % 2 != 0:
                result = (result * x) % m
            x = ((x % m) * (x % m)) % m
            n //= 2
        return result


if __name__ == "__main__":
    sol = Solution()
    func = sol.power
    m = 10**9 + 7

    # testing against built-in pow function
    for x in range(-10**3, 10**3):
        for n in range(1, 10**3):
            assert func(x, n, m) == pow(x, n, m)
