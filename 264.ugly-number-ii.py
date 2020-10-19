#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (41.90%)
# Likes:    2167
# Dislikes: 133
# Total Accepted:    188.5K
# Total Submissions: 444.7K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # dp
        idx_2 = idx_3 = idx_5 = 0
        res = [1]
        count = 1
        while count<n:
            val = min(res[idx_2]*2,res[idx_3]*3,res[idx_5]*5)
            if val == res[idx_2]*2:
                idx_2 += 1
            if val == res[idx_3]*3:
                idx_3 += 1
            if val == res[idx_5]*5:
                idx_5 += 1
            count += 1
            res.append(val)
        return res[-1]

            
            
        

        
# @lc code=end

