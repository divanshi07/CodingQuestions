class Solution:
    global dp;
    dp=[-1]*46
    def climbStairs(self, n: int) -> int:
        global dp
        if n<=2:
            return n
        if(dp[n]!=-1):
            return dp[n]
        ans = self.climbStairs(n-1)+self.climbStairs(n-2)
        dp[n]=ans
        return dp[n]
        