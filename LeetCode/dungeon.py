class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        if len(dungeon) ==0 or len(dungeon[0])==0:
            return 1
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[1 for i in range(n) ] for j in range(m) ] 
        dp[m-1][n-1] = max(1,1-dungeon[m-1][n-1])
        for i in range(m-2,-1,-1):
            dp[i][n-1] = max(1,dp[i+1][n-1]-dungeon[i][n-1])
        for i in range(n-2,-1,-1):
            dp[m-1][i] = max(1,dp[m-1][i+1]-dungeon[m-1][i])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] = max(1,min(dp[i+1][j],dp[i][j+1])-dungeon[i][j])
        return dp[0][0]
        