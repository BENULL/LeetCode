#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#
# https://leetcode-cn.com/problems/increasing-subsequences/description/
#
# algorithms
# Medium (55.08%)
# Likes:    297
# Dislikes: 0
# Total Accepted:    39.4K
# Total Submissions: 71.5K
# Testcase Example:  '[4,6,7,7]'
#
# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是 2 。
# 
# 
# 
# 示例：
# 
# 
# 输入：[4, 6, 7, 7]
# 输出：[[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7],
# [4,7,7]]
# 
# 
# 
# 提示：
# 
# 
# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
# 
# 
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums):
        # dfs
        if len(nums)<2: return []
        res = []
        
        def dfs(i, path):
            if i >= len(nums): return 
            
            if path[-1]<=nums[i]:
                path.append(nums[i])
                if path not in res:
                    res.append(path[:])
                dfs(i+1,path)
                path.pop(-1)
            dfs(i+1,path)

        for i in range(len(nums)):
            dfs(i+1,[nums[i]])
        return res


if __name__ == '__main__':
    s = Solution()
    s.findSubsequences([4,6,7,7])

# @lc code=end

