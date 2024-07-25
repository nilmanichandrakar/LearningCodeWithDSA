class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        h = {chr(i) : i-64 for i in range(65, 65+26)}
        s= columnTitle
        n = len(s)

        res=0
        mul= 1
        for i in range(n-1, -1, -1):
            res+= h[s[i]]* mul
            mul *=26
        return res
