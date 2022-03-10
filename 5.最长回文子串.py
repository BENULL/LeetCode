#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (36.15%)
# Likes:    4834
# Dislikes: 0
# Total Accepted:    916K
# Total Submissions: 2.5M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp
        max_len = 1
        start = 0
        n = len(s)
        if n<2:
            return s

        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for j in range(1,n):
            for i in range(j):
                if s[i]==s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j-i+1>max_len:
                    max_len = j - i + 1
                    start = i
        return s[start:start+max_len]




# @lc code=end

