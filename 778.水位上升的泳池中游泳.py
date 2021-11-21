#
# @lc app=leetcode.cn id=778 lang=python3
#
# [778] 水位上升的泳池中游泳
#
# https://leetcode-cn.com/problems/swim-in-rising-water/description/
#
# algorithms
# Hard (59.38%)
# Likes:    200
# Dislikes: 0
# Total Accepted:    24.1K
# Total Submissions: 40.7K
# Testcase Example:  '[[0,2],[1,3]]'
#
# 在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。
# 
# 现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t
# 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。
# 
# 你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？
# 
# 
# 
# 示例 1:
# 
# 
# 输入: [[0,2],[1,3]]
# 输出: 3
# 解释:
# 时间为0时，你位于坐标方格的位置为 (0, 0)。
# 此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
# 
# 等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
# 
# 
# 示例2:
# 
# 
# 输入:
# [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# 输出: 16
# 解释:
# ⁠0  1  2  3  4
# 24 23 22 21  5
# 12 13 14 15 16
# 11 17 18 19 20
# 10  9  8  7  6
# 
# 最终的路线用加粗进行了标记。
# 我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
# 
# 
# 
# 
# 提示:
# 
# 
# 2 .
# grid[i][j] 是 [0, ..., N*N - 1] 的排列。
# 
# 
#

# @lc code=start
class Solution:
    def swimInWater(self, grid) -> int:
        # bfs parcial accept 
        # N = len(grid)
        # visited = [[-1]*N for _ in range(N)]
        # visited[0][0] = grid[0][0]
        # queue = [(0,0)]
        # while queue:
        #     i, j = queue.pop(0)
        #     t = visited[i][j]
            
        #     for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
        #         if 0<=i+x<N and 0<=j+y<N:
                
        #             if visited[i+x][j+y]==-1:
        #                 if grid[i+x][j+y]<=t:
        #                     visited[i+x][j+y] = t
        #                 else:
        #                     visited[i+x][j+y] = grid[i+x][j+y]
        #                 queue.append((i+x,j+y))
        #             elif grid[i+x][j+y]<=t and visited[i+x][j+y]>t:
        #                 visited[i+x][j+y] = t
        #                 queue.append((i+x,j+y))        
        # return visited[N-1][N-1]



        # bfs + binary search
        N = len(grid)
        left, right = 0, N*N-1

        def bfs(mid):
            visited = {grid[0][0]}
            queue = [(0,0)]
            while queue:
                i, j = queue.pop(0)
                for x, y in [(0,1),(0,-1), (1,0),(-1,0),]:
                    if 0<=i+x<N and 0<=j+y<N and \
                        grid[i+x][j+y] not in visited and \
                        grid[i+x][j+y] <= mid:
                        if i+x==N-1 and j+y==N-1:
                            return True
                        queue.append((i+x,j+y))
                        visited.add(grid[i+x][j+y])
            return False
            
        while left<right:
            mid = left + (right-left) // 2
            if bfs(mid) and grid[0][0]<=mid:
                right = mid
            else:
                left = mid + 1
        return left


        

if __name__ == '__main__':
    s = Solution()
    s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
)

# @lc code=end

