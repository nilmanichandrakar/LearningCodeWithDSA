class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        left_arr =[0]*n
        right_arr= [0]*n
        l=1
        r=1

        for i, num in enumerate(nums):
            left_arr[i] =l
            j= -i- 1
            right_arr[j]= r
            l=l*nums[i]
            r =r*nums[j]
        
        return [l*r for l, r in zip(left_arr, right_arr)]
