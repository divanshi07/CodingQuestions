class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==1:
            if nums[0]==1:
                return 2
            return 1
        for i in range(0,len(nums)):
            if nums[i]<=0:
                nums[i]=len(nums)+1 
        for i in range(0,len(nums)):
            val = abs(nums[i])-1
            if val<len(nums):
                nums[val]=-1*abs(nums[val])
        for i in range(0,len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1