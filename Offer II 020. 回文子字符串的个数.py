class Solution:
    """
    给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。

    具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

    示例 1：

    输入：s = "abc"
    输出：3
    解释：三个回文子串: "a", "b", "c"
    示例 2：

    输入：s = "aaa"
    输出：6
    解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
     

    提示：

    1 <= s.length <= 1000
    s 由小写英文字母组成        
    """
    def countSubstrings(self, s: str) -> int:
        def count(left, right):
            cnt = 0
            while left>=0 and right<len(s) and s[left]==s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt



        if not str:
            return 0
        res = 0
        for i in range(len(s)):
            res += count(i, i)
            res += count(i, i+1)
        return res