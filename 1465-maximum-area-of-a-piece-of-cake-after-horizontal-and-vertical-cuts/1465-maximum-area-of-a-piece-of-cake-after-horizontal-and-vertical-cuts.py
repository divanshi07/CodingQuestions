class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(h)
        verticalCuts.append(w)
        horizontalCuts.append(0)
        verticalCuts.append(0)
        horizontalCuts.sort()
        verticalCuts.sort()
        maxDiff=0
        maxVDiff=0
        for i in range(0,len(horizontalCuts)-1):
            maxDiff=max(maxDiff,horizontalCuts[i+1]-horizontalCuts[i])
        for i in range(0,len(verticalCuts)-1):
            maxVDiff=max(maxVDiff,verticalCuts[i+1]-verticalCuts[i])
        return (maxDiff*maxVDiff)%((10**9)+7)
        