# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root is None):
            return 
        res=[]
        queue=[]
        queue.append(root)
        while(len(queue)):
            myVal=[]
            for i in range(0,len(queue)):
                myTop=queue.pop(0)
                myVal.append(myTop.val)
                if(myTop.left is not None):
                    queue.append(myTop.left)
                if(myTop.right is not None):
                    queue.append(myTop.right)
            res.append(myVal[len(myVal)-1])
        return res