""" Problem statement:
https://leetcode.com/problems/swap-nodes-in-pairs/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head):
        """ Swap nodes in pairs in a linked list.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        if not head or not head.next:  # empty list or list with 1 node
            return head

        dummy = ListNode(None)
        tail = dummy
        prev, curr = None, head
        while curr and curr.next:
            # swap 1st node in current pair
            link = curr.next
            curr.next = prev

            # swap 2nd node
            prev = curr
            curr = link
            link = curr.next
            curr.next = prev

            # attach reversed pair to the tail
            tail.next = curr
            tail = prev  # update tail
            prev.next = link
            curr = link  # go the next node, no need to update prev node
        return dummy.next
