class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        firstOcc=-1
        lastOcc=-1
        while(left<=right):
            mid=left + (right-left)//2
            if(nums[mid]==target):
                firstOcc=mid
                right=mid-1
            elif(target<nums[mid]):
                right=mid-1
            else:
                left=mid+1
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=left + (right-left)//2
            if(nums[mid]==target):
                lastOcc=mid
                left=mid+1
            elif(target<nums[mid]):
                right=mid-1
            else:
                left=mid+1
        result=[firstOcc,lastOcc]
        return result