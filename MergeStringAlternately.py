class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1= len(word1)
        l2= len(word2)
        res= ""
        n= max(l1,l2)
        for i in range(n):
            if i<l1:
                res=res+word1[i]
            if i<l2:
                res=res+word2[i]
        return res
