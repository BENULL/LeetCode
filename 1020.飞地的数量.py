#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#
# https://leetcode-cn.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (59.83%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    35.7K
# Total Submissions: 58.8K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# 给你一个大小为 m x n 的二进制矩阵 grid ，其中 0 表示一个海洋单元格、1 表示一个陆地单元格。
# 
# 一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
# 
# 返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：所有 1 都在边界上或可以到达边界。
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] 的值为 0 或 1
# 
# 
#

# @lc code=start
from curses.ascii import SO, SP


class Solution:
    def numEnclaves(self, grid) -> int:
        
        def dfs(i,j):
            visted[i][j]=1
            cnt = 1
            flag = False
            for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                r = i + x
                c = j + y
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    if grid[r][c]==1 and visted[r][c]==0:
                        can, num = dfs(r,c)
                        cnt += num
                        flag = flag or can
                else:
                    flag = True
            return flag, cnt
                
                
        # dfs
        cnt = 0
        visted = [[0]*len(row) for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visted[i][j]==0 and grid[i][j]==1:
                    flag, num = dfs(i,j) 
                    cnt += (num if not flag else 0)
        return cnt
    
if __name__ == "__main__":
    s = Solution()
    s.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]])
    

# @lc code=end

