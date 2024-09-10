class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        g = [[0] * n for _ in range(m)]
        g[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i:
                    g[i][j] += g[i - 1][j]
                if j:
                    g[i][j] += g[i][j - 1]
        return g[-1][-1]
