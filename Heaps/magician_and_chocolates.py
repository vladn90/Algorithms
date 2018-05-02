""" Problem statement:
https://www.interviewbit.com/problems/magician-and-chocolates/
"""
import heapq


class Solution:
    def max_chocolate(self, k, bags):
        """ Time complexity: O(n * lg(n) + k * lg(n)). Space complexity: O(1),
        n is len(bag).
        """
        if not k or not bags:  # no time or no chocolate
            return 0

        m = 10 ** 9 + 7  # modulo value
        heap = []  # max heap
        for choc in bags:  # put all chocolate from the bag into max heap
            # -choc because Python heapq module implements min heap
            heapq.heappush(heap, -choc)

        total = 0  # total amount of eaten chocolate
        for i in range(k):
            curr = -heap[0]
            total = (total + curr % m) % m  # add bag with maximum number of chocolates
            heapq.heapreplace(heap, -(curr // 2))  # update bag contents
        return total


if __name__ == "__main__":
    sol = Solution()
    func = sol.max_chocolate

    bags = [6, 5]
    k = 3
    print(func(k, bags))
