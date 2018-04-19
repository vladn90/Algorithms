""" Problem statement:
https://www.interviewbit.com/problems/copy-list/
"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        """ Creates a deep copy of a linked list with random pointer.
        Returns head of a new list.
        Time complexity: O(n). Space complexity: O(n), n is len(linked list).
        """
        # create a dictionary
        # where key=original node, value=node's copy with original value
        nodes = {None: None}  # for convinience when .next or .random is None
        curr = head
        while curr:
            nodes[curr] = RandomListNode(curr.label)
            curr = curr.next

        # copy next and random pointers for each node's copy
        curr = head
        while curr:
            nodes[curr].next = nodes[curr.next]  # copy next pointer
            nodes[curr].random = nodes[curr.random]  # copy random pointer
            curr = curr.next
        return nodes[head]  # link to the new head
