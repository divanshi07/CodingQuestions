class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if(len(nums)==0):
            return 0
        myCount=1
        myMax=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if nums[i]-nums[i-1]==1:
                    myCount+=1
                else:
                    myMax=max(myMax,myCount)
                    myCount=1 
        return max(myMax,myCount)
                    