import random
from longest_brute import Solution as SolBrute
from longest_dp import Solution as SolDP
from longest_expand import Solution as SolExpand
from longest_manacher import Solution as SolManacher


sol_brute = SolBrute()
sol_dp = SolDP()
sol_expand = SolExpand()
sol_manacher = SolManacher()


# stress testing brute force solution against dynamic programming solution
for i in range(10**3):
    string = "".join(map(chr, [random.randrange(65, 91) for i in range(10**2)]))
    brute_result = sol_brute.longest_palindrome(string)
    dp_result = sol_dp.longest_palindrome(string)
    if brute_result == dp_result:
        print("OK")
        print(brute_result)
        print()
    else:
        print("Error.")
        print(f"string: {string}")
        print(f"brute force result: {brute_result}")
        print(f"dp result: {dp_result}")
        break

# stress testing dynamic programming solution against expand solution
for i in range(10**3):
    string = "".join(map(chr, [random.randrange(65, 91) for i in range(10**2)]))
    dp_result = sol_dp.longest_palindrome(string)
    expand_result = sol_expand.longest_palindrome(string)
    if expand_result == dp_result:
        print("OK")
        print(expand_result)
        print()
    else:
        print("Error.")
        print(f"string: {string}")
        print(f"dp result: {dp_result}")
        print(f"expand result: {expand_result}")
        break

# stress expand solution against Manacher's algorithm solution
for i in range(10**3):
    string = "".join(map(chr, [random.randrange(65, 91) for i in range(10**2)]))
    expand_result = sol_expand.longest_palindrome(string)
    manacher_result = sol_manacher.longest_palindrome(string)
    if expand_result == manacher_result:
        print("OK")
        print(expand_result)
        print()
    else:
        print("Error.")
        print(f"string: {string}")
        print(f"expand result: {expand_result}")
        print(f"manacher result: {manacher_result}")
        break

print("All tests are done!")
