class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = 0
        for n in numbers:
            if n - 1 not in numbers:
                seq_len = 1
                while n + seq_len in numbers:
                    seq_len += 1
                res = max(res, seq_len)
        return res