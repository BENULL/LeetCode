#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (55.01%)
# Likes:    3946
# Dislikes: 268
# Total Accepted:    659.1K
# Total Submissions: 1.2M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# Find the kth largest element in an unsorted array. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
# 
# Example 1:
# 
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
# 
# Example 2:
# 
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
# 
#

# @lc code=start
class Solution:
    # quick select

    def partion(self,nums,low,high):
        pivot = nums[low]
        while low < high: 
            while low < high and pivot>=nums[high]:
                high-=1
            nums[low] = nums[high]
            while low < high and pivot<nums[low]:
                low+=1
            nums[high] = nums[low]
        nums[high] = pivot
        return high



    def findKthLargest(self, nums: List[int], k: int) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            pos = self.partion(nums,low,high)
            if pos+1 < k:
                low = pos + 1
            elif pos + 1 > k :
                high = pos - 1
            else:
                return nums[pos]
        return nums[low]



        
# @lc code=end

