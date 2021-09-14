#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#
# https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (47.24%)
# Likes:    214
# Dislikes: 0
# Total Accepted:    53.2K
# Total Submissions: 109.2K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 给你一个字符串 s 和一个字符串数组 dictionary 作为字典，找出并返回字典中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
# 
# 如果答案不止一个，返回长度最长且字典序最小的字符串。如果答案不存在，则返回空字符串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# 输出："apple"
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abpcplea", dictionary = ["a","b","c"]
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 1 
# s 和 dictionary[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # two point and sort early stop
        # dictionary.sort(key=lambda x: (-len(x), x))
        # for t in dictionary:
        #     i = j = 0
        #     while i < len(t) and j < len(s):
        #         if t[i] == s[j]:
        #             i += 1
        #         j += 1
        #     if i == len(t):
        #         return t
        # return ""

        # dp
        # https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-di-at66/
        m = len(s)
        dp = [[0]*26 for _ in range(m)]
        dp.append([m]*26)


        for i in range(m-1, -1, -1):
            for j in range(26):
                if ord(s[i]) == j + 97:
                    dp[i][j] = i
                else:
                    dp[i][j] = dp[i + 1][j]
        
        dictionary.sort(key=lambda x: (-len(x), x))
        for t in dictionary:
            index = 0
            for c in t:
                if dp[index][ord(c)-97] == m:
                    break
                index = dp[index][ord(c)-97] + 1
            else:
                return t
            
        return ""




# @lc code=end

