#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
# https://leetcode-cn.com/problems/word-break-ii/description/
#
# algorithms
# Hard (49.23%)
# Likes:    523
# Dislikes: 0
# Total Accepted:    55.2K
# Total Submissions: 111.6K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典
# wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 
# 说明：
# 
# 
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# 示例 2：
# 
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """bfs
        """
        # queue = [[0,[]]]
        # visited = [False]*len(s)
        # res = []
        # while queue:
        #     start, path= queue.pop(0)
        #     # if visited[start]:
        #     #     continue
        #     # visited[start] = True
        #     for i in range(start+1, len(s)+1):
        #         if s[start:i] in wordDict:
        #             if i<len(s):
        #                 queue.append([i,path+[i]])
        #             else:
        #                 res.append(path)
        # ans = []
        # if res:
        #     for path in res:
        #         start = 0
        #         sentence = []
        #         for index in path:
        #             sentence.append(s[start:index])
        #             start = index
        #         sentence.append(s[start:])
        #         ans.append(" ".join(sentence))

        # return ans

        """dp
        """
        dp = [[] for _ in range(len(s)+1)]
        # dp[0] = [0]
        for i in range(len(s)):
            for j in range(i,len(s)):
                if (dp[i] or i==0) and s[i:j+1] in wordDict:
                    dp[j+1] += [path+[j+1] for path in dp[i]] if dp[i] else [[j+1]]
        ans = []
        def pairwise(iterable):
            "s -> (s0,s1), (s1,s2), (s2, s3), ..."
            a, b = itertools.tee(iterable)
            next(b, None)
            return zip(a, b)

        if dp[-1]:    
            for path in dp[-1]:
                ans.append(" ".join(s[start:end] for start,end in pairwise([0]+path)))

        # if dp[-1]:
        #     for path in dp[-1]:
        #         start = 0
        #         sentence = []
        #         for index in path:
        #             sentence.append(s[start:index])
        #             start = index
        #         ans.append(" ".join(sentence))
        return ans

# if __name__ == "__main__":
#     s = Solution()
#     print(s.wordBreak("catsanddog",["cat", "cats", "and", "sand", "dog"]))


# @lc code=end

