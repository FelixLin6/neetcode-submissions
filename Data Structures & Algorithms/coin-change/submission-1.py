class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf')] * amount
        for n in range(0, amount + 1):
            for c in coins:
                if c <= n:
                    dp[n] = min(dp[n], dp[n - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1