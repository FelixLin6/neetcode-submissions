class Solution:
    def __init__(self):
        self.bank = {}

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = -1, -1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                length = j - i
                if length == 1:
                    is_pal = True
                elif length == 2:
                    is_pal = s[i] == s[j - 1]
                else:
                    is_pal = self.bank[(i + 1, j - 1)] and s[i] == s[j - 1]

                self.bank[(i, j)] = is_pal

                if is_pal and length > end - start:
                        start, end = i, j

        if (start, end) == (-1, -1):
            return ""

        return s[start:end]