""" Problem statement:
https://leetcode.com/problems/odd-even-linked-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head):
        """ Returns a head to the modified list.
        Time complexity: O(n). Space complexity: O(1), n is length of the list.
        """
        # special case, linked list has 1 or less nodes
        if head is None or head.next is None:
            return head

        # choose 1st odd and 1st even node
        odd = head
        even = head.next
        even_start = even  # save the link to the 1st even node(see below why)

        # traverse list and attach every odd / even node to nodes above
        curr = head.next.next  # start from the 3rd node
        is_odd = True  # set to True since 3rd node is odd
        while curr:
            if is_odd:
                odd.next = curr
                odd = odd.next
                is_odd = False  # since next node will be even
            else:
                even.next = curr
                even = even.next
                is_odd = True  # since next node will be odd
            curr = curr.next

        # connect last odd node to the first even node
        odd.next = even_start
        even.next = None  # prevents creating a cycle inside linked list
        return head
