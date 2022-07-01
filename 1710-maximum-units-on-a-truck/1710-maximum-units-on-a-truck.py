class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        mySortedArr=sorted(boxTypes, key=lambda x: x[1], reverse=True)
        i=0
        myAmount=0
        while(truckSize>0 and i<len(mySortedArr)):
            if(truckSize>=mySortedArr[i][0]):
                myAmount+=mySortedArr[i][0]*mySortedArr[i][1]
                # print("first if",mySortedArr[i][0],mySortedArr[i][1])
                truckSize-=mySortedArr[i][0]
            elif(truckSize<mySortedArr[i][0]):
                myAmount+=(truckSize)*mySortedArr[i][1]
                # print("second if",mySortedArr[i][0]-truckSize,mySortedArr[i][1])
                return myAmount
            i+=1 
        return myAmount
                
                