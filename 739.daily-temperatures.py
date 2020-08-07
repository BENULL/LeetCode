#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (63.20%)
# Likes:    2955
# Dislikes: 90
# Total Accepted:    167.6K
# Total Submissions: 264.8K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#

# @lc code=start
class Solution:
    """
        We compute the result in reverse order. Given temperatures = [73, 74, 75, 71, 69, 72, 76, 73], suppose that we already obtain number of days for i >= 3: res = [?, ?, ?, 2, 1, 1, 0, 0] where ? denotes values to be determined. In order to find the number of days for i = 2, we proceed as follows:
        Let j = i + 1, i.e., j = 3. If temperatures[i] < temperatures[j], res[i] = 1;
        Otherwise, temperatures[i] >= temperatures[j]. we examine the value of res[j], which is equal to 2, which means that the most recent day with higher temperature than temperatures[j] in the future is 2 days away. Since temperatures[i] >= temperatures[j], the most recent day with higher temperature than temperatures[i] should be at least 2 days away. Therefore, we can skip some days and arrive directly at day j + res[j]. This process continues until we find higher temperature or we know we should stop as descibed in the third point.
        If temperatures[j] == 0, we shoud directly set res[i] to 0 since we know we cannot find higher temperature in the future.
        The code is as follows. The complexity is O(n) in time and O(1) in space (since we leverage the space of the output).
    """
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        size = len(T)
        res = [0]*size
        for i in range(size-1,-1,-1):
            j = i + 1
            while j<size and T[j]<=T[i]:
                if res[j] > 0:
                    j = res[j]+j
                else:
                    j = size
            if j<size:
                res[i] = j - i
        return res

        
# @lc code=end

