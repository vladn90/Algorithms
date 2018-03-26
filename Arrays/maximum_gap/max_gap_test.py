import random
from max_gap_naive import Solution as SolutionNaive
from max_gap_bucket import Solution as SolutionBucket


# stress testing naive algorithm against bucket algorithm
while True:
    array = [random.randrange(1, 10**4) for i in range(10**4)]
    sol_naive = SolutionNaive()
    sol_bucket = SolutionBucket()
    result_naive = sol_naive.maximumGap(array)
    result_bucket = sol_bucket.maximumGap(array)
    if result_naive == result_bucket:
        print("OK")
        print(result_naive)
    else:
        print("Results are different.")
        print(f"array = {array}")
        print(f"naive result: {result_naive}")
        print(f"bucket result: {result_bucket}")
        break
