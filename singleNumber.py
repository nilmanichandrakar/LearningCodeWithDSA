class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        has = Counter(nums)
        for i in has:
            if has[i]==1:
                return i
