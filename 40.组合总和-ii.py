#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (61.82%)
# Likes:    743
# Dislikes: 0
# Total Accepted:    216.1K
# Total Submissions: 349.7K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 注意：解集不能包含重复的组合。 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# 
# 示例 2:
# 
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
# 
# 
# 
# 提示:
# 
# 
# 1 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # TLE
        res = []
        path = []
        visited = [False]*len(candidates)
        candidates.sort()
        # def notExist(path):
        #     for p in res:
        #         if sorted(p) == sorted(path):
        #             return False
        #     return True
        def dfs(_sum, start):
            if _sum > target: return 
            if _sum == target:
                res.append(path[:])
            for i in range(start, len(candidates)):
                # if not visited[i]:
                if i>0 and candidates[i]==candidates[i-1] and not visited[i-1]:
                    continue
                if _sum + candidates[i] > target: break
                path.append(candidates[i])
                visited[i] = True
                dfs(_sum + candidates[i],i+1)
                visited[i] = False
                path.pop()
        dfs(0,0)
        return res



# @lc code=end

