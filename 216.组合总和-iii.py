#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (73.62%)
# Likes:    392
# Dislikes: 0
# Total Accepted:    108.8K
# Total Submissions: 147.8K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 
# 说明：
# 
# 
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 
# 
# 示例 2:
# 
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) :
        """dfs
        """
        # res = []
        # def dfs(start, _sum, path, depth):
        #     if start>10: return 
        #     if _sum==n and k==depth:
        #         res.append(path[:])
        #         return 
        #     if _sum > n or depth >= k:
        #         return 
            
        #     # for i in range(start,10):
        #     path.append(start)
        #     dfs(start+1, _sum+start, path, depth+1)
        #     path.pop()
        #     dfs(start+1, _sum, path, depth)
            
        # dfs(1, 0, [], 0)
        # return res

        """dp 滚动数组优化
        """
        # https://leetcode-cn.com/problems/combination-sum-iii/solution/yong-bei-bao-jie-jue-zu-he-zong-he-iii-by-wannabea/
        dp = [[[]] if j == 0 else [] for j in range(n + 1)]
        for num in range(1, 10):
            for j in range(n, num - 1, -1):
                dp[j].extend(res + [num] for res in dp[j - num])
        return [res for res in dp[-1] if len(res) == k]

        
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3, 7))
# @lc code=end

