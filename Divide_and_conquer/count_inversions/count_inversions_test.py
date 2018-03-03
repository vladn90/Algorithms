""" Stress testing divide and conquer algorithm against brute force algorithm.
"""
import random
from count_inversions_brute import count_inv_brute
from count_inversions_dc import count_inv


if __name__ == "__main__":
    # stress testing
    while True:
        array = [random.randrange(-10**6, 10**6) for i in range(10**3)]
        result_brute = count_inv_brute(array)
        result_dc = count_inv(array)
        if result_dc == result_brute:
            print("OK")
            print(f"result: {result_dc}")
        else:
            print("Something went wrong.")
            print(f"array: {array}")
            print(f"result brute force: {result_brute}")
            print(f"result divide and conquer: {result_dc}")
            break
