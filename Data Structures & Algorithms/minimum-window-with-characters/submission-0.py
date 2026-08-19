class Solution:
    def minWindow(self, s: str, t: str) -> str:

        countW, countT = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, res_len = [-1, -1], float("+inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            countW[c] = 1 + countW.get(c, 0)
            if c in countT and countW[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1 < res_len):
                    res, res_len = [l, r], r - l + 1
                countW[s[l]] -= 1
                if s[l] in countT and countW[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l: r + 1] if res_len != float("+inf") else ""

        
            