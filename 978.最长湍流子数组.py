#
# @lc app=leetcode.cn id=978 lang=python3
#
# [978] 最长湍流子数组
#
# https://leetcode-cn.com/problems/longest-turbulent-subarray/description/
#
# algorithms
# Medium (47.34%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    43.2K
# Total Submissions: 91.3K
# Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
#
# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
# 
# 
# 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
# 
# 
# 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
# 
# 返回 A 的最大湍流子数组的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：[9,4,2,10,7,8,8,1,9]
# 输出：5
# 解释：(A[1] > A[2] < A[3] > A[4] < A[5])
# 
# 
# 示例 2：
# 
# 输入：[4,8,12,16]
# 输出：2
# 
# 
# 示例 3：
# 
# 输入：[100]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        brute force slide window
        """

        # _len = len(arr)
        # if _len<2: return _len
        # l = arr[0]-arr[1]
        # maxsize = 1 if l==0 else 2
        # res = maxsize
        # left, right = 1, 2
        # while right<_len:
        #     r = arr[left]-arr[right]
        #     if l*r<0:
        #         maxsize+=1
        #     else:
        #         maxsize= 1 if r==0 else 2
        #     res = max(res,maxsize)
        #     l = r
        #     left+=1
        #     right+=1
        # return res

        """
        dp
        """
        dp = [[1]*2 for _ in range(len(arr))]
        dp[0][0]=dp[0][1]=1
        for i in range(1, len(arr)):
            if arr[i]>arr[i-1]:
                dp[i][0] = dp[i-1][1]+1
            elif arr[i]<arr[i-1]:
                dp[i][1] = dp[i-1][0]+1
            
        return max(j for i in dp for j in i)




# @lc code=end

