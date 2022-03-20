class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col=len(matrix[0])-1
        row=len(matrix)
        i=0
        while(i<row):
            if(matrix[i][col]==target):
                return True
            elif matrix[i][col]>target:
                return binarySearch(matrix[i],target)
            elif(target>matrix[i][col]):
                i+=1
    
def binarySearch(arr,target):
    left=0
    right=len(arr)-1
    while(left<=right):
        mid = left + (right-left)//2
        if(target==arr[mid]):
            return True
        elif(target>arr[mid]):
            left=mid+1
        else:
            right=mid-1
    return False