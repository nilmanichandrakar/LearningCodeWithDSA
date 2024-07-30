class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j= 0, 0
        len_s= len(s)
        lenOft=  len(t)
        while i < len_s and j < lenOft:
            if s[i] == t[j]:
                i =i+1
            j =j+ 1
        return i == len_s
        
