class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numbers = set()
        k = 0

        for num in nums:
            if num not in numbers:
                nums[k] = num
                k += 1
                numbers.add(num)

        return k

            
