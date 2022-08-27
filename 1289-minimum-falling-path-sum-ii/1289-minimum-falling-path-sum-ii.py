class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        h = w = len(arr)
        
        ## Base case:
        # top row
        if h == 1:
            return arr[0][0]
        
        ## General case: 
        # current cost + minimal cost of neighbor on previous row
        for y in range(1, h):
            
            for x in range(w):
                
                arr[y][x] = arr[y][x] + min( arr[y-1][perv_neighbor] for perv_neighbor in range(w) if perv_neighbor != x )
        
        return min( arr[h-1] )