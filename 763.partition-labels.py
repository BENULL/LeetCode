#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (75.70%)
# Likes:    3149
# Dislikes: 133
# Total Accepted:    173.2K
# Total Submissions: 224.3K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# A string S of lowercase English letters is given. We want to partition this
# string into as many parts as possible so that each letter appears in at most
# one part, and return a list of integers representing the size of these
# parts.
# 
# 
# 
# Example 1:
# 
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
# 
# 
# 
# 
# Note:
# 
# 
# S will have length in range [1, 500].
# S will consist of lowercase English letters ('a' to 'z') only.
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ends = {c:i for i,c in enumerate(S)}
        curr,out= 0,[0]
        while curr <len(S):
            last = ends[S[curr]]
            while curr<=last:
                symb = S[curr]
                last = max(last,ends[symb])
                curr += 1
            out.append(curr)

        return [out[i]-out[i-1] for i in range(1,len(out))]
        


        
# @lc code=end

