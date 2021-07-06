#
# @lc app=leetcode.cn id=423 lang=python3
#
# [423] 从英文中重建数字
#
# https://leetcode-cn.com/problems/reconstruct-original-digits-from-english/description/
#
# algorithms
# Medium (56.75%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    7.5K
# Total Submissions: 13.2K
# Testcase Example:  '"owoztneoer"'
#
# 给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。
# 
# 注意:
# 
# 
# 输入只包含小写英文字母。
# 输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
# 输入字符串的长度小于 50,000。
# 
# 
# 示例 1:
# 
# 
# 输入: "owoztneoer"
# 
# 输出: "012" (zeroonetwo)
# 
# 
# 示例 2:
# 
# 
# 输入: "fviefuro"
# 
# 输出: "45" (fourfive)
# 
# 
#

# @lc code=start
class Solution:
    def originalDigits(self, s: str) -> str:
        # cnts = collections.Counter(s)
        # res = ''
        # for num, num_str in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine']):
        #     while min([cnts[c] for c in num_str])>0:
        #         for c in num_str:
        #             cnts[c] -= 1 
        #         res += str(num)
        # return res
        
        # 找规律
        d = {}
        d[0] = s.count('z')
        d[2] = s.count('w')
        d[4]= s.count('u')
        d[6] = s.count('x')
        d[8] = s.count('g')
        d[1] = s.count('o') - d[2] - d[4] - d[0]
        d[3] = s.count('t') - d[2] - d[8]
        d[5] = s.count('f') - d[4]
        d[7] = s.count('s') - d[6]
        d[9] = s.count('i') - d[8] - d[6] - d[5] 
        res = ''
        for i in range(10):
            res += str(i) * d[i]
        return res






# @lc code=end

