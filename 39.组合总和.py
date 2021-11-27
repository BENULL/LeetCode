#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (72.73%)
# Likes:    1636
# Dislikes: 0
# Total Accepted:    364.5K
# Total Submissions: 501.1K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target
# 的唯一组合。
# 
# candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
# 
# 对于给定的输入，保证和为 target 的唯一组合数少于 150 个。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: candidates = [2,3,6,7], target = 7
# 输出: [[7],[2,2,3]]
# 
# 
# 示例 2：
# 
# 
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 
# 示例 3：
# 
# 
# 输入: candidates = [2], target = 1
# 输出: []
# 
# 
# 示例 4：
# 
# 
# 输入: candidates = [1], target = 1
# 输出: [[1]]
# 
# 
# 示例 5：
# 
# 
# 输入: candidates = [1], target = 2
# 输出: [[1,1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# candidate 中的每个元素都是独一无二的。
# 1 
# 
# 
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        def dfs(_sum, start):
            if _sum > target: return 
            if _sum == target: res.append(path[:])
            for i in range(start, len(candidates)):
                if candidates[i]+_sum > target: return
                path.append(candidates[i])
                dfs(_sum + candidates[i], i)
                path.pop()
        dfs(0, 0)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,5],8))

# @lc code=end

