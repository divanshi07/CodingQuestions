class Solution:
    dp=[]
    def fib(self, n: int) -> int:
        global dp 
        dp=[-1]*31
        dp[0]=0
        dp[1]=1
        if(dp[n]!=-1):
            return dp[n]
        ans = self.fib(n-1)+self.fib(n-2)
        dp[n]=ans
        return ans