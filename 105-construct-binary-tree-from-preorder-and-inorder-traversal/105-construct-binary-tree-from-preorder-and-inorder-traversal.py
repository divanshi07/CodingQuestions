# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, A: List[int], B: List[int]) -> Optional[TreeNode]:
        return self.createBinary(A,B,0,len(A)-1,0,len(B)-1)
    def createBinary(self,A,B,ps,pe,ins,ine):
        if(ps>pe):
            return None 

        rootVal=A[ps]
        root = TreeNode(rootVal)
        index=0 
        for i in range(ins,ine+1):
            if(B[i]==rootVal):
                index=i 
                break 
        root.left=self.createBinary(A,B,ps+1,ps+index-ins,ins,index-1)
        root.right=self.createBinary(A,B,ps+index-ins+1,pe,index+1,ine)
        return root