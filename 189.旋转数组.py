#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#
# https://leetcode-cn.com/problems/rotate-array/description/
#
# algorithms
# Medium (45.86%)
# Likes:    945
# Dislikes: 0
# Total Accepted:    248K
# Total Submissions: 540.9K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 
# 
# 
# 进阶：
# 
# 
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
# 
# 
# 示例 2:
# 
# 
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100]
# 
# 
# 
# 提示：
# 
# 
# 1 
# -2^31 
# 0 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Solution 1: 插入

        # n = len(nums)
        # k %= n
        # for _ in range(k):
        #     nums.insert(0, nums.pop())

        # Solution 2: 翻转
        n = len(nums)
        k %= n
        # nums[:] = nums[::-1]
        # nums[:k] = nums[:k][::-1]
        # nums[k:] = nums[k:][::-1]

        # nums[:]=nums[n-k:]+nums[:n-k]

        
        # def swap(l,r):
        #     while(l<r):
        #         nums[l],nums[r]=nums[r],nums[l]
        #         l=l+1
        #         r=r-1
        # swap(0,n-k-1)
        # swap(n-k,n-1)
        # swap(0,n-1)

        # Solution 3: 环状替换
        # https://leetcode-cn.com/problems/rotate-array/solution/xuan-zhuan-shu-zu-yuan-di-huan-wei-xiang-xi-tu-jie/
        cnt = 0
        start = 0
        while cnt < n:
            current = start
            pre = nums[start]
            while True:
                nxt = (current + k) % len(nums)
                nums[nxt], pre = pre, nums[nxt]
                current = nxt
                cnt += 1
                if start == current:
                    break
            start += 1



        



# @lc code=end

