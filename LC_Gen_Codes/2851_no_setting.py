class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        n = len(s)
        dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]
        
        # Base case: when s and t are equal after 0 moves
        for i in range(n + 1):
            dp[i][i][0] = 1
        
        for m in range(1, k + 1):
            for i in range(1, n + 1):
                for j in range(i, n + 1):
                    # If we can transform s[i:] to t[j:] in m-1 moves,
                    # then we can transform s[i-1:] to t[j-1:] in m moves
                    dp[i][j][m] += dp[i-1][j-1][m-1]
                    
                    # If we can transform s[i:] to t[j+1:] in m-1 moves,
                    # then we can transform s[i-1:] to t[j:] in m moves
                    dp[i][j][m] += dp[i-1][j][m-1]
                    
                    dp[i][j][m] %= (10**9 + 7)
        
        return dp[n][n][k]