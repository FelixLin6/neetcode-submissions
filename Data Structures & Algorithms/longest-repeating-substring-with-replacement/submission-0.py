class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        l, r = 0, 0
        cnt = Counter()
        win_len = 0
        res = 0
        while r < len(s):
            win_len += 1
            cnt[s[r]] += 1
            used = win_len - max(cnt.values())
            if used > k:
                cnt[s[l]] -= 1
                win_len -= 1
                l += 1
            res = max(res, win_len)
            r += 1

        return res
