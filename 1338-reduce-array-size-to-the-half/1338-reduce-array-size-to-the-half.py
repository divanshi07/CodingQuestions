class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        myList = {}
        for i in arr:
            if i in myList:
                myList[i]+=1 
            else:
                myList[i]=1 
        myList = sorted(myList.items(), key=lambda x:x[1] ,reverse = True)
        mySet=set()
        maxLen = len(arr)
        myLen=0 
        count = 0
        for key,value in myList:
            maxLen -= value
            count += 1
            
            if maxLen <= len(arr)//2:
                return count

        return count
        
        