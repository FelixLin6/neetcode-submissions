class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = 1
        right_prod = 1
        res = [1] * len(nums)
        
        for i in range(len(nums) - 1):
            left_prod *= nums[i]
            res[i + 1] *= left_prod
            
        for i in range(len(nums) - 1, 0, -1):
            right_prod *= nums[i]
            res[i - 1] *= right_prod

        return res