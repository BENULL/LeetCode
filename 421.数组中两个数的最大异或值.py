#
# @lc app=leetcode.cn id=421 lang=python3
#
# [421] 数组中两个数的最大异或值
#
# https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (60.28%)
# Likes:    244
# Dislikes: 0
# Total Accepted:    10.5K
# Total Submissions: 17.4K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# 给定一个非空数组，数组中元素为 a0, a1, a2, … , an-1，其中 0 ≤ ai < 2^31 。
# 
# 找到 ai 和aj 最大的异或 (XOR) 运算结果，其中0 ≤ i,  j < n 。
# 
# 你能在O(n)的时间解决这个问题吗？
# 
# 示例:
# 
# 
# 输入: [3, 10, 5, 25, 2, 8]
# 
# 输出: 28
# 
# 解释: 最大的结果是 5 ^ 25 = 28.
# 
# 
#

# @lc code=start
class Trie:
    def __init__(self,val) -> None:
        self.val = val
        self.child = {}
       
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Trie 前缀树
        # https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/solution/python3-qiao-miao-li-yong-qian-zhui-shu-0alcy/
        
        # 构造前缀树
        L = len(format(max(nums), 'b'))-1

        root = Trie(-1)
        for num in nums:
            curr = root
            for i in range(L,-1,-1):
                v = (num>>i) & 1
                if v not in curr.child:
                    curr.child[v] = Trie(v)
                curr = curr.child[v]
    
        res = 0
        
        for num in nums:
            curr = root
            total = 0
            for i in range(L,-1,-1):
                v = (num>>i) & 1
                if 1-v in curr.child:
                    total = (total<<1) + 1
                    curr = curr.child[1-v]
                else:
                    total <<= 1 
                    curr = curr.child[v]

            res = max(res,total)

        return res


        
# @lc code=end

