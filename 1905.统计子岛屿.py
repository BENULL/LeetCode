#
# @lc app=leetcode.cn id=1905 lang=python3
#
# [1905] 统计子岛屿
#
# https://leetcode-cn.com/problems/count-sub-islands/description/
#
# algorithms
# Medium (61.48%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 12.4K
# Testcase Example:  '[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n' +
#'[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]'
#
# 给你两个 m x n 的二进制矩阵 grid1 和 grid2 ，它们只包含 0 （表示水域）和 1 （表示陆地）。一个 岛屿 是由 四个方向
# （水平或者竖直）上相邻的 1 组成的区域。任何矩阵以外的区域都视为水域。
# 
# 如果 grid2 的一个岛屿，被 grid1 的一个岛屿 完全 包含，也就是说 grid2 中该岛屿的每一个格子都被 grid1
# 中同一个岛屿完全包含，那么我们称 grid2 中的这个岛屿为 子岛屿 。
# 
# 请你返回 grid2 中 子岛屿 的 数目 。
# 
# 
# 
# 示例 1：
# 
# 输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# 输出：3
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。
# 
# 
# 示例 2：
# 
# 输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# 输出：2 
# 解释：如上图所示，左边为 grid1 ，右边为 grid2 。
# grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] 和 grid2[i][j] 都要么是 0 要么是 1 。
# 
# 
#

# @lc code=start
class Solution:
  def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    contain = True
    def dfs(i,j):
      if grid1[i][j]!=1:
        nonlocal contain
        contain = False
      grid2[i][j] = 0
      for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
          r = i+x
          c = j+y
          if 0 <= r < len(grid1) and 0 <= c < len(grid1[0]) and grid2[r][c]==1:
            dfs(r,c)
      
      # dfs
      
    res = 0
    for i in range(len(grid2)):
        for j in range(len(grid2[i])):
            if grid2[i][j]==1 and grid1[i][j]==1:
                dfs(i,j)
                if contain:
                  res+=1
                else:
                  contain=True
    return res
# @lc code=end

