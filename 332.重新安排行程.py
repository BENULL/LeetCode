#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
# https://leetcode-cn.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (44.58%)
# Likes:    417
# Dislikes: 0
# Total Accepted:    34K
# Total Submissions: 76.4K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从
# JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 开始。
# 
# 
# 
# 提示：
# 
# 
# 如果存在多种有效的行程，请你按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"]
# 相比就更小，排序更靠前
# 所有的机场都用三个大写字母表示（机场代码）。
# 假定所有机票至少存在一种合理的行程。
# 所有的机票必须都用一次 且 只能用一次。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# 输出：["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
# 
# 示例 2：
# 
# 
# 输入：[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
# 
#

# @lc code=start
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer 算法
        # 一笔画的最后一划一定是死胡同。
        # 因为无论从哪个点开始递归，一定是进入到”死胡同“后无其他路径可走，开始返回。dfs函数内，while循环结束后（既无其他递归可以调用）再将当前节点加入结果集保证了”死胡同”一定是第一个进入结果集的节点。对于其他节点，都是偶数出入度的节点，你随便怎么拆边总是能都拆完。（但在这个题中，heap保证了拆边的字典顺序）。
        def dfs(curr):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)
            
        vec = collections.defaultdict(list)
        for start, end in tickets:
            vec[start].append(end)
        
        for key in vec:
            heapq.heapify(vec[key])
        
        stack = []
        dfs('JFK')
        return stack[::-1]

# @lc code=end

