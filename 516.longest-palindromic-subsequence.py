#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (52.85%)
# Likes:    2403
# Dislikes: 198
# Total Accepted:    136K
# Total Submissions: 251.2K
# Testcase Example:  '"bbbab"'
#
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
# 
# Example 1:
# Input:
# 
# 
# "bbbab"
# 
# Output:
# 
# 
# 4
# 
# One possible longest palindromic subsequence is "bbbb".
# 
# 
# 
# Example 2:
# Input:
# 
# 
# "cbbd"
# 
# Output:
# 
# 
# 2
# 
# One possible longest palindromic subsequence is "bb".
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # # dp top-down 
        # @lru_cache(None)
        # def helper(i,j):
        #     if i>j:
        #         return 0
        #     if i==j:
        #         return 1
        #     if s[i]==s[j]:
        #         return helper(i+1,j-1)+2
        #     return max(helper(i+1,j),helper(i,j-1))
        # i, j =0, len(s)-1
        # return helper(i,j)

        # dp
        l = len(s)
        dp = [[0]*l for _ in range(l) ]
        for i in range(l):
            dp[i][i] = 1
        for i in range(l-2,-1,-1):
            for j in range(i+1,l):
                if s[i] == s[j]:
                    dp[i][j] = 2 +  dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i+1][j]) 
        return dp[0][l-1]    

        
# @lc code=end

