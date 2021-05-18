#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode-cn.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (47.69%)
# Likes:    517
# Dislikes: 0
# Total Accepted:    53.8K
# Total Submissions: 112.9K
# Testcase Example:  '"bcabc"'
#
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
# 
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "bcabc"
# 输出："abc"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbacdcbc"
# 输出："acdb"
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    import collections
    def removeDuplicateLetters(self, s: str) -> str:
        # 单调栈
        stack = []
        cnt = collections.Counter(s)
        for c in s:
            if c not in stack:
                while stack and stack[-1]>c and cnt[stack[-1]]>0:
                    stack.pop()
                stack.append(c)
            cnt[c] -= 1
        return ''.join(stack)






# @lc code=end

