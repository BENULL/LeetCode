#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (42.83%)
# Likes:    5247
# Dislikes: 217
# Total Accepted:    370K
# Total Submissions: 829K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# You are given an array of integers nums, there is a sliding window of size k
# which is moving from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position.
# 
# Return the max sliding window.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,-1], k = 1
# Output: [1,-1]
# 
# 
# Example 4:
# 
# 
# Input: nums = [9,11], k = 2
# Output: [11]
# 
# 
# Example 5:
# 
# 
# Input: nums = [4,-2], k = 2
# Output: [4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    # Brute Force 
    # Time Limit Exceeded

    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     return nums and [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
    
    # deque
    # https://leetcode.com/problems/sliding-window-maximum/discuss/871317/Clear-thinking-process-with-PICTURE-brute-force-to-mono-deque-pythonjavajavascript
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        res = []
        for i, cur in enumerate(nums):
            while q and nums[q[-1]]<=cur:
                q.pop()
            q.append(i)
            if q[0] == i-k:
                q.popleft()
            if i >= k - 1:
                res.append(nums[q[0]])
        return res


        
# @lc code=end

