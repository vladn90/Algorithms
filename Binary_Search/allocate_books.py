""" Problem statement:
https://www.interviewbit.com/problems/allocate-books/

Same as Painter's Partition problem:
https://www.interviewbit.com/problems/painters-partition-problem/

Very good and detailed description of the algorithm for Painter's Partition:
https://articles.leetcode.com/the-painters-partition-problem-part-ii/
"""


class Solution:
    def count_students(self, books, min_pages):
        """ Returns number of students needed if you assign to each student min_pages.
        Time complexity: O(n). Space complexity: O(1), n is len(books).
        """
        curr = 0  # number of pages assigned to current student
        total = 1  # number of students needed so far
        for page in books:
            if curr + page > min_pages:  # current student have enough pages already
                total += 1
                curr = 0
            curr += page
        return total

    def min_pages(self, books, m):
        """ Returns minimum number of pages per student.
        Time complexity: O(n * lg(m)). Space complexity: O(1),
        n is len(books), m is sum of all pages in books, i.e. sum(books).
        """
        if m > len(books) or not m:  # allotment is not possible, not enough books
            return -1

        low = max(books)  # minimum number of pages that can be assigned to one student
        high = sum(books)  # and maximum number
        while low < high:  # use binary search to find minimum number of pages
            mid = (low + high) // 2
            result = self.count_students(books, mid)
            if result > m:  # need to assign more pages for each student
                low = mid + 1
            else:  # result <= m, need to assign this number or less for each student
                high = mid
        return low


if __name__ == "__main__":
    sol = Solution()
    func = sol.min_pages

    books = [12, 34, 67, 90]
    m = 2
    assert func(books, m) == 113

    books = [73, 58, 30, 72, 44, 78, 23, 9]
    m = 5
    assert func(books, m) == 110

    books = [10, 12, 15]
    m = 4
    assert func(books, m) == -1
