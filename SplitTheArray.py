class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dictn = Counter(nums)

        for c in dictn.values():
            if c > 2:
                return False
            
        return True
        
