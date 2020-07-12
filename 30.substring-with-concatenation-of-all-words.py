#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (25.28%)
# Likes:    858
# Dislikes: 1237
# Total Accepted:    176.4K
# Total Submissions: 698K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# You are given a string, s, and a list of words, words, that are all of the
# same length. Find all starting indices of substring(s) in s that is a
# concatenation of each word in words exactly once and without any intervening
# characters.
# 
# 
# 
# Example 1:
# 
# 
# Input:
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar"
# respectively.
# The output order does not matter, returning [9,0] is fine too.
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# Output: []
# 
# 
#

# @lc code=start
class Solution:

    # Using a counter and a sliding window, we push the window from left to right, 
    # counting the number of valid words in the window. 
    # When the number of a word in the window is more than the times it appears in words or we meet a invalid word,push the window.
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0: 
            return []
        from collections import deque,defaultdict,Counter
        s_len,word_len = len(s),len(words[0])
        word_len_total = word_len*len(words)
        count = Counter(words)
        _dict = defaultdict(deque)
        res = []
        for start in range(word_len):
            _dict.clear()
            end = start
            while start + word_len_total <= s_len:
                sub = s[end:end+word_len]
                end += word_len
                if sub in count:
                    queue = _dict[sub]
                    queue.append(end)
                    while queue[0] < start:
                        queue.popleft()
                    if len(queue) > count[sub]:
                        start = queue.popleft()
                    if start + word_len_total == end:
                        res.append(start)
                else:
                    start = end
        return res  



        
# @lc code=end

