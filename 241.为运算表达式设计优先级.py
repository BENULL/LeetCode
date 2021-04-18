#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
# https://leetcode-cn.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (73.41%)
# Likes:    360
# Dislikes: 0
# Total Accepted:    23.4K
# Total Submissions: 31.8K
# Testcase Example:  '"2-1-1"'
#
# 给定一个含有数字和运算符的字符串，为表达式添加括号，改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。有效的运算符号包含 +, - 以及
# * 。
# 
# 示例 1:
# 
# 输入: "2-1-1"
# 输出: [0, 2]
# 解释: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
# 
# 示例 2:
# 
# 输入: "2*3-4*5"
# 输出: [-34, -14, -10, -10, 10]
# 解释: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
# 
#

# @lc code=start
import operator
from typing import List
class Solution:

    

    # def findOp(self,expression):
    #         for i,s in enumerate(expression):
    #             if s=='+' or s=='-' or s=='*':
    #                 return i,s
    #         return -1,-1
    
    # def diffWaysToCompute(self, s: str) -> List[int]:
    #     # dfs
    #     # import operator
    #     res = []
    #     ops = {'+':operator.add,'-':operator.sub,'*':operator.mul}

    #     index, op = self.findOp(expression)
    #     if index>0:
    #         left = int(expression[:index])
    #         right = self.diffWaysToCompute(expression[index+1:])
    #         res = [ops[op](left,r) for r in right]

    #         index2, _ = self.findOp(expression[index+1:])
    #         if index2>0:
    #             right2 = int(expression[index+1:index+1+index2])
    #             rightans = ops[op](left,right2)
    #             res.extend(self.diffWaysToCompute(str(rightans)+expression[index+1+index2:]))
    #     else:
    #         res.append(eval(expression))

    #     return res

        # 分治
        # if s.isdigit(): return [int(s)]
        # res = []
        # for i, c in enumerate(s):
        #     if c in '+-*':
        #         for left in self.diffWaysToCompute(s[:i]):
        #             for right in self.diffWaysToCompute(s[i+1:]):
        #                 res.append(eval(f'{left}{c}{right}'))
        # return res


    def diffWaysToCompute(self, input: str):
        # 递归 + 备忘录
        self.formula = input
        self.memo = {}
        return self._diffWaysToCompute(0, len(input))

    def _diffWaysToCompute(self, lo, hi):
        if self.formula[lo:hi].isdigit():
            return [int(self.formula[lo:hi])]
        if((lo, hi) in self.memo):
            return self.memo.get((lo, hi))
        ret = []
        for i, char in enumerate(self.formula[lo:hi]):
            if char in ['+', '-', '*']:
                leftResult = self._diffWaysToCompute(lo, i + lo)
                rightResult = self._diffWaysToCompute(lo + i + 1, hi)
                ret.extend([eval(str(i) + char + str(j)) for i in leftResult for j in rightResult])
                self.memo[(lo, hi)] = ret
        return ret






# @lc code=end

