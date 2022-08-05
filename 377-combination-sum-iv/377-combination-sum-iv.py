class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0]*target

        for t in range(1, target+1):
            for i in range(bisect_right(nums, t)):
                dp[t] += dp[t-nums[i]]

        return dp[-1]