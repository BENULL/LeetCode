#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (35.38%)
# Likes:    1608
# Dislikes: 545
# Total Accepted:    223.1K
# Total Submissions: 597.6K
# Testcase Example:  '"25525511135"'
#
# Given a string s containing only digits, return all possible valid IP
# addresses that can be obtained from s. You can return them in any order.
# 
# A valid IP address consists of exactly four integers, each integer is between
# 0 and 255, separated by single dots and cannot have leading zeros. For
# example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and
# "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
# addresses. 
# 
# 
# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]
# Example 3:
# Input: s = "1111"
# Output: ["1.1.1.1"]
# Example 4:
# Input: s = "010010"
# Output: ["0.10.0.10","0.100.1.0"]
# Example 5:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 3000
# s consists of digits only.
# 
# 
#

# @lc code=start
class Solution:

    # dfs
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, 0, "", res)
        return res
    
    def dfs(self, s, idx, path, res):
        if idx > 4:
            return 
        if idx == 4 and not s:
            res.append(path[:-1])
            return 
        for i in range(1, len(s)+1):
            if s[:i]=='0' or (s[0]!='0' and 0 < int(s[:i]) < 256):
                self.dfs(s[i:], idx+1, path+s[:i]+".", res)


        
# @lc code=end