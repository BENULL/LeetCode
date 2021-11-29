#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (43.28%)
# Likes:    501
# Dislikes: 0
# Total Accepted:    132.1K
# Total Submissions: 305.1K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
# 
# 换句话说，s1 的排列之一是 s2 的 子串 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 
# 
# 示例 2：
# 
# 
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # slide window
        m, n = len(s1), len(s2)
        if n<m: return False
        d1 = [0] * 26
        d2 = [0] * 26
        for i in s1:
            d1[ord(i) - 97] += 1
        left, right = 0, 0
        while right < n:
            d2[ord(s2[right]) - 97] += 1
            if right - left >= m:
                d2[ord(s2[left]) - 97] -= 1
                left += 1
            if d2 == d1:
                return True
            right += 1
        return False 

        

# @lc code=end

