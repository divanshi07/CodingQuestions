# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, A: Optional[TreeNode]) -> List[List[int]]:
        myQueue, result = [], []
        if A:
            myQueue.append(A)
        while len(myQueue):
            myVal = []
            for _ in range(len(myQueue)):
                x = myQueue.pop(0)
                myVal.append(x.val)
                if x.left:
                    myQueue.append(x.left)
                if x.right:
                    myQueue.append(x.right)
            result.append(myVal)
        return result