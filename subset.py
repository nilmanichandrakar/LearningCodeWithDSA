class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        n= len(nums)
        
        def backtrack(i=0):
            if i==n:
                subset.append(res[:])
                return
            backtrack(i+1)

            res.append(nums[i])
            backtrack(i+1)
            res.pop()
        backtrack()
        return subset
        
        
