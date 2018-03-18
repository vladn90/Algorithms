import random
from longest_brute import Solution as SolBrute
from longest_dp import Solution as SolDP


sol_brute = SolBrute()
sol_dp = SolDP()

# stress testing brute force solution against dynamic programming solution
while True:
    string = "".join(map(chr, [random.randrange(65, 91) for i in range(10**2)]))
    brute_result = sol_brute.longest_palindrome(string)
    dp_result = sol_dp.longest_palindrome(string)
    if brute_result == dp_result:
        print("OK")
        print(brute_result)
    else:
        print("Results are different.")
        print(f"string: {string}")
        print(f"brute force result: {brute_result}")
        print(f"dp result: {dp_result}")
        break
