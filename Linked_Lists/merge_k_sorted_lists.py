""" Problem statement:
https://leetcode.com/problems/merge-k-sorted-lists/description/
"""
from queue import PriorityQueue


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class SolutionNaive:
    def mergeKLists(self, lists):  # correct solution, but TLE
        """ Merges sorted linked lists from array lists into one linked list.
        Returns head of a new linked list.
        Choose the node with min value from all the lists, attach it to the new
        list. Move head pointer of choosen list 1 node ahead. Repeat until
        we don't have any nodes left.

        Time complexity: O(n * k). Space complexity: O(1),
        n is a total number of nodes in all linked lists, k is len(lists).
        """
        n = len(lists)
        dummy = ListNode(None)
        tail = dummy  # current tail of a new linked list

        while True:  # choose min value from current nodes of linked lists
            min_val = float("inf")
            j = None  # index of current linked list with min node
            for i in range(n):
                if lists[i] and lists[i].val < min_val:
                    min_val = lists[i].val
                    j = i
            if j == None:  # no nodes left
                break
            tail.next = lists[j]
            tail = tail.next
            lists[j] = lists[j].next
        return dummy.next  # return head of a new list


class SolutionSort:
    def mergeKLists(self, lists):
        """ Merges sorted linked lists from array lists into one linked list.
        Returns head of a new linked list.
        Collect all the nodes values from all the linked lists into array.
        Sort the array. Create a new linked list from sorted array.

        Time complexity: O(n * lg(n)). Space complexity: O(n),
        n is a total number of nodes in all linked lists.
        """
        # collect all values from all nodes from all linked lists into array
        values = []
        for curr in lists:
            while curr:
                values.append(curr.val)
                curr = curr.next

        values.sort()  # sort the array of values

        # create a new linked list out of sorted values
        dummy = tail = ListNode(None)
        for v in values:
            node = ListNode(v)
            tail.next = node
            tail = tail.next
        return dummy.next


class SolutionQueue:
    def mergeKLists(self, lists):
        """ Merges sorted linked lists from array lists into one linked list.
        Returns head of a new linked list.
        Optimize the naive solution by using priority queue.

        Time complexity: O(n * lg(k)). Space complexity: O(n),
        n is a total number of nodes in all linked lists, k is len(lists).
        """
        # loop over array lists and from each linked lists
        # put 1st node, its value and current list index into priority queue
        dummy = tail = ListNode(None)  # tail is current tail of a new linked list
        node_queue = PriorityQueue()
        for i, node in enumerate(lists):
            if node:
                node_queue.put((node.val, i, node))  # we can't compare nodes directly

        # extract min node, attach it to the list, add next node to the queue
        while not node_queue.empty():
            value, i, tail.next = node_queue.get()  # extract node object
            tail = tail.next  # move pointer to the just added node
            if tail.next:  # put the next node of the current list into queue
                node_queue.put((tail.next.val, i, tail.next))
        return dummy.next


class SolutionDivideAndConquer:
    def merge(self, head1, head2):
        """ Merges two sorted linked lists and returns head of a new list.
        Time complexity: O(m + n). Space complexity: O(1),
        m, n are lengths of linked lists.
        """
        dummy = tail = ListNode(None)
        while head1 and head2:
            if head1.val <= head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2
        return dummy.next

    def mergeKLists(self, lists):
        """ Merges sorted linked lists from array lists into one linked list.
        Returns head of a new linked list.
        Start by combining each linked list with the next one. Then combine
        resulting linked lists with the next ones and so on. Repeat until
        there's only one linked list left, return its head.
        Implementation is similar to implementing bottom-up merge sort.

        Time complexity: O(n * lg(k)). Space complexity: O(1),
        n is a total number of nodes in all linked lists, k is len(lists).
        """
        n = len(lists)
        step = 1
        while step < n:
            for i in range(0, n, step * 2):
                left = lists[i]
                if i + step > n - 1:  # nothing to merge
                    continue
                right = lists[i + step]
                lists[i] = self.merge(left, right)
            step *= 2
        return lists[0] if n > 0 else None
