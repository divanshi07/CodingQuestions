class Solution:
    def reverse(self, x: int) -> int:            
        temp = str(x)
        if temp[0]=='-':
            newRev = temp[1:]
            finalRes = "-" + newRev[::-1]
        else:
            finalRes=temp[::-1]
            # -2147483648
        print(int(finalRes))
        if(int(finalRes)>=-2147483648 and int(finalRes)<=2147483648):
            return int(finalRes)
        else:
            return 0
            
        