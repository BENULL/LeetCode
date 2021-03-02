#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (34.49%)
# Likes:    6106
# Dislikes: 414
# Total Accepted:    502.2K
# Total Submissions: 1.4M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given two strings s and t, return the minimum window in s which will contain
# all the characters in t. If there is no such window in s that covers all
# characters in t, return the empty string "".
# 
# Note that If there is such a window, it is guaranteed that there will always
# be only one unique minimum window in s.
# 
# 
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 10^5
# s and t consist of English letters.
# 
# 
# 
# Follow up: Could you find an algorithm that runs in O(n) time?
#

# @lc code=start

# slide window
# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j,c in enumerate(s,1):
            missing -= need[c]>0
            need[c] -= 1
            if not missing:
                while i<j and need[s[i]]<0:
                    need[s[i]]+=1
                    i+=1
                if not J or j-i<=J-I:
                    I, J = i, j
        return s[I:J]

        
# @lc code=end

