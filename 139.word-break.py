#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (39.82%)
# Likes:    4387
# Dislikes: 233
# Total Accepted:    559K
# Total Submissions: 1.4M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """dp
        """
        # dp = [False]*(len(s)+1) 
        # dp[0] = True
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         if dp[i] and s[i:j+1] in wordDict:
        #             dp[j+1] = True
        # return dp[-1]

        """dfs
        """
        # @functools.lru_cache(None)
        # def dfs(start):
        #     if start == len(s):
        #         return True
        #     for i in range(start+1, len(s)+1):
        #         if s[start:i] in wordDict and dfs(i):
        #             return True
        #     return False
        # return dfs(0)

        """bfs
        """
        queue = [0]
        visited = [False]*len(s)
        while queue:
            start = queue.pop(-1)
            if visited[start]:
                continue
            visited[start] = True
            for i in range(start+1, len(s)+1):
                if s[start:i] in wordDict:
                    if i<len(s):
                        queue.append(i)
                    else:
                        return True
        return False




    
        
# @lc code=end

