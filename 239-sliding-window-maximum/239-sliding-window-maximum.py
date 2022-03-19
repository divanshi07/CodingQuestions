class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        j=0
        if(k==len(nums)):
            return [max(nums)]
        maxi=0
        maxEl=[]
        listMade=[]
        while(j<len(nums)):
            while(len(listMade)!=0 and listMade[len(listMade)-1]<nums[j]):
                listMade.pop()
            listMade.append(nums[j])
            if(j-i+1<k):
                j+=1
            elif(j-i+1==k):
                maxEl.append(listMade[0])
                if nums[i]==listMade[0]:
                    listMade.pop(0)
                i+=1
                j+=1
        return(maxEl)