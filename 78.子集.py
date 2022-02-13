#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (80.33%)
# Likes:    1476
# Dislikes: 0
# Total Accepted:    368.5K
# Total Submissions: 458.7K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [0]
# 输出：[[],[0]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10 
# nums 中的所有元素 互不相同
# 
# 
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = [[]]
        # def dfs(path,i):
        #     if i >= len(nums):
        #         return 
        #     path.append(nums[i])
        #     res.append(path[:])
        #     dfs(path, i+1)
        #     path.pop()
        #     dfs(path, i+1)
        # dfs([], 0)
        # return res

        # 迭代法实现子集枚举
        res = []
        n = len(nums)
        for mask in range(1<<n):
            ans = []
            for i in range(n):
                if mask&(1<<i):
                    ans.append(nums[i])
            res.append(ans)
        return res


# @lc code=end

