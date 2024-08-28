class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for x in s:
            if x == '*':
                res.pop()
            else:
                res.append(x)
        return ''.join(res)
        
