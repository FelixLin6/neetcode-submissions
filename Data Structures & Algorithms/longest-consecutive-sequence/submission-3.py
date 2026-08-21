class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = 0
        for n in numbers:
            curr = n
            if curr - 1 not in numbers:
                seq_len = 1
                while curr + 1 in numbers:
                    seq_len += 1
                    curr += 1
                res = max(res, seq_len)
        return res