#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (78.60%)
# Likes:    536
# Dislikes: 0
# Total Accepted:    139.4K
# Total Submissions: 177.5K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        tar = n*n
        res = [[0]*n for _ in range(n)]
        times = 0
        num = 1
        while  num<=tar:
            if n==1:
                res[times][times] = num
                num += 1
            else:
                # top
                for i in range(n-1):
                    res[times][times+i] = num
                    num += 1
                # right
                for i in range(n-1):
                    res[times+i][times+n-1] = num
                    num += 1
                for i in range(n-1):
                    res[times+n-1][times+n-1-i] = num
                    num += 1
                for i in range(n-1):
                    res[times+n-1-i][times] = num
                    num += 1
            n -= 2
            times += 1
        return res
# @lc code=end

