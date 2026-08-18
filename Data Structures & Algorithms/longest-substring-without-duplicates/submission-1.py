class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        if len(s) == 1:
            return 1

        curr = set()
        res = 0
        
        l, r = 0, 0

        while r < len(s):
            if s[r] in curr:
                curr.remove(s[l])
                l += 1
            else:
                curr.add(s[r])
                r += 1
            res = max(len(curr), res)

        return res