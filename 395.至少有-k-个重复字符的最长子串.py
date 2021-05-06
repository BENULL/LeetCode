#
# @lc app=leetcode.cn id=395 lang=python3
#
# 分治[395] 至少有 K 个重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (51.89%)
# Likes:    471
# Dislikes: 0
# Total Accepted:    43.2K
# Total Submissions: 83.3K
# Testcase Example:  '"aaabb"\n3'
#
# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由小写英文字母组成
# 1 
# 
# 
#

# @lc code=start
class Solution:

    # 分治
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t,k) for t in s.split(c))
        return len(s)
# @lc code=end

