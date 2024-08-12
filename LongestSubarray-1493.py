class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = zero_count = max_len = 0

        while right < n:
            if nums[right] == 0:
                zero_count += 1
            
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len - 1  
