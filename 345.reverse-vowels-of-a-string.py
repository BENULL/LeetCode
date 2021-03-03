#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (44.05%)
# Likes:    934
# Dislikes: 1434
# Total Accepted:    265.1K
# Total Submissions: 588.1K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # left, right = 0, len(s)-1
        # res = list(s)
        # while left<right:
        #     if s[left] not in 'aeiouAEIOU':
        #         left += 1
        #     if s[right] not in 'aeiouAEIOU':
        #         right -= 1
        #     if s[right] in 'aeiouAEIOU' and s[left] in 'aeiouAEIOU' and left<right:
        #         res[left],res[right] = s[right],s[left]
        #         left+=1
        #         right-=1

        # return ''.join(res)


        s = list(s)
        vowels = set('aeiouAEIOU')
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] not in vowels:
                i += 1
                continue
                
            if s[j] not in vowels:
                j -= 1
                continue
                
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
            
        return ''.join(s)
            
        
# @lc code=end

