""" Problem statement:
https://www.interviewbit.com/problems/colorful-number/
"""
import random


class SolutionBrute:
    def digits_product(self, number):
        """ Returns a product of number's digits.
        input: number as string
        output: integer
        """
        digits = map(int, number)
        result = 1
        for d in digits:
            result *= d
        return result

    def is_colorful(self, number):
        """ Returns 1 if number is colorful, 0 otherwise.
        input: number as integer
        output: integer
        """
        number = str(number)
        n = len(number)
        # break number into different subsequences using sliding window
        # calculate product of each subsequence digits and check if it's unique
        product = set()
        for w in range(1, n + 1):  # w is a size of current sliding window
            for i in range(0, n - w + 1):
                # product of current subsequence digits
                curr_prod = self.digits_product(number[i:i + w])
                if curr_prod in product:
                    return 0  # product isn't unique
                product.add(curr_prod)
        return 1


class SolutionFast:
    def is_colorful(self, number):
        """ Returns 1 if number is colorful, 0 otherwise.
        Optimize initial algorithm by precomputing a table of cumulative product.
        Then we can find product of subsequence number[i:j] by calculating
        table[j] / table[i - 1].
        input: number as integer
        output: integer
        """
        number = str(number)
        n = len(number)
        product_table = [0] * n  # precompute cumulative product table
        product_table.append(1)  # for convinience
        for i, digit in enumerate(number):
            if digit == "0":
                break  # since every other product after 0 is gonna be 0
            product_table[i] = product_table[i - 1] * int(digit)

        product = set()  # hash table of unique products of digits
        for w in range(1, n + 1):  # w is a size of current sliding window
            for i in range(0, n - w + 1):
                # handle product equal to zero
                if product_table[i - 1] == 0:
                    curr_prod = 0
                else:
                    curr_prod = product_table[i + w - 1] // product_table[i - 1]
                if curr_prod in product:
                    return 0  # product isn't unique
                product.add(curr_prod)
        return 1


if __name__ == "__main__":
    sol_fast = SolutionFast()
    sol_brute = SolutionBrute()
    slow = sol_brute.is_colorful
    fast = sol_fast.is_colorful

    number = 3245
    assert slow(number) == 1
    assert fast(number) == 1

    while True:  # stress testing brute force and improved algorithms
        number = random.randrange(10**6)
        slow_result = slow(number)
        fast_result = fast(number)
        if slow_result == fast_result:
            print("OK")
            if slow_result:
                print(f"Found it! {number} is colorful!")
            else:
                print(f"{number} is not colorful.")
        else:
            print("Results are different.")
            print(f"number = {number}")
            print(f"slow result = {slow_result}")
            print(f"fast result = {fast_result}")
            break
