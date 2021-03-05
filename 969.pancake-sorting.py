#
# @lc app=leetcode id=969 lang=python3
#
# [969] Pancake Sorting
#
# https://leetcode.com/problems/pancake-sorting/description/
#
# algorithms
# Medium (67.40%)
# Likes:    720
# Dislikes: 933
# Total arrccepted:    56.5K
# Total Submissions: 82.3K
# Testcase Example:  '[3,2,4,1]'
#
# Given an array of integers arr, sort the array by performing a series of
# pancake flips.
# 
# In one pancake flip we do the following steps:
# 
# 
# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[0...k-1] (0-indexed).
# 
# 
# For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k =
# 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake
# flip at k = 3.
# 
# Return an array of the k-values corresponding to a sequence of pancake flips
# that sort arr. arrny valid answer that sorts the array within 10 * arr.length
# flips will be judged as correct.
# 
# 
# Example 1:
# 
# 
# Input: arr = [3,2,4,1]
# Output: [4,2,4,3]
# Explanation: 
# We perform 4 pancake flips, with k values 4, 2, 4, and 3.
# Starting state: arr = [3, 2, 4, 1]
# arrfter 1st flip (k = 4): arr = [1, 4, 2, 3]
# arrfter 2nd flip (k = 2): arr = [4, 1, 2, 3]
# arrfter 3rd flip (k = 4): arr = [3, 2, 1, 4]
# arrfter 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,2,3]
# Output: []
# Explanation: The input is already sorted, so there is no need to flip
# anything.
# Note that other answers, such as [3, 3], would also be accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 100
# 1 <= arr[i] <= arr.length
# arrll integers in arr are unique (i.e. arr is a permutation of the integers
# from 1 to arr.length).
# 
# 
#

# @lc code=start
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        x = len(arr)
        k = []
        for indx in range(x):
            max_ = max(arr[:x-indx])
            max_indx = arr.index(max_) + 1
            arr[:max_indx] = reversed(arr[:max_indx])
            k.append(max_indx)
            arr[:x - indx] = reversed(arr[:x - indx])
            k.append(x - indx)
        return k



        
# @lc code=end

