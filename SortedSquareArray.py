class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        return sorted(nums)
        n= len(nums)
        result=[0]*n
        f, l=0, n-1
        for i in range(n-1, -1, -1):
            if abs(num[f] > abs(nums[l])):
                val=nums[f]
                f += 1
            else:
                val=nums[l]
                l -= 1
            result[i] =val **2
        return result
