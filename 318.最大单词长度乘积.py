#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (66.40%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    14.9K
# Total Submissions: 22.3K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j])
# 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
# 
# 示例 1:
# 
# 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16 
# 解释: 这两个单词为 "abcw", "xtfn"。
# 
# 示例 2:
# 
# 输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4 
# 解释: 这两个单词为 "ab", "cd"。
# 
# 示例 3:
# 
# 输入: ["a","aa","aaa","aaaa"]
# 输出: 0 
# 解释: 不存在这样的两个单词。
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # brute force

        # words.sort(key=len,reverse=True)
        # res = 0
        # for i in range(len(words)):
        #     for j in range(i+1,len(words)):
        #         if not set(words[i]).intersection(words[j]):
        #             res = max(len(words[i])*len(words[j]),res)
        #             break
        # return  res
        

        # 优化
        # 方法一：最小化寻找是否有共同字母方法的时间复杂度

        # 方法二：最小化单词的比较次数。在所有具有相同字符集的单词中只保留最长的一个单词。


        hashmap = defaultdict(int)
        bit_number = lambda ch : ord(ch) - ord('a')
        
        for word in words:
            bitmask = 0
            for ch in word:
                # add bit number bit_number in bitmask
                bitmask |= 1 << bit_number(ch)
            # there could be different words with the same bitmask
            # ex. ab and aabb
            hashmap[bitmask] = max(hashmap[bitmask], len(word))
        
        max_prod = 0
        for x in hashmap:
            for y in hashmap:
                if x & y == 0:
                    max_prod = max(max_prod, hashmap[x] * hashmap[y])
        return max_prod







# @lc code=end