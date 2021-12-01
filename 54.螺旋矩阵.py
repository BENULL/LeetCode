#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (48.22%)
# Likes:    920
# Dislikes: 0
# Total Accepted:    203.1K
# Total Submissions: 421K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# 
# 
#

# @lc code=start
class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix: return res
        m,n = len(matrix), len(matrix[0])
        times = 0
        while  n>0 and m>0:
            if m==1:
                res.extend(matrix[times][i+times] for i in range(n))
            elif n == 1:
                res.extend(matrix[i+times][times] for i in range(m))
            else:
                # top
                res.extend(matrix[times][times+i] for i in range(n-1))
                # right
                res.extend(matrix[times+i][times+n-1] for i in range(m-1))
                # bottom
                res.extend(matrix[times+m-1][times+n-1-i] for i in range(n-1))
                # left
                res.extend(matrix[times+m-1-i][times] for i in range(m-1))
            m -= 2
            n -= 2
            times += 1
        return res


# @lc code=end

