#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (52.19%)
# Likes:    1184
# Dislikes: 0
# Total Accepted:    114.6K
# Total Submissions: 219.3K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = []
# 输出：0
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [["0"]]
# 输出：0
# 
# 
# 示例 4：
# 
# 
# 输入：matrix = [["1"]]
# 输出：1
# 
# 
# 示例 5：
# 
# 
# 输入：matrix = [["0","0"]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# rows == matrix.length
# cols == matrix[0].length
# 1 <= row, cols <= 200
# matrix[i][j] 为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 84题转化
       
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])

        left = [[0]*n for _ in range(m)]

         # 统计每个点最侧1的数量
        for i,j in itertools.product(range(m),range(n)):
            if matrix[i][j]== '1':
                left[i][j] = (0 if j == 0 else left[i][j - 1]) + 1

        # 单调栈 84 题做法 求柱状图最大矩形
        # 对于每一列，使用基于柱状图的方法

        res = 0
        for j in range(n):
            left_min, right_min = [0]*m, [0]*m 

            stack = []
            for i in range(m):
                while stack  and left[i][j]<= left[stack[-1]][j]:
                    stack.pop()
                left_min[i] = stack[-1] if stack else -1 
                stack.append(i)
            
            stack = []
            for i in range(m-1,-1,-1):
                while stack and left[i][j]<=left[stack[-1]][j]:
                    stack.pop()
                right_min[i] = stack[-1] if stack else m
                stack.append(i)
        
            for i in range(m):
                res = max(res, left[i][j]*(right_min[i]-left_min[i]-1))

        return res


                


        
# @lc code=end

