""" Problem statement:
https://www.interviewbit.com/problems/4-sum/
"""
import random


class Solution:
    def four_sum_brute(self, array, target):
        """ Brute force algorithm. Checks all possible combinations.
        Time complexity: O(n ^ 4). Space complexity: O(1), n is len(array),
        size of the output isn't uncluded in space complexity analysis.
        """
        result = set()
        n = len(array)
        for a in range(n - 3):
            for b in range(a + 1, n - 2):
                for c in range(b + 1, n - 1):
                    for d in range(c + 1, n):
                        n1, n2, n3, n4 = array[a], array[b], array[c], array[d]
                        if n1 + n2 + n3 + n4 == target:
                            result.add(tuple(sorted([n1, n2, n3, n4])))
        return sorted(result)

    def four_sum_hash(self, array, target):
        """ Optimized solution by using hash map.
        Time complexity: O(n ^ 2). Space complexity: O(n), n is len(array),
        size of the output isn't uncluded in space complexity analysis.
        """
        result = set()
        sums = dict()
        n = len(array)
        for a in range(n - 1):
            for b in range(a + 1, n):
                curr = array[a] + array[b]
                missing = target - curr
                if missing in sums:
                    for arr in sums[missing]:
                        c, d = arr
                        if a != c and a != d and b != c and b != d:
                            n1, n2 = array[c], array[d]
                            n3, n4 = array[a], array[b]
                            result.add(tuple(sorted([n1, n2, n3, n4])))
                if curr in sums:
                    sums[curr].append([a, b])
                else:
                    sums[curr] = [[a, b]]
        return sorted(result)

    def stress_test(self, func1, func2):
        """ Stress tests two functions against each other using random array.
        """
        while True:
            array = [random.randrange(1, 10) for i in range(30)]
            target = random.randrange(10, 20)

            res1 = func1(array, target)
            res2 = func1(array, target)
            if res1 == res2:
                print("OK")
                print(len(res1))
            else:
                print("Results are different.")
                print(f"array = {array}")
                print(f"target = {target}")
                print(f"result 1 = {res1}")
                print(f"result 2 = {res2}")
                break


if __name__ == "__main__":
    sol = Solution()

    array = [1, 0, -1, 0, -2, 2]
    target = 0
    print(sol.four_sum_brute(array, target))
    print(sol.four_sum_hash(array, target))

    array = [1, 2, 3, 4, 5, 5, 10, 10]
    target = 15
    print(sol.four_sum_brute(array, target))
    print(sol.four_sum_hash(array, target))

    array = [1, 2, 3]
    target = 6
    print(sol.four_sum_brute(array, target))
    print(sol.four_sum_hash(array, target))

    array = [-1, -1, -1, - 1, 0, 0, 0, 0, 1, 1, 1, 1]
    target = 0
    print(sol.four_sum_brute(array, target))
    print(sol.four_sum_hash(array, target))

    sol.stress_test(sol.four_sum_brute, sol.four_sum_hash)
