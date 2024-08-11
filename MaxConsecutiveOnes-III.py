class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l =0 
        cnt=0
        for x in nums:
            cnt += x ^ 1
            if cnt > k:
                cnt -= nums[l] ^ 1
                l =l+ 1
        return len(nums) - l
