class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        dp = [[float('inf')] * (n+1) for _ in range(n+1)]
        dp[0][0] = 0
        
        for i in range(1, n+1):
            dp[i][1] = dp[i-1][1] + cost[i-1]
            for j in range(2, i+1):
                dp[i][j] = min(dp[i-1][j-1] + cost[i-1], dp[i-1][j])
        
        min_cost = float('inf')
        for i in range(1, n+1):
            min_cost = min(min_cost, max(dp[n][i], time[n-i]))
        
        return min_cost