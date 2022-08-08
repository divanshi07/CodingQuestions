class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        lis = [1]*n
        for i in range(1, n):
            for j in range(0, i):
                if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j]+1
        maximum = 0

        # Pick maximum of all LIS values
        for i in range(n):
            maximum = max(maximum, lis[i])

        return maximum