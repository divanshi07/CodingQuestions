class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        count = 0
        for i in range(cols):
            colsum = [0] * rows
            for j in range(i, cols):
                ht = collections.defaultdict(int)
                rowsum = 0
                ht[0] = 1
                for r in range(rows):
                    colsum[r] += matrix[r][j]
                    rowsum += colsum[r]
                    count += ht[rowsum-target]
                    ht[rowsum] += 1
                    
        return count