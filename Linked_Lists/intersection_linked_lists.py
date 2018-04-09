""" Problem statement:
https://leetcode.com/problems/intersection-of-two-linked-lists/description/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def get_intersection_node(self, head1, head2):
        """ Returns a node where list 1 connects with list 2 if there's one,
        returns None otherwise.
        Time complexity: O(n + m). Space complexity: O(1), where
        n, m are lengths of linked lists.
        """
        curr1, curr2 = head1, head2
        # prevents infinite loop if two lists don't have an intersection
        exit1, exit2 = False, False
        while curr1 != curr2:  # traverse lists until we find the same node
            if curr1 is not None:
                curr1 = curr1.next
            elif not exit1:  # traversed list1 once, put curr1 pointer to the head of list 2
                exit1 = True
                curr1 = head2
            else:  # traversed lists twice
                return
            if curr2 is not None:
                curr2 = curr2.next
            elif not exit2:
                exit2 = True
                curr2 = head1
            else:  # traversed lists twice
                return
        # we broke out of the loop, hence we found two equal nodes
        return curr1

    def get_intersection_node(self, head1, head2):
        """ Faster code. Assumes there's an intersection between two lists.
        Otherwise it'll just run in infinite loop.
        Time complexity: O(n + m). Space complexity: O(1), where
        n, m are lengths of linked lists.
        """
        curr1, curr2 = head1, head2
        while curr1 != curr2:
            if curr1:  # more nodes to see
                curr1 = curr1.next
            else:  # reached the end of the list, i.e. curr1 == None
                curr1 = head2
            if curr2:
                curr2 = curr2.next
            else:
                curr2 = head1
        return curr1
