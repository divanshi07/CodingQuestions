class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        myDict={}
        maxLen=0
        while(j<len(s)):
            if s[j] in myDict:
                myDict[s[j]]+=1
            else:
                myDict[s[j]]=1
            if(j-i+1==len(myDict)):
                maxLen=max(maxLen,j-i+1)
                j+=1
            elif len(myDict)<j-i+1:
                while(len(myDict)<j-i+1):
                    myDict[s[i]]-=1
                    if myDict[s[i]]==0:
                        del myDict[s[i]]
                    i+=1
                j+=1
        return maxLen
            
            
                
                
        