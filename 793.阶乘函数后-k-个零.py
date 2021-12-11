#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#
# https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function/description/
#
# algorithms
# Hard (39.35%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    5.5K
# Total Submissions: 13.9K
# Testcase Example:  '0'
#
#  f(x) 是 x! 末尾是 0 的数量。（回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 ）
# 
# 例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11!= 39916800 末端有 2 个 0 。给定
# K，找出多少个非负整数 x ，能满足 f(x) = K 。
# 
# 
# 
# 示例 1： 
# 
# 
# 输入：K = 0
# 输出：5
# 解释：0!, 1!, 2!, 3!, and 4! 均符合 K = 0 的条件。
# 
# 
# 示例 2：
# 
# 
# 输入：K = 5
# 输出：0
# 解释：没有匹配到这样的 x!，符合 K = 5 的条件。
# 
# 
# 
# 提示：
# 
# 
# 
# K 是范围在 [0, 10^9] 的整数。
# 
# 
# 
#

# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # return 0 if n==0 else (n/5  + self.trailingZeroes(n/5))
        # return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)
        res = 0
        while n // 5:
            res += n//5
            n = n//5
        return res
        
    # def left_bound(self,k):
    #     left, right = 0, 
    #     while left<=right:
    #         mid = left + (right-left)//2
    #         zeros = self.trailingZeroes(mid)
    #         if zeros>=k:
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return left
    
    def left_bound(self,k):
        left, right = 0, 10^10000000000
        while left<right:
            mid = left + (right-left)//2
            zeros = self.trailingZeroes(mid)
            if zeros>=k:
                right = mid 
            else:
                left = mid + 1
        return left

    
    def right_bound(self,k):
        left, right = 0, 10^10000000000
        while left<right:
            mid = left + (right-left)//2
            zeros = self.trailingZeroes(mid)
            if zeros<=k:
                left = mid + 1
            else:
                right = mid 
        return left -1 

    def preimageSizeFZF(self, k: int) -> int:
    #     def zeta(x):
    #         return x//5 + zeta(x//5) if x > 0 else 0

    #     lo, hi = K, 10*K + 1
    #     while lo < hi:
    #         mi = (lo + hi) // 2
    #         zmi = zeta(mi)
    #         if zmi == K: return 5
    #         elif zmi < K: lo = mi + 1
    #         else: hi = mi

    #     return 0

        return self.right_bound(k) - self.left_bound(k)+1

# @lc code=end

