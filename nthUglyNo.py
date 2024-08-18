class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = [1]
        visited = {1}
        res = 1
        for _ in range(n):
            res = heappop(h)
            for v in [2, 3, 5]:
                nxt = res * v
                if nxt not in visited:
                    visited.add(nxt)
                    heappush(h, nxt)
        return res
