""" Problem statement:
https://leetcode.com/problems/reverse-nodes-in-k-group/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """ Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        if not head or not head.next:  # empty list or list with 1 node
            return head

        # find length of the list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        if k > length or k < 1:  # special case, invalid k
            return head
        m = length // k  # number of total reverses

        # traverse the list and reverse nodes in k groups
        n = 1  # number of current reverse
        i = 1  # index of current node in k group, 1-based index
        dummy = ListNode(None)  # dummy node to attach reversed nodes to
        tail = dummy  # current tail of reversed list
        prev, curr = None, head  # previous and current pointers
        start = head  # pointer to 1st node in current k group
        while n <= m:
            # reverse current node
            link = curr.next  # save the link to the next node
            curr.next = prev  # change the next link of current node
            if i < k:
                i += 1  # increment current k-group node index
                prev = curr
                curr = link
            else:
                i = 1
                n += 1
                start.next = link
                tail.next = curr
                tail = start  # update tail of reversed list so far
                start = link  # set next node as the 1st node in k group
                curr = link
        return dummy.next
