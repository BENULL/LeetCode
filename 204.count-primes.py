#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (31.38%)
# Likes:    2814
# Dislikes: 742
# Total Accepted:    448.4K
# Total Submissions: 1.4M
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# 
# Example 1:
# 
# 
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
# Example 2:
# 
# 
# Input: n = 0
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: n = 1
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 5 * 10^6
# 
# 
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        # The Sieve of Eratosthenes
        if n<2:
            return 0
        primes = [True]*n
        primes[0] = primes[1] = False
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i] = [False]*len(primes[i*i:n:i])
        return sum(primes)


        
# @lc code=end

