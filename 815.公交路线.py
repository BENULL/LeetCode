#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] 公交路线
#
# https://leetcode-cn.com/problems/bus-routes/description/
#
# algorithms
# Hard (43.36%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    27.2K
# Total Submissions: 62.9K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
# 
# 
# 例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1
# -> ... 这样的车站路线行驶。
# 
# 
# 现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
# 
# 求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。 
# 
# 
# 示例 2：
# 
# 
# 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# 输出：-1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 .
# 1 
# routes[i] 中的所有值 互不相同
# sum(routes[i].length) 
# 0 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        # graph bfs

        if source==target: return 0
        queue = []
        buses = defaultdict(set)
        m = dict()
        for index, bus in enumerate(routes):
            for station in bus:
                if source==station:
                    queue.append(index)
                    m[index] = 1
                buses[station].add(index)

        while queue:
            index = queue.pop(0)
            step = m[index]
            for station in routes[index]:
                if station==target:
                    return step
                for bus in buses[station]:
                    if bus not in m:
                        m[bus] = step+1
                        queue.append(bus)
                    
        return -1

# @lc code=end

