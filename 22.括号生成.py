#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (77.27%)
# Likes:    2226
# Dislikes: 0
# Total Accepted:    393.3K
# Total Submissions: 508.8K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：["()"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtrace
        res = []
        path = []
        def dfs(left,right):
            if left>right: return 
            if left<0 or right<0: return 
            if left==0 and right==0:
                res.append(''.join(path))
                return
            path.append('(')
            dfs(left-1, right)
            path.pop()

            path.append(')')
            dfs(left, right-1)
            path.pop()
            

        dfs(n, n)
        return res

# @lc code=end

