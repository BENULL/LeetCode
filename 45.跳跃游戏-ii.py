#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (43.89%)
# Likes:    1402
# Dislikes: 0
# Total Accepted:    261.9K
# Total Submissions: 596.5K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 
# 假设你总是可以到达数组的最后一个位置。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [2,3,0,1,4]
# 输出: 2
# 
# 
# 
# 
# 提示:
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def jump(self, nums) -> int:
        # n, rightmost = len(nums), 0
        # queue = [0]
        # times = 0
        # while queue and rightmost<n-1:
        #     times += 1
        #     right = queue.pop(0)
        #     rightmost = max([i+nums[i] for i in range(right+1)]+[rightmost])
        #     queue.append(rightmost)
            
        # return times

        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            maxPos = max(maxPos, i + nums[i])
            if i == end:
                end = maxPos
                step += 1
        return step


            
if __name__=='__main__':
    s = Solution()
    s.jump([2,3,1,1,4])
            
# @lc code=end

