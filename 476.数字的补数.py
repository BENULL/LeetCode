#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#
# https://leetcode-cn.com/problems/number-complement/description/
#
# algorithms
# Easy (69.75%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    32.3K
# Total Submissions: 46.2K
# Testcase Example:  '5'
#
# 给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = 5
# 输出：2
# 解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
# 
# 
# 示例 2：
# 
# 
# 输入：num = 1
# 输出：0
# 解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
# 
# 
# 
# 
# 提示：
# 
# 
# 给定的整数 num 保证在 32 位带符号整数的范围内。
# num >= 1
# 你可以假定二进制数不包含前导零位。
# 本题与 1009 https://leetcode-cn.com/problems/complement-of-base-10-integer/ 相同
# 
# 
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        # 1     自己和补数相加等于2**n-1
        # return 2**(len(bin(num))-2)-1 - num

        # 2     因为a^b=c可以推出a^c=b
        return num^(2**(len(bin(num))-2)-1)


# @lc code=end

