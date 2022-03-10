class Solution:
    """
        在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，
        每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，
        输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

        示例:

        现有矩阵 matrix 如下：

        [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
        ]
        给定 target = 5，返回 true。

        给定 target = 20，返回 false。

         
    """
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m-1
        while 0<=i<=n-1 and 0<=j<=m-1:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j -= 1
            else:
                i += 1
        return False

