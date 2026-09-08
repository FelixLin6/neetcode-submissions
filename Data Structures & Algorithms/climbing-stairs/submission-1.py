class Solution:
    def __init__(self):
        self.dp = {}

    def climbStairs(self, n: int) -> int:
        if n <= 0: 
            self.dp[n] = 0
            return 0
        if n == 1: 
            self.dp[n] = 1
            return 1
        if n == 2:
            self.dp[n] = 2
            return 2

        if self.dp.get(n):
            return self.dp.get(n)

        x, y = self.climbStairs(n-1), self.climbStairs(n-2)
        self.dp[n] = x + y
        return x + y