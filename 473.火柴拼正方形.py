#
# @lc app=leetcode.cn id=473 lang=python3
#
# [473] 火柴拼正方形
#
# https://leetcode-cn.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (41.57%)
# Likes:    188
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 43.3K
# Testcase Example:  '[1,1,2,2,2]'
#
# 
# 还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。
# 
# 输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。
# 
# 示例 1:
# 
# 
# 输入: [1,1,2,2,2]
# 输出: true
# 
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
# 
# 
# 示例 2:
# 
# 
# 输入: [3,3,3,3,4]
# 输出: false
# 
# 解释: 不能用所有火柴拼成一个正方形。
# 
# 
# 注意:
# 
# 
# 给定的火柴长度和在 0 到 10^9之间。
# 火柴数组的长度不超过15。
# 
# 
#

# @lc code=start
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # if not matchsticks:
        #     return False
        
        # L = len(matchsticks)

        # perimeter = sum(matchsticks)

        # possible_side = perimeter // 4
        # if possible_side*4 != perimeter:
        #     return False
        
        # matchsticks.sort(reverse=True)

        # sums = [0 for _ in range(4)]

        # def dfs(index):
        #     if index == L:
        #         return sums[0]==sums[1]==sums[2]==possible_side

        #     for i in range(4):
        #         if sums[i] + matchsticks[index] <= possible_side:
        #             sums[i] += matchsticks[index]
        #             if dfs(index+1):
        #                 return True
        #             sums[i] -= matchsticks[index]
        #     return False
        # return dfs(0)

        _len = sum(matchsticks)
        if _len % 4:
            return False
        matchsticks.sort(reverse=True)
        edges = [0]*4
        def dfs(idx):
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i]<= _len//4 and dfs(idx+1):
                    return True
                edges[i] -= matchsticks[idx]
            return False
            
        return dfs(0)



        
# @lc code=end

