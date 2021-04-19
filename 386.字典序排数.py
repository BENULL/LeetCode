#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#
# https://leetcode-cn.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (73.57%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    17.4K
# Total Submissions: 23.6K
# Testcase Example:  '13'
#
# 给定一个整数 n, 返回从 1 到 n 的字典顺序。
# 
# 例如，
# 
# 给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。
# 
# 请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。
# 
#

# @lc code=start
import functools
class Solution:
    # def cmp(self,x,y):
    #     x,y = str(x), str(y)
    #     for _x, _y in zip(x,y):
    #         if _x<_y:
    #             return -1
    #         elif _x>_y:
    #             return 1
    #     return -1 if len(x)<len(y) else 1

    # def lexicalOrder(self, n: int) -> List[int]:
    #     nums = list(range(1,n+1))
    #     return sorted(nums,key=functools.cmp_to_key(self.cmp))


    # dfs
    def lexicalOrder(self, n: int) -> List[int]:
        # return sorted(list(range(1,n+1)),key=lambda x:str(x))
        
        res = [] 
        def dfs(num):
            if num>n: return 
            res.append(num)
            for i in range(10):
                dfs(num*10+i)
        
        [dfs(i) for i in range(1,10)]   
        return res


# @lc code=end

