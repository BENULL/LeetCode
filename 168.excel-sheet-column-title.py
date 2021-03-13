#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (30.91%)
# Likes:    1603
# Dislikes: 293
# Total Accepted:    247.8K
# Total Submissions: 779.4K
# Testcase Example:  '1'
#
# Given an integer columnNumber, return its corresponding column title as it
# appears in an Excel sheet.
# 
# For example:
# 
# 
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
# 
# 
# 
# Example 1:
# 
# 
# Input: columnNumber = 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: columnNumber = 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: columnNumber = 701
# Output: "ZY"
# 
# 
# Example 4:
# 
# 
# Input: columnNumber = 2147483647
# Output: "FXSHRXW"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= columnNumber <= 2^31 - 1
# 
# 
#

# @lc code=start
import string
alphabet = string.ascii_uppercase
class Solution:
    
    def convertToTitle(self, n: int) -> str:
        # res = ''
        # while columnNumber>0:
        #     columnNumber -= 1
        #     res = chr(columnNumber%26+65) + res
        #     columnNumber = columnNumber // 26
        # return res

        # result = "" 
        # while columnNumber > 0: 
        #     result = result + string.ascii_uppercase[(columnNumber - 1) % 26] # string.ascii_uppercase generates A-Z, and if you give a parameter then it will give you the value at that index. Eg, ascii_uppercase[0] will return A and so on.
        #     columnNumber = (columnNumber - 1) // 26
        # return result[::-1]
       # 0 - 25 

        result = ""

        while n > 0:
            n -= 1

            n, i = divmod(n, 26)
            result += alphabet[i]

        return result[::-1]
# @lc code=end

