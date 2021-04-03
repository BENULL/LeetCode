#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (56.72%)
# Likes:    139
# Dislikes: 0
# Total Accepted:    42.3K
# Total Submissions: 74.6K
# Testcase Example:  '"a"\n"b"'
#
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines
# 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
# 
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
# 
# 
# 
# 示例 1：
# 
# 
# 输入：ransomNote = "a", magazine = "b"
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：ransomNote = "aa", magazine = "ab"
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：ransomNote = "aa", magazine = "aab"
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 你可以假设两个字符串均只含有小写字母。
# 
# 
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # mC = collections.Counter(magazine)
        # for c in ransomNote:
        #     if c in mC and mC[c]>=0:
        #         mC[c] -= 1 
        #     else:
        #         return False
        # return True

        # doodad
        # return all([Counter(magazine).get(k, 0) - v >=0 for k, v in Counter(ransomNote).items()])

        
# @lc code=end

