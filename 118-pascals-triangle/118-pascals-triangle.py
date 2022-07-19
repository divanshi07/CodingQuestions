class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        matrix=[]
        firstRow=[1]
        secondRow=[1,1]
        matrix.append(firstRow)
        
        if(numRows==1):
            return matrix
        matrix.append(secondRow)

        for i in range(2,numRows):
            result=[]
            for j in range(0,i+1):
                if(j==0):
                    result.append(matrix[i-1][j])

                elif(j==i):
                    result.append(matrix[i-1][j-1])
                    # matrix[i][j]=matrix[i-1][j-1]
                else:
                    result.append(matrix[i-1][j] + matrix[i-1][j-1])
                    # matrix[i][j]=matrix[i-1][j] + matrix[i-1][j-1]
            matrix.append(result)
        return matrix