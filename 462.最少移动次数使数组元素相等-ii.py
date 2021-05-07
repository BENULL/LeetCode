#
# @lc app=leetcode.cn id=462 lang=python3
#
# [462] 最少移动次数使数组元素相等 II
#
# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/description/
#
# algorithms
# Medium (59.64%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    11.2K
# Total Submissions: 18.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。
# 
# 例如:
# 
# 
# 输入:
# [1,2,3]
# 
# 输出:
# 2
# 
# 说明：
# 只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）： 
# 
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
# 
# 
#

# @lc code=start
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # 当 x 为这个 N 个数的中位数时
        # https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/solution/jiang-dao-li-by-carudy/

        nums.sort()
        i, j = 0, len(nums)-1
        ans = 0
        while i<j:
            ans += nums[j]-nums[i]
            i += 1
            j -= 1     
        return ans

# @lc code=end

