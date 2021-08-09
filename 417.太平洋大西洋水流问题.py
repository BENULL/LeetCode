#
# @lc app=leetcode.cn id=417 lang=python3
#
# [417] 太平洋大西洋水流问题
#
# https://leetcode-cn.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (46.53%)
# Likes:    259
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 48.3K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# 给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。
# 
# 规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。
# 
# 请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。
# 
# 
# 
# 提示：
# 
# 
# 输出坐标的顺序不重要
# m 和 n 都小于150
# 
# 
# 
# 
# 示例：
# 
# 
# 
# 
# 给定下面的 5x5 矩阵:
# 
# ⁠ 太平洋 ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * 大西洋
# 
# 返回:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # dfs 顺流而下 有错误 or TLE
        # if not heights or not heights[0]: return []
        # m, n = len(heights), len(heights[0])
        # vis = [[0]*n for _ in range(m)]
        # a_res = set()
        # p_res = set()
        
        # def dfs(i, j, flow):
        #     # vis[i][j] = 1
        #     flow.append(i*n+j)

        #     for direction in [[-1,0],[0,-1],[1,0],[0,1]]:
        #         x, y = i+direction[0], j+direction[1]
        #         if x==-1 or y==-1:
        #             p_res.update(flow)
        #             continue
        #         elif x==m or y==n:
        #             a_res.update(flow)
        #             continue
                
        #         if heights[x][y]>heights[i][j]:
        #             continue
        #         if x*n+y in flow:
        #             continue 
        #         if not vis[x][y]:
        #             dfs(x, y, flow[:])
        #         else:
        #             if x*n+y in a_res:
        #                 a_res.update(flow)
        #             if x*n+y in p_res:
        #                 p_res.update(flow)
                   
        # for i, j in itertools.product(range(m),range(n)):
        #     if not vis[i][j]:
        #         vis[i][j] = 1
        #         dfs(i, j, [])

        # return[ [index//n, index%n] for index in (a_res & p_res)]


        # dfs 逆流而上
        if not heights or not heights[0]: return []
        m, n = len(heights), len(heights[0])
        
        a_res = [[0]*n for _ in range(m)]
        p_res = [[0]*n for _ in range(m)]

        directions = [[-1,0],[0,-1],[1,0],[0,1]]

        def dfs(i, j, vis):
            vis[i][j]=1
            for direction in directions:
                _i, _j = i+direction[0], j+direction[1]
                if m>_i>=0 and n>_j>=0 and not vis[_i][_j] and heights[_i][_j]>=heights[i][j]:
                    dfs(_i, _j, vis)
                    
        # p
        for i, j in [[0,y] for y in range(n)]+[[x,0] for x in range(1,m)]:
            dfs(i, j, p_res)
            
        # a
        for i, j in [[m-1,y] for y in range(n)]+[[x,n-1] for x in range(m-1)]:
            dfs(i, j, a_res)

        return [[i,j] for i, j in itertools.product(range(m),range(n)) if a_res[i][j] and p_res[i][j]]

# @lc code=end

