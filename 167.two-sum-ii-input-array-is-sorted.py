#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
#
# algorithms
# Easy (53.88%)
# Likes:    1766
# Dislikes: 625
# Total Accepted:    431.1K
# Total Submissions: 796.6K
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2.
# 
# Note:
# 
# 
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Example:
# 
# 
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# 
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        # l, r = 0, len(numbers)-1
        # while l < r:
        #     num = numbers[l]+numbers[r]
        #     if num == target:
        #         return [l+1,r+1]
        #     elif num < target:
        #         l+=1
        #     else:
        #         r-=1


        # dict
        # _dict = {}
        # for i,num in enumerate(numbers):
        #     if target - num in _dict:
        #         return [_dict[target-num]+1,i+1]
        #     _dict[num] = i 


        # binary search
        for i in range(len(numbers)):
            l, r = i+1,len(numbers)-1
            tmp = target - numbers[i]
            while l<=r:
                mid = (l+r)//2
                if numbers[mid] == tmp:
                    return [i+1,mid+1]
                elif numbers[mid] < tmp:
                    l = mid+1
                else:
                    r = mid-1
        
# @lc code=end

