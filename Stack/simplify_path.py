""" Problem statement:
https://leetcode.com/problems/simplify-path/description/
"""


class Solution:
    def simplifyPath(self, path):
        """ Simplifies UNIX-like directory path and returns it.
        Time complexity: O(n). Space complexity: O(n), n is len(path).
        """
        pwd = []  # stack, present working directory
        path = path.split("/")
        for curr in path:
            if not curr or curr == ".":  # skip current dir
                continue
            elif curr == "..":
                if pwd:  # if we're not in the root directory, go back
                    pwd.pop()
            else:
                pwd.append(curr)
        return "/" + "/".join(pwd)
