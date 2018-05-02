""" Problem statement:
https://www.interviewbit.com/problems/symmetric-binary-tree/

Solution algorithm and description:
https://leetcode.com/problems/symmetric-tree/solution/
https://www.geeksforgeeks.org/symmetric-tree-tree-which-is-mirror-image-of-itself/
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SolutionLeetCode:
    def is_mirror(self, root1, root2):
        """ Returns True if two trees are mirror of one another, False otherwise.
        """
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.is_mirror(root1.left, root2.right) \
                and self.is_mirror(root1.right, root2.left)
        return False

    def isSymmetric(self, root):
        """ Returns True if binary tree is symmetric, False otherwise.
        Recursive algorithm.
        Time complexity: O(n). Space complexity: O(n), n is number of nodes.
        """
        if not root:  # empty tree
            return True
        if self.is_mirror(root.left, root.right):
            return True
        return False

    def isSymmetric(self, root):
        """ Returns True if binary tree is symmetric, False otherwise.
        Iterative algorithm.
        Time complexity: O(n). Space complexity: O(n), n is number of nodes.
        """
        queue = deque()
        queue.append(root)  # appending root twice makes further code shorter
        queue.append(root)
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            if not node1 and not node2:  # both subtrees are empty
                continue
            if not node1 or not node2:  # one subtree is empty, while another one isn't
                return False
            if node1.val != node2.val:
                return False
            # subtrees' root values are equal, enqueue their subtrees in the right order
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
        return True  # all checks went good, tree is symmetric


class SolutionInterviewBit:
    def is_mirror(self, root1, root2):
        """ Returns True if two trees are mirror of one another, False otherwise.
        """
        if not root1 and not root2:
            return True
        if root1 and root2 and root1.val == root2.val:
            return self.is_mirror(root1.left, root2.right) \
                and self.is_mirror(root1.right, root2.left)
        return False

    def isSymmetric(self, root):
        """ Returns True if binary tree is symmetric, False otherwise.
        Time complexity: O(n). Space complexity: O(n), n is number of nodes.
        """
        if not root:  # empty tree
            return 1
        if self.is_mirror(root.left, root.right):
            return 1
        return 0
