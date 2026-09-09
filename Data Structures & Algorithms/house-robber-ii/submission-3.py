class Solution:
    def rob1(self, nums: List[int]) -> int:
        bank = {}
        res = 0
        for i in range(len(nums)):
            if i == 0: bank[i] = max(0, nums[i])
            elif i == 1: bank[i] = max(0, max(nums[i], nums[i-1]))
            else:
                bank[i] = max(bank[i-1], bank[i-2] + nums[i])
            res = max(res, bank[i])
        return res

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.rob1(nums[1:]), self.rob1(nums[:-1]))
