class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n= len(grid)
        res= 0
        for i in range(n):
            for j in range(n):
                res+= all(grid[i][k]== grid[k][j] for k in range(n))
    
        return res
