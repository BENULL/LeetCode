#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.98%)
# Likes:    859
# Dislikes: 0
# Total Accepted:    275.8K
# Total Submissions: 358.3K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
# 
# 你可以按 任何顺序 返回答案。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
# 
# 示例 2：
# 
# 
# 输入：n = 1, k = 1
# 输出：[[1]]
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(path,i):
            if len(path) + (n - i + 1) < k:
                return 
            if len(path) == k:
                res.append(path[:])
                return
            path.append(i)
            dfs(path, i+1)
            path.pop()
            dfs(path, i+1)
        dfs([], 1)
        return res
# @lc code=end

