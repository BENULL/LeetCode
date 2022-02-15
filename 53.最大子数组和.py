#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (55.18%)
# Likes:    4348
# Dislikes: 0
# Total Accepted:    850.2K
# Total Submissions: 1.5M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 子数组 是数组中的一个连续部分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [5,4,-1,7,8]
# 输出：23
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# 
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
# 
#

# @lc code=start

Status = collections.namedtuple('Status', ['lSum', 'rSum', 'mSum', 'iSum'])

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp

        # pre, maxAns = 0, nums[0]
        # for num in nums:
        #     pre = max(pre+num,num)
        #     maxAns = max(maxAns, pre)
        # return maxAns


        # divide  segment tree
        # https://leetcode-cn.com/problems/maximum-subarray/solution/zui-da-zi-xu-he-by-leetcode-solution/
        return self.getInfo(nums, 0, len(nums)-1).mSum
    
    def getInfo(self, nums, l, r)->Status:
        if l==r:
            return Status._make([nums[l]]*4)
        m = l + (r-l) // 2
        lSub = self.getInfo(nums, l, m)
        rSub = self.getInfo(nums, m+1, r)
        return self.pushUp(lSub, rSub)
    
    def pushUp(self, lSub, rSub)-> Status:
        iSum = lSub.iSum + rSub.iSum
        lSum = max(lSub.lSum, lSub.iSum+rSub.lSum)
        rSum = max(rSub.rSum, rSub.iSum+lSub.rSum)
        mSum = max(max(lSub.mSum, rSub.mSum), lSub.rSum+rSub.lSum)
        return Status(lSum, rSum, mSum, iSum)


    




# @lc code=end

