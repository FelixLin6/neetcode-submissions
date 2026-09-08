class Solution:
    def __init__(self):
        self.dp = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        if self.dp.get(n):
            return self.dp.get(n)

        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]