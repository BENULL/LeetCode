#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (69.45%)
# Likes:    239
# Dislikes: 0
# Total Accepted:    85.5K
# Total Submissions: 123.1K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
# 
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 
# 请找出在 t 中被添加的字母。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。
# 
# 
# 示例 2：
# 
# 输入：s = "", t = "y"
# 输出："y"
# 
# 
# 示例 3：
# 
# 输入：s = "a", t = "aa"
# 输出："a"
# 
# 
# 示例 4：
# 
# 输入：s = "ae", t = "aea"
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s 和 t 只包含小写字母
# 
# 
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # sC = collections.Counter(s)
        # tC = collections.Counter(t)
        # res = tC - sC
        # return list(res.keys())[0]

        # Solution 2 : sum
        # res = functools.reduce(lambda x,y : x+ord(y),t,0) - functools.reduce(lambda x,y : x+ord(y),s,0)
        # return chr(res)

        # Solution 3 位运算
        # 如果将两个字符串拼接成一个字符串，则问题转换成求字符串中出现奇数次的字符
        # return chr(functools.reduce(lambda x,y : x^ord(y),s+t,0))
        return chr(reduce(xor, map(ord, s + t)))
# @lc code=end

