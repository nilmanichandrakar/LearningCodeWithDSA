class Solution:
    def tribonacci(self, n: int) -> int:
        x, y,z= 0, 1, 1
        for _ in range(n):
            x, y, z = y, z, x + y + z
        return x
