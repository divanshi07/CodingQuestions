class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        a=[]
        for r in matrix:
            a.extend(r)
        return sorted(a)[k-1]        