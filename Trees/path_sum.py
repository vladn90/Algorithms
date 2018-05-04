""" Problem statement:
https://leetcode.com/problems/path-sum/description/
https://www.interviewbit.com/problems/path-sum/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def is_path(self, root, curr, s):
        if not root:  # empty subtree of non-leaf node
            return False
        if not root.left and not root.right:  # leaf node
            if curr + root.val == s:
                return True
            return False
        return self.is_path(root.left, curr + root.val, s) or self.is_path(root.right, curr + root.val, s)

    def hasPathSum(self, root, s):
        return self.is_path(root, 0, s)


class Solution:  # shorter version, no need for helper function with extra argument
    def hasPathSum(self, root, s):
        if not root:  # empty subtree of non-leaf node
            return False
        if not root.left and not root.right:  # leaf node
            if root.val == s:
                return True
            return False
        return self.hasPathSum(root.left, s - root.val) or self.hasPathSum(root.right, s - root.val)
