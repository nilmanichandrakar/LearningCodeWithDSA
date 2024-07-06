class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cntr1= Counter(s)  #hashmap
        cntr2= Counter(t)  #hashmap

        return cntr1==cntr2
        
