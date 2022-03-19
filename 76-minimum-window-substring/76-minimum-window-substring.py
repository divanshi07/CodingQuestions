class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s)<len(t):
            return ""
        elif 1>len(s):
            return ""
        myDict={}
        for i in t:
            if i in myDict:
                myDict[i]+=1
            else:
                myDict[i]=1
        i=0
        j=0
        mini=float("Inf") 
        window=""
        myCount=len(myDict)
        while(j<len(s)):
            if s[j] in myDict:
                myDict[s[j]]-=1
                if myDict[s[j]]==0:
                    myCount-=1
            while(myCount==0 and i<=j):
                if mini > j-i+1:
                    mini = j-i+1                    
                    window=s[i:j+1] 
                if s[i] in myDict:
                    myDict[s[i]]+=1
                    if myDict[s[i]]==1:
                        myCount+=1
                i+=1
            j+=1
        return window 