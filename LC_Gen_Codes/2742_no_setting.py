class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[float('inf')] * 2 for _ in range(n+1)]
        
        dp[0][0] = dp[0][1] = 0
        
        for i in range(1, n+1):
            dp[i][0] = cost[i-1] + min(dp[i-1][0], dp[i-1][1])
            dp[i][1] = time[i-1] + dp[i-1][0]
        
        return min(dp[n][0], dp[n][1])