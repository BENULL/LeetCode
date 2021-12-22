#
# @lc app=leetcode.cn id=1541 lang=python3
#
# [1541] 平衡括号字符串的最少插入次数
#
# https://leetcode-cn.com/problems/minimum-insertions-to-balance-a-parentheses-string/description/
#
# algorithms
# Medium (46.55%)
# Likes:    35
# Dislikes: 0
# Total Accepted:    6.8K
# Total Submissions: 14.7K
# Testcase Example:  '"(()))"'
#
# 给你一个括号字符串 s ，它只包含字符 '(' 和 ')' 。一个括号字符串被称为平衡的当它满足：
# 
# 
# 任何左括号 '(' 必须对应两个连续的右括号 '))' 。
# 左括号 '(' 必须在对应的连续两个右括号 '))' 之前。
# 
# 
# 比方说 "())"， "())(())))" 和 "(())())))" 都是平衡的， ")()"， "()))" 和 "(()))" 都是不平衡的。
# 
# 你可以在任意位置插入字符 '(' 和 ')' 使字符串平衡。
# 
# 请你返回让 s 平衡的最少插入次数。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "(()))"
# 输出：1
# 解释：第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 ')' 使字符串变成平衡字符串
# "(())))" 。
# 
# 
# 示例 2：
# 
# 输入：s = "())"
# 输出：0
# 解释：字符串已经平衡了。
# 
# 
# 示例 3：
# 
# 输入：s = "))())("
# 输出：3
# 解释：添加 '(' 去匹配最开头的 '))' ，然后添加 '))' 去匹配最后一个 '(' 。
# 
# 
# 示例 4：
# 
# 输入：s = "(((((("
# 输出：12
# 解释：添加 12 个 ')' 得到平衡字符串。
# 
# 
# 示例 5：
# 
# 输入：s = ")))))))"
# 输出：5
# 解释：在字符串开头添加 4 个 '(' 并在结尾添加 1 个 ')' ，字符串变成平衡字符串 "(((())))))))" 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 只包含 '(' 和 ')' 。
# 
# 
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        # res = 0
        # left = 0
        # i = 0
        # while i<len(s):
        #     if s[i]=='(':
        #         left += 1
        #         i += 1
        #     elif i+1 < len(s) and s[i+1]==')':
        #         if left > 0:
        #             left -= 1
        #         else:
        #             res += 1
        #         i += 2
        #     else:
        #         res += 1
        #         if left > 0:
        #             left -= 1
        #         else:
        #             res += 1
        #         i += 1
        # return res + (2 * left)


        res = 0
        need = 0
        for c in s:
            if c=='(':
                need += 2
                if need%2==1:
                    res += 1
                    need -= 1
            else:
                need -= 1
                if need == -1:
                    res += 1
                    need = 1 
        return res + need
                
# @lc code=end

