class Solution:
    """
    剑指 Offer 38. 字符串的排列
    输入一个字符串，打印出该字符串中字符的所有排列。

    

    你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

    

    示例:

    输入：s = "abc"
    输出：["abc","acb","bac","bca","cab","cba"]
    

    限制：

    1 <= s 的长度 <= 8
    """
    def permutation(self, s: str) -> List[str]:
        ans = []
        s = sorted(list(s))
        visited = [False]*len(s)

        def backtrack(i, path):
            if i==len(s):
                ans.append(''.join(path))
                return 
            for j in range(len(s)):
                if visited[j] or (j>0 and not visited[j-1] and s[j]==s[j-1]):
                    continue
                visited[j] = True
                backtrack(i+1, path + [s[j]])
                visited[j] = False
        backtrack(0, [])
        return ans
