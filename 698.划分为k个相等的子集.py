#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
# https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (44.47%)
# Likes:    495
# Dislikes: 0
# Total Accepted:    36.4K
# Total Submissions: 81.8K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
# 
# 示例 1：
# 
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
# 
# 
# 
# 提示：
# 
# 
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
# 
# 
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        partial_sum, mod = divmod(sum(nums), k)
        # 不能整除，肯定不行
        if mod != 0:
            return False

        def dfs(groups) -> bool:
            if not nums:
                return True
            # 优化，接排序
            # 数组被排序过，pop()得到的数为此时最大
            num = nums.pop()
            for i in range(k):
                groups[i] += num
                if groups[i] <= partial_sum:
                    if dfs(groups):
                        return True
                groups[i] -= num
                # 优化
                # 当前项复原后为0，那么后面的结果和此时结果相同
                # 既然当前项都不行，那么之后也不用继续搜索
                if groups[i] == 0:
                    break
            # 复原数组
            nums.append(num)
            return False

        # 优化
        # 排序后先尝试大的数，缩小搜索空间
        nums.sort()
        # 优化
        # 最后一项大于partial_sum，直接返回False
        if nums[-1] > partial_sum:
            return False
        # 优化
        # 缩小搜索空间
        while nums and nums[-1] == partial_sum:
            nums.pop()
            k -= 1
        return dfs([0] * k)

         

# @lc code=end

