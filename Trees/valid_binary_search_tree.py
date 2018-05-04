""" Problem statement:
https://leetcode.com/problems/validate-binary-search-tree/description/
https://www.interviewbit.com/problems/valid-binary-search-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def is_valid(self, root, min_val, max_val):
        if not root:
            return True
        if min_val < root.val < max_val:
            return self.is_valid(root.left, min_val, root.val) \
                and self.is_valid(root.right, root.val, max_val)
        return False

    def isValidBST(self, root):
        return self.is_valid(root, float("-inf"), float("inf"))
