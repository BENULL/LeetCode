#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#
# https://leetcode-cn.com/problems/frog-jump/description/
#
# algorithms
# Hard (45.56%)
# Likes:    383
# Dislikes: 0
# Total Accepted:    46.7K
# Total Submissions: 102.6K
# Testcase Example:  '[0,1,3,5,6,8,12,17]'
#
# 一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。
# 
# 给你石子的位置列表 stones（用单元格序号 升序 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。
# 
# 开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃一个单位（即只能从单元格 1 跳至单元格 2 ）。
# 
# 如果青蛙上一步跳跃了 k 个单位，那么它接下来的跳跃距离只能选择为 k - 1、k 或 k + 1 个单位。
# 另请注意，青蛙只能向前方（终点的方向）跳跃。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：stones = [0,1,3,5,6,8,12,17]
# 输出：true
# 解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子,
# 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
# 
# 示例 2：
# 
# 
# 输入：stones = [0,1,2,3,4,8,9,11]
# 输出：false
# 解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
# 
# 
# 
# 提示：
# 
# 
# 2 
# 0 
# stones[0] == 0
# 
# 
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        """dfs
        """
        # end = max(stones)
        # @functools.lru_cache(None)
        # def dfs(i,k):
        #     # if i==0:
        #     #     return dfs(1,1)
        #     if i==end:
        #         return True
        #     if i>end:
        #         return False
        #     for step in [k-1, k, k+1]:
        #         if step>0 and i+step in stones and dfs(i+step,step):
        #             return True
        #     return False
        # return dfs(0,0)

        """dp
        **只有可能以step = k <= i的步子跳到第i块石头，因为跳一步最多增加1步
        """
        # if stones[1]!=1: return False
        # dp = [[False]*len(stones) for _ in range(len(stones))]
        # dp[1][1] = True
        # for i in range(2,len(stones)):
        #     for j in range(1,i):
        #         k = stones[i] - stones[j]
        #         if k<=j+1:
        #             dp[i][k] = dp[j][k-1] or dp[j][k] or dp[j][k+1]
        # for i in range(len(stones)):
        #     if dp[len(stones) - 1][i]: return True 
        # return False

        """bfs
        """
        end = max(stones)
        if stones[1]!=1: return False
        queue = [(1,1)]
        visited = set((1,1))
        while queue:
            i, k = queue.pop(0)
            if i==end:
                return True
            for step in [k-1, k, k+1]:
                if step>0 and i+step in stones and (i+step,step) not in visited :
                    queue.append((i+step,step))
                    visited.add((i+step,step))
        return False
                









# @lc code=end

