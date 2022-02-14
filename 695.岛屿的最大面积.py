#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (67.04%)
# Likes:    686
# Dislikes: 0
# Total Accepted:    163.7K
# Total Submissions: 244.1K
# Testcase Example:  '[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
#
# 给你一个大小为 m x n 的二进制矩阵 grid 。
# 
# 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid
# 的四个边缘都被 0（代表水）包围着。
# 
# 岛屿的面积是岛上值为 1 的单元格的数目。
# 
# 计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid =
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 输出：6
# 解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [[0,0,0,0,0,0,0,0]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] 为 0 或 1
# 
# 
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        cnt = 0
        def dfs(i,j):
            visted[i][j]=1
            nonlocal cnt 
            cnt += 1
            for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                r = i+x
                c = j+y
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]==1 and visted[r][c]==0:
                    dfs(r,c)
        # dfs
        max_cnt = 0
        visted = [[0]*len(row) for row in grid]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visted[i][j]==0 and grid[i][j]==1:
                    dfs(i,j)
                    max_cnt = max(max_cnt,cnt)
                    cnt = 0
        return max_cnt

if __name__ == '__main__':
    s = Solution()
    s.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
)
    
# @lc code=end

