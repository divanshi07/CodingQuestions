class Solution:
    def firstUniqChar(self, s: str) -> int:
        myDict={}
        for i in s:
            myDict[i]=s.count(i)
            if myDict[i]==1:
                return s.index(i)
        return -1