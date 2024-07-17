class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n= len(nums)
        new_nums =[0]* (2*n)

        for i in range(n):
            new_nums[i]=nums[i]
            new_nums[i+n]=nums[i]
        return new_nums

      #another method
      #return nums*2
