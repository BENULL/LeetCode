#
# @lc app=leetcode.cn id=1109 lang=python3
#
# [1109] 航班预订统计
#
# https://leetcode-cn.com/problems/corporate-flight-bookings/description/
#
# algorithms
# Medium (57.98%)
# Likes:    293
# Dislikes: 0
# Total Accepted:    63K
# Total Submissions: 108.1K
# Testcase Example:  '[[1,2,10],[2,3,20],[2,5,25]]\n5'
#
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
# 
# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从
# firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。
# 
# 请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# 输出：[10,55,45,25,25]
# 解释：
# 航班编号        1   2   3   4   5
# 预订记录 1 ：   10  10
# 预订记录 2 ：       20  20
# 预订记录 3 ：       25  25  25  25
# 总座位数：      10  55  45  25  25
# 因此，answer = [10,55,45,25,25]
# 
# 
# 示例 2：
# 
# 
# 输入：bookings = [[1,2,10],[2,2,15]], n = 2
# 输出：[10,25]
# 解释：
# 航班编号        1   2
# 预订记录 1 ：   10  10
# 预订记录 2 ：       15
# 总座位数：      10  25
# 因此，answer = [10,25]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 2 * 10^4
# 1 <= bookings.length <= 2 * 10^4
# bookings[i].length == 3
# 1 <= firsti <= lasti <= n
# 1 <= seatsi <= 10^4
# 
# 
#

# @lc code=start
class DiffArray:
    def __init__(self, nums) -> None:
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1,len(nums)):
            self.diff[i] = nums[i] - nums[i-1]
    def increment(self, i, j, val):
        self.diff[i] += val
        if j+1 < len(self.diff):
            self.diff[j+1] -= val
    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i-1] + self.diff[i]
        return res

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Diff array
        diff = DiffArray([0]*n)
        for booking in bookings:
            diff.increment(booking[0]-1,booking[1]-1,booking[2])
        return diff.result()
# @lc code=end

