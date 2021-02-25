#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#
# https://leetcode.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (43.99%)
# Likes:    3790
# Dislikes: 71
# Total Accepted:    273.8K
# Total Submissions: 583.6K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# Median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value. So the median is the mean of the two
# middle value.
# For example,
# 
# [2,3,4], the median is 3
# 
# [2,3], the median is (2 + 3) / 2 = 2.5
# 
# Design a data structure that supports the following two operations:
# 
# 
# void addNum(int num) - Add a integer number from the data stream to the data
# structure.
# double findMedian() - Return the median of all elements so far.
# 
# 
# 
# 
# Example:
# 
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 
# 
# 
# Follow up:
# 
# 
# If all integer numbers from the stream are between 0 and 100, how would you
# optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how
# would you optimize it?
# 
# 
#

# @lc code=start
from heapq import *
import bisect

class MedianFinder:

    # Solution 1 : two heap

    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.smaller = []
    #     self.larger = []
        

    # def addNum(self, num: int) -> None:
    #   if len(self.smaller) == len(self.larger):
    #     heappush(self.larger,-heappushpop(self.smaller,-num))
    #   else:
    #     heappush(self.smaller,-heappushpop(self.larger,num))

    # def findMedian(self) -> float:
    #   if len(self.smaller) == len(self.larger):
    #     return float(self.larger[0]-self.smaller[0])/2.0
    #   else:
    #     return float(self.larger[0])

    # Solution 2: binary search insert
    def __init__(self):
      self.nums = []

    def addNum(self, num: int) -> None:
      bisect.insort(self.nums,num)

    def findMedian(self): 
      if len(self.nums)%2 == 0:
        temp = len(self.nums)//2
        return (self.nums[temp]+self.nums[temp-1])/2.0
      else:
        return self.nums[len(self.nums)//2]


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

