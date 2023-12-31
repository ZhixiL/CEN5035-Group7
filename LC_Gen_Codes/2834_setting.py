class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            dp[i][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod
                if j >= i:
                    dp[i][j] = (dp[i][j] + dp[i-1][j-i]) % mod
        
        return dp[n][target]