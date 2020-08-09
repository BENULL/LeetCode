#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (60.48%)
# Likes:    2767
# Dislikes: 115
# Total Accepted:    192.9K
# Total Submissions: 318.2K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# 
# Note:
# 
# 
# The input string length won't exceed 1000.
# 
# 
# 
#

# @lc code=start
class Solution:
    # brute force
    # def countSubstrings(self, s: str) -> int:
    #     res = 0
    #     for i in range(len(s)):
    #         for j in range(len(s)):
    #             if s[i:j] == s[i:j:-1]:
    #                 res += 1
    #     return res
    




    """
        Iterate the word, for each character, judge palindromic substrings by applying a fucntion palindrom. There are two cases, the
        palindromic string length is odd or even. For example aaa, aa. The fucntion palindrom checks from the center to end. If the two
        character equals, move on, left pointer moves left, right pointer moves right, if not, break the loop.
    """
    def countSubstrings(self, s: str) -> int:
        self.cnt = 0
        n = len(s)
        for i in range(n):
            self.palindromic(s, i, i) # judge odd length string
            self.palindromic(s, i, i+1) # judge even length string
        return self.cnt
        
    
    def palindromic(self, s, left, right): # judge if a substring is palindromic
        n = len(s)
        while(left >= 0 and right < n and s[left] == s[right]):
            self.cnt += 1
            left -= 1
            right += 1



        
# @lc code=end

