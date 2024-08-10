class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        r= len(nums)-1
        nums.sort()
        l, res = 0, 0
        while l < r:
            s = nums[l] + nums[r]
            if s == k:
                res =res+ 1
                l, r = l + 1, r - 1
            elif s > k:
                r =r- 1
            else:
                l =l+ 1
        return res
        
