#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (35.48%)
# Likes:    1623
# Dislikes: 51
# Total Accepted:    84.6K
# Total Submissions: 232.8K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
# represents the width and the height of an envelope.
# 
# One envelope can fit into another if and only if both the width and height of
# one envelope is greater than the width and height of the other envelope.
# 
# Return the maximum number of envelopes can you Russian doll (i.e., put one
# inside the other).
# 
# Note: You cannot rotate an envelope.
# 
# 
# Example 1:
# 
# 
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
# 
# 
# Example 2:
# 
# 
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= envelopes.length <= 5000
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    # ==  300
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        N = len(envelopes)

        # two ways of sort
        # envelopes.sort(cmp = lambda x,y: x[0]-y[0] if x[0]!=y[0] else y[1]-x[1])
        envelopes.sort(key = lambda x : (x[0],-1*x[1]))

        return self.lengthOfLIS([e[1] for e in envelopes])

    def lengthOfLIS(self,nums):
        tails = []
        for num in nums:
            idx = bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)
        
# @lc code=end

