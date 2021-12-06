#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#
# https://leetcode-cn.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (66.86%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    24.7K
# Total Submissions: 36.8K
# Testcase Example:  '[[2,1,3],[6,5,4],[7,8,9]]'
#
# 给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。
# 
# 下降路径
# 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置
# (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1)
# 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
# 输出：13
# 解释：下面是两条和最小的下降路径，用加粗+斜体标注：
# [[2,1,3],      [[2,1,3],
# ⁠[6,5,4],       [6,5,4],
# ⁠[7,8,9]]       [7,8,9]]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[-19,57],[-40,-5]]
# 输出：-59
# 解释：下面是一条和最小的下降路径，用加粗+斜体标注：
# [[-19,57],
# ⁠[-40,-5]]
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [[-48]]
# 输出：-48
# 
# 
# 
# 
# 提示：
# 
# 
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix) -> int:
        # bfs TLE
        # n = len(matrix)
        # res = float('inf')
        # queue = [(0, i, matrix[0][i]) for i in range(n)]
        # memo = {(0,i):matrix[0][i] for i in range(n)}
        # while queue:
        #     i, j, val = queue.pop(0)
        #     if (i, j)in memo and memo[(i,j)]<val:
        #         continue
        #     memo[(i,j)] = val
        #     if i==n-1:
        #         res = min(res, val)
        #         continue
        #     for y in (-1,0,1):
        #         if i+1<n and 0 <= j+y < n:
        #             queue.append((i+1,j+y,val+matrix[i+1][j+y]))
        # return res

        # recursive

        # 2d dp
        # n = len(matrix)
        # dp = [[0]*n for _ in range(n)]
        # dp[0] = matrix[0]
        # for i in range(1,n):
        #     for j in range(n):
        #         a = dp[i-1][j] if 0<=j<n else float('inf')
        #         b = dp[i-1][j-1] if 0<=j-1<n else float('inf')
        #         c = dp[i-1][j+1] if 0<=j+1<n else float('inf')
        #         dp[i][j] = matrix[i][j]+min(a,b,c)
        # return min(dp[n-1])

        #  dp     
        while len(matrix) >= 2:
            row = matrix.pop()            
            for i in range(len(row)):
                matrix[-1][i] += min(row[max(0,i-1): min(len(row), i+2)])
        return min(matrix[0])

if __name__ == "__main__":
    s = Solution()
    s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])             

# @lc code=end

