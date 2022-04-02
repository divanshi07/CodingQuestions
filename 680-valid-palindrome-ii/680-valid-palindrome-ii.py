class Solution:
    def isPalindrome(self,s,low,high):
        while(low<high):
            if s[low]!=s[high]:
                return False 
            low+=1
            high-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        low=0
        high=len(s)-1
        for i in range(0,len(s)):
            while(low<high):
                if s[low]==s[high]:
                    low+=1
                    high-=1 
                else:
                    if self.isPalindrome(s,low+1,high):
                        return True 
                    if self.isPalindrome(s,low,high-1):
                        return True 
                    return False 
        return True
        
        