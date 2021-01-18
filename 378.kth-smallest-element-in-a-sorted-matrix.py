#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (54.06%)
# Likes:    3193
# Dislikes: 168
# Total Accepted:    234.1K
# Total Submissions: 419K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n^2.
#

# @lc code=start
class Solution:
    # binary search with range
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi =matrix[0][0], matrix[-1][-1]
        while lo<=hi:
            mid = lo + (hi-lo)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     return sorted(itertools.chain.from_iterable(matrix))[k-1]

            
        
# @lc code=end

