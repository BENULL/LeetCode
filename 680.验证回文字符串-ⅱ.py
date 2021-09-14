#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (40.17%)
# Likes:    394
# Dislikes: 0
# Total Accepted:    84.7K
# Total Submissions: 211.1K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "aba"
# 输出: true
# 
# 
# 示例 2:
# 
# 
# 输入: s = "abca"
# 输出: true
# 解释: 你可以删除c字符。
# 
# 
# 示例 3:
# 
# 
# 输入: s = "abc"
# 输出: false
# 
# 
# 
# 提示:
# 
# 
# 1 
# s 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # def checkPalindrome(low, high):
        #     i, j = low, high
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True

        low, high = 0, len(s)
        while low < high:
            if s[low] == s[high-1]: 
                low += 1
                high -= 1
            else:
                return s[low + 1:high]==s[low + 1:high][::-1] or s[low:high-1]==s[low:high-1][::-1]
        return True
# @lc code=end

