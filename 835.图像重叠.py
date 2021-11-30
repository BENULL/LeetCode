#
# @lc app=leetcode.cn id=835 lang=python3
#
# [835] 图像重叠
#
# https://leetcode-cn.com/problems/image-overlap/description/
#
# algorithms
# Medium (57.47%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    4.4K
# Total Submissions: 7.7K
# Testcase Example:  '[[1,1,0],[0,1,0],[0,1,0]]\n[[0,0,0],[0,1,1],[0,0,1]]'
#
# 给你两个图像 img1 和 img2 ，两个图像的大小都是 n x n ，用大小相同的二进制正方形矩阵表示。二进制矩阵仅由若干 0 和若干 1 组成。
# 
# 转换 其中一个图像，将所有的 1 向左，右，上，或下滑动任何数量的单位；然后把它放在另一个图像的上面。该转换的 重叠 是指两个图像 都 具有 1
# 的位置的数目。
# 
# 
# 
# 请注意，转换 不包括 向任何方向旋转。越过矩阵边界的 1 都将被清除。
# 
# 最大可能的重叠数量是多少？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
# 输出：3
# 解释：将 img1 向右移动 1 个单位，再向下移动 1 个单位。
# 
# 两个图像都具有 1 的位置的数目是 3（用红色标识）。
# 
# 
# 
# 示例 2：
# 
# 
# 输入：img1 = [[1]], img2 = [[1]]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：img1 = [[0]], img2 = [[0]]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# n == img1.length == img1[i].length
# n == img2.length == img2[i].length
# 1 <= n <= 30
# img1[i][j] 为 0 或 1
# img2[i][j] 为 0 或 1
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        """ brute force O(n^4)
        """
        N = len(img1)
        count = collections.Counter()
        for i, j in itertools.product(range(N),range(N)):
            if img1[i][j]:
                for x,y in itertools.product(range(N),range(N)):
                    if img2[x][y]:
                        count[i-x, j-y] += 1
        return max(count.values() or [0])
# @lc code=end

