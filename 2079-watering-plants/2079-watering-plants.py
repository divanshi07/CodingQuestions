class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        temCap=capacity
        myStep=0
        myCap=capacity
        for i in range(0,len(plants)):
            if(myCap>=plants[i]):
                myStep+=1
                myCap-=plants[i]
            else:
                myStep+=(2*i)+1
                myCap=capacity-plants[i]
        return myStep
                