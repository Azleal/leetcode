# -*- coding: utf-8 -*-
import math


class Solution:
    def maximalSquare(self, matrix) -> int:
        if len(matrix) == 0:
            return 0

        max_square_edge = min(len(matrix),len(matrix[0]))
        max_square_area = 0

        square_row = len(matrix)
        square_column = len(matrix[0])

        info = [[[ False for _ in range(max_square_edge + 1)] for _ in range(len(matrix[0]))  ] for _ in range(len(matrix)) ]

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):


        return max_square_area




# matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"],["1","0","0","1","0"]]
# matrix=[["1","1"],["1","1"]]
matrix=[["1","1","1","1"],["1","1","1","1"],["1","1","1","1"]]
max_square_edge = int(math.log(min(len(matrix),len(matrix[0])),2))
r=Solution().maximalSquare(matrix)
print(r)


