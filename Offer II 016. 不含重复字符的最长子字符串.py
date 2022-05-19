class Solution:
    """
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长连续子字符串 的长度。

    示例 1:

    输入: s = "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子字符串是 "abc"，所以其长度为 3。
    示例 2:

    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子字符串是 "b"，所以其长度为 1。
    示例 3:

    输入: s = "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
    示例 4:

    输入: s = ""
    输出: 0
     

    提示：

    0 <= s.length <= 5 * 104
    s 由英文字母、数字、符号和空格组成


    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        vis = set()
        n = len(s)
        right, res = 0, 0
        for i in range(n):
            if i!=0:
                vis.remove(s[i-1])
            while right<n and s[right] not in vis:
                vis.add(s[right])
                right += 1
            res = max(res, right-i)
        return res
