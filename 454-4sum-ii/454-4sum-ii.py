class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        myDict={}
        for i in nums4:
            for j in nums3:
                if (i+j) in myDict:
                    myDict[i+j]+=1
                else:
                    myDict[i+j]=1
        count=0
        for k in nums1:
            for l in nums2:
                target = 0-(k+l)
                if target in myDict:
                    count+=myDict[target]
        return count