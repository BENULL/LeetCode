#
# @lc app=leetcode.cn id=678 lang=python3
#
# [678] 有效的括号字符串
#
# https://leetcode-cn.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (38.58%)
# Likes:    404
# Dislikes: 0
# Total Accepted:    44K
# Total Submissions: 114.1K
# Testcase Example:  '"()"'
#
# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
# 
# 
# 任何左括号 ( 必须有相应的右括号 )。
# 任何右括号 ) 必须有相应的左括号 ( 。
# 左括号 ( 必须在对应的右括号之前 )。
# * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
# 一个空字符串也被视为有效字符串。
# 
# 
# 示例 1:
# 
# 
# 输入: "()"
# 输出: True
# 
# 
# 示例 2:
# 
# 
# 输入: "(*)"
# 输出: True
# 
# 
# 示例 3:
# 
# 
# 输入: "(*))"
# 输出: True
# 
# 
# 注意:
# 
# 
# 字符串大小将在 [1，100] 范围内。
# 
# 
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        # dp
        # n = len(s)
        # dp = [[False]*n for _ in range(n)]
        # for i in range(n):
        #     if s[i]=='*':
        #         dp[i][i]=True 
        # for i in range(1,n):
        #     dp[i-1][i] = (s[i-1]=='(' or s[i-1]=='*') and  (s[i]==')' or s[i]=='*')
        
        # for i in range(n-3,-1,-1):
        #     for j in range(i+2, n):
        #         if (s[i]=='(' or s[i]=='*') and (s[j]==')' or s[j]=='*'):
        #             dp[i][j] = dp[i+1][j-1]
        #             for k in range(i,j):
        #                 if not dp[i][j]:
        #                     dp[i][j] = dp[i][k] and dp[k+1][j]
        # return dp[0][n-1]

        # 2 stack match
        add_stack = []
        star_stack = []
        for i in range(len(s)):
            if s[i]=='(':
                add_stack.append(i)
            elif s[i]=='*':
                star_stack.append(i)
            else:
                if add_stack:
                    add_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        while add_stack:
            if star_stack:
                add_index, star_index = add_stack.pop(), star_stack.pop()
                if add_index>star_index:
                    return False
            else:
                return False
        return True

        # simulate or greedy
        # emo


                    



# @lc code=end

