#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (50.30%)
# Likes:    2894
# Dislikes: 485
# Total Accepted:    597.9K
# Total Submissions: 1.2M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
# 
# A happy number is a number defined by the following process:
# 
# 
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# 
# 
# Return true if n is a happy number, and false if not.
# 
# 
# Example 1:
# 
# 
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:

    # def isHappy(self, n: int) -> bool:
    #     vis = {n}
    #     _sum = n
    #     while  _sum != 1:
    #         c = 0
    #         for i in str(_sum):
    #             c += int(i)**2
    #         _sum = c
    #         if _sum in vis:
    #             return False
    #         vis.add(_sum)
        
    #     return True


    #  The only cycle starts and ends with 4
    # def isHappy(self, n: int) -> bool:
    #     while n != 1:
    #         n = sum([int(i) ** 2 for i in str(n)])
    #         if n == 4:
    #             return False
        
    #     return True



    # tortoise hare technique
    def isHappy(self, n: int) -> bool:
	# 20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while slow!=fast and fast!=1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))

        return fast==1

    def squared(self, n):
        result = 0
        while n>0:
            last = n%10
            result += last * last
            n = n//10
        return result



        
# @lc code=end

