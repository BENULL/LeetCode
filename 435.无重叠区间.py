#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
# https://leetcode-cn.com/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (50.77%)
# Likes:    464
# Dislikes: 0
# Total Accepted:    83.3K
# Total Submissions: 163.1K
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
#
# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
# 
# 注意:
# 
# 
# 可以认为区间的终点总是大于它的起点。
# 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
# 
# 
# 示例 1:
# 
# 
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 
# 输出: 1
# 
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
# 
# 
# 示例 2:
# 
# 
# 输入: [ [1,2], [1,2], [1,2] ]
# 
# 输出: 2
# 
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
# 
# 
# 示例 3:
# 
# 
# 输入: [ [1,2], [2,3] ]
# 
# 输出: 0
# 
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
# 
# 
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # greedy 右端点排序 
        # if not intervals: return 0
        # intervals.sort(key=lambda x:x[1])
        # count = 0
        # start, end = intervals[0]
        # for l, r in intervals[1:]:
        #     if l<end:
        #         count += 1
        #     else:
        #         start, end = l, r
        # return count

        # dp 最长上升子序列 n2 TLE 可优化到nlogn
        # intervals.sort()
        # dp = [1]*len(intervals)
        # for i in range(1,len(intervals)):
        #     for j in range(i):
        #         if intervals[j][1]<=intervals[i][0]:
        #             dp[i]=max(dp[i],dp[j]+1)
        # return len(intervals)-dp[len(intervals)-1]


        # 列表推导优化 TLE
        intervals.sort()
        _len = len(intervals)
        dp = [1]
        for i in range(1,_len):
            dp.append(max((dp[j] for j in range(i) if intervals[j][1]<=intervals[i][0]),default = 0)+1)
        return _len-dp[_len-1]





    

                




# @lc code=end

