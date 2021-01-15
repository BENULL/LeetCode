#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (38.00%)
# Likes:    3234
# Dislikes: 131
# Total Accepted:    323.8K
# Total Submissions: 826.8K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
# 
# Example: 
# 
# 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
# 
#

# @lc code=start
class Solution:
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # O(n)
        # slide window 
        # l = 0
        # res = len(nums)+1
        # _sum = 0
        # for r in range(len(nums)):
        #     _sum += nums[r]
        #     while _sum>=s:
        #         res = min(res,r-l+1)
        #         _sum -= nums[l]
        #         l+=1
        # return res if res<len(nums)+1 else 0

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # binary search 
        # O(nlogn)
        n, res = len(nums),len(nums)+1
        sums = [0]*(n+1)
        for i in range(1,n+1):
            sums[i] = sums[i-1]+nums[i-1]
        for left in range(0,n+1):
            right = self.binarySearch(left+1,n,sums[left]+s,sums)
            if right == n+1:
                break
            res = min(res,right-left)
        return 0 if res==n+1 else res

    def binarySearch(self,left,right,val,sums):
        while left<=right:
            mid = left+(right-left)//2
            if sums[mid]<val:
                left = mid+1
            else:  
                right = mid-1
        return left






        
# @lc code=end

