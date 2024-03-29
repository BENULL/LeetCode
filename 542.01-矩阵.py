#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
# https://leetcode-cn.com/problems/01-matrix/description/
#
# algorithms
# Medium (45.88%)
# Likes:    525
# Dislikes: 0
# Total Accepted:    70.9K
# Total Submissions: 154.9K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。
# 
# 两个相邻元素间的距离为 1 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：[[0,0,0],[0,1,0],[0,0,0]]
# 
# 
# 示例 2：
# 
# 
# 
# 
# 输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
# 输出：[[0,0,0],[0,1,0],[1,2,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 
# 1 
# mat[i][j] is either 0 or 1.
# mat 中至少有一个 0 
# 
# 
#

# @lc code=start
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        dp
        """
        # m, n = len(mat), len(mat[0])
        # dp = [[float('inf')]*n for _ in range(m)]
        # for i, j in itertools.product(range(m), range(n)):
        #     if mat[i][j] == 0:
        #         dp[i][j] = 0
        # for i in range(m):
        #     for j in range(n):
        #         if i - 1 >= 0:
        #             dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
        #         if j - 1 >= 0:
        #             dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        # # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if i + 1 < m:
        #             dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
        #         if j + 1 < n:
        #             dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        # return dp
        """
        bfs
        """
        m, n = len(mat), len(mat[0])
        dist = [[0]*n for _ in range(m)]
        q = [(i,j) for i, j in itertools.product(range(m),range(n)) if mat[i][j]==0]
        visited = set(q)
        while q:
            i, j = q.pop(0)
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    visited.add((ni, nj))
        return dist





# @lc code=end

