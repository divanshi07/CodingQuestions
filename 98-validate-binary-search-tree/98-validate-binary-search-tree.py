# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=[]
        self.inorder(root,res)
        for i in range(0,len(res)-1):
            if(res[i+1]<=res[i]):
                return 0
        return 1
        
    def inorder(self,A,res):
        if(A is None):
            return 
        self.inorder(A.left,res)
        res.append(A.val)
        self.inorder(A.right,res)
        
