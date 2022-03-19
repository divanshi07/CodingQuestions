'''
        0  1  0  2  1  0  1  3  2  1  2  1
maxL    0           2
maxR    3           3
            

    
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        maxL=[0]*len(height)
        maxR=[0]*len(height)
        myRes=0
        maxL[0]=height[0]
        for i in range(1,len(height)):
            maxL[i]=max(maxL[i-1],height[i])
        maxR[len(height)-1]=height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            maxR[i]=max(maxR[i+1],height[i])
        for i in range(len(height)):
            myRes+=min(maxL[i],maxR[i])-height[i]

        return myRes

        
        
            
        