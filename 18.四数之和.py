#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (39.52%)
# Likes:    1042
# Dislikes: 0
# Total Accepted:    244.5K
# Total Submissions: 619.2K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
# nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
# 
# 
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# 你可以按 任意顺序 返回答案 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # dfs TLE
        path = []
        nums.sort()
        n = len(nums)
        def dfs(start, _sum):
            if _sum==target and len(path)==4:
                res.append(path[:])
                return

            for index in range(start,n):
                if  (n-index)<(4-len(path)) or (index < n - 1 and _sum + nums[index] + (3 - len(path)) * nums[index + 1] > target):
                    return
                if (index>start and nums[index]==nums[index-1]) or (index < n - 1 and _sum + nums[index] + (3 - len(path)) * nums[n - 1] < target):
                    continue
                path.append(nums[index])
                dfs(index+1, _sum + nums[index])
                path.pop()
        res = []
        dfs(0,0)
        return res
# @lc code=end

