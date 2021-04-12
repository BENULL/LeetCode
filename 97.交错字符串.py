#
# @lc app=leetcode.cn id=97 lang=python3
#
# [97] 交错字符串
#
# https://leetcode-cn.com/problems/interleaving-string/description/
#
# algorithms
# Medium (45.88%)
# Likes:    425
# Dislikes: 0
# Total Accepted:    44.2K
# Total Submissions: 96.2K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
# 
# 两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
# 
# 
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# |n - m| 
# 交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
# 
# 
# 提示：a + b 意味着字符串 a 和 b 连接。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# s1、s2、和 s3 都由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # dp
        # https://leetcode-cn.com/problems/interleaving-string/solution/jiao-cuo-zi-fu-chuan-by-leetcode-solution/
        
        f = [False]*(len(s2)+1)

        n, m, t = len(s1), len(s2), len(s3)

        if n+m != t: return False

        f[0] = True

        for i,j in itertools.product(range(n+1),range(m+1)):
            p = i+j-1
            if i>0:
                f[j] &= (s1[i-1]==s3[p])
            if j>0:
                f[j] |= (f[j - 1] and s2[j - 1] == s3[p])
        return f[m]




        # dfs
        # if "" in (s1,s2): return s3 in (s1,s2)

        # len1, len2 = len(s1), len(s2)

        # if len1+len2!=len(s3):return False

        # visit = [ [False]*(len2+1) for _ in range(len1+1)]

        # def dfs(i,j):
        #     nonlocal visit,s1,s2,s3
        #     visit[i][j] = True
        #     return (i<len1 and (not visit[i+1][j]) and s1[i]==s3[i+j] and dfs(i+1,j)) \
        #            or (j<len2 and (not visit[i][j+1]) and s2[j]==s3[i+j] and dfs(i,j+1)) \
        #            or (i==len1 and j==len2)
        # return dfs(0,0)





# @lc code=end

