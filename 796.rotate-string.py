#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (49.69%)
# Likes:    1041
# Dislikes: 61
# Total Accepted:    95.2K
# Total Submissions: 193.8K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# We are given two strings, A and B.
# 
# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.
# 
# 
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
# 
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
# 
# 
# Note:
# 
# 
# A and B will have length at most 100.
# 
# 
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        # if len(A)!=len(B):
        #     return False
        # if len(A)==len(B) and len(A)==0:
        #     return True
        # for i in range(len(A)):
        #     if A[i:]+A[:i] == B:
        #         return True
        # return False

        return len(A) == len(B) and B in A+A
        
# @lc code=end

