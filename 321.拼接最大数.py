#
# @lc app=leetcode.cn id=321 lang=python3
#
# [321] 拼接最大数
#
# https://leetcode-cn.com/problems/create-maximum-number/description/
#
# algorithms
# Hard (42.39%)
# Likes:    429
# Dislikes: 0
# Total Accepted:    27.4K
# Total Submissions: 64.6K
# Testcase Example:  '[3,4,6,5]\n[9,1,2,5,8,3]\n5'
#
# 给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n)
# 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
# 
# 求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
# 
# 说明: 请尽可能地优化你算法的时间和空间复杂度。
# 
# 示例 1:
# 
# 输入:
# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# 输出:
# [9, 8, 6, 5, 3]
# 
# 示例 2:
# 
# 输入:
# nums1 = [6, 7]
# nums2 = [6, 0, 4]
# k = 5
# 输出:
# [6, 7, 6, 0, 4]
# 
# 示例 3:
# 
# 输入:
# nums1 = [3, 9]
# nums2 = [8, 9]
# k = 3
# 输出:
# [9, 8, 9]
# 
#

# @lc code=start
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # 1. find max sequence in nums1 and nums2
        # 2. merge

        def merge(a, b):
            res = []
            while a or b:
                bigger = a if a>b else b
                res.append(bigger.pop(0))
            return res 
        
            
        def maxSequences(nums, size):
            stack = []
            drop = len(nums) - size
            for num in nums:
                while drop and stack and stack[-1]<num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:size]
        
        # def bigger(a, b):
        #     for x, y in zip()

        m, n = len(nums1), len(nums2)
        start, end = max(0, k-n), min(k, m)

        res = []
        for i in range(start, end+1):
            a = maxSequences(nums1, i)
            b = maxSequences(nums2, k-i)
            merged = merge(a, b)
            if merged > res:
                res = merged
            # res = bigger(merged, res)
        return res


if __name__ == "__main__":
    s = Solution()
    s.maxNumber([6,7], [6, 0, 4], 5)
# @lc code=end

