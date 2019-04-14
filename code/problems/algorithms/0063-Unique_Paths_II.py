# -*- coding: utf-8 -*-
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        if len(obstacleGrid) == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for row in range(len(obstacleGrid)):
            for column in range(len(obstacleGrid[0])):
                if obstacleGrid[row][column] == 0:
                    if row > 0:
                        dp[row][column] += dp[row - 1][column]
                    if column > 0:
                        dp[row][column] += dp[row][column - 1]
        return dp[-1][-1]

obs=[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
r=Solution().uniquePathsWithObstacles(obs)
print(r)