#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (46.59%)
# Likes:    6115
# Dislikes: 205
# Total Accepted:    781.9K
# Total Submissions: 1.7M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
# 
# 
# Example 1:
# 
# 
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
# 
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            visted[i][j]=1
            for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
                r = i+x
                c = j+y
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c]=='1' and visted[r][c]==0:
                    dfs(r,c)
        # dfs
        visted = [[0]*len(row) for row in grid]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visted[i][j]==0 and grid[i][j]=='1':
                    dfs(i,j)
                    res+=1
        return res
    
    

        
# @lc code=end

