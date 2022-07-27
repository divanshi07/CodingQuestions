# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root != None:
            curr = TreeNode(0)
            record = curr
            stack = [root]
            while stack:
                u = stack.pop()
                curr.left = None
                curr.right = u
                curr = u
                if u.right != None:
                    stack.append(u.right)
                if u.left != None:
                    stack.append(u.left)
            root = record.right
        return root