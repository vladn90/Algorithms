""" Problem statement:
https://leetcode.com/problems/add-two-numbers/description/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, head1, head2):
        """ Returns head pointer to a new linked list.
        Time complexity: O(n + m). Space complexity: O(1), where
        n, m are lengths of the linked lists.
        """
        # traverse both lists and save resulting number in 1st list
        curr1, curr2 = head1, head2
        rem = 0
        prev = None  # pointer to the previous node of list 1
        while curr1 and curr2:
            curr_sum = curr1.val + curr2.val + rem  # total sum of current digits
            curr1.val = curr_sum % 10
            rem = curr_sum // 10
            prev = curr1  # update previous pointer
            curr1, curr2 = curr1.next, curr2.next

        # 1st number has more digits and we have some remainder to deal with
        while curr1 and rem:
            curr_sum = rem + curr1.val
            curr1.val = curr_sum % 10
            rem = curr_sum // 10
            prev, curr1 = curr1, curr1.next

        # 2nd number has more digits in it
        if curr2:  # link last node of the 1st list to the curr node of the 2nd
            prev.next = curr2
        while curr2:
            curr_sum = curr2.val + rem
            curr2.val = curr_sum % 10
            rem = curr_sum // 10
            prev, curr2 = curr2, curr2.next

        # attach the remainder if there's some
        if rem:
            prev.next = ListNode(rem)
        return head1
