class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        myStats=[0]*(len(cost))
        myStats[0]=cost[0]
        myStats[1]=cost[1]
        for i in range(2,len(cost)):
            myStats[i]=cost[i]+min(myStats[i-1],myStats[i-2])
        return min(myStats[-1],myStats[-2])