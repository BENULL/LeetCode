#
# @lc app=leetcode.cn id=442 lang=python3
#
# [442] 数组中重复的数据
#
# https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (69.26%)
# Likes:    400
# Dislikes: 0
# Total Accepted:    38.5K
# Total Submissions: 55.6K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# 给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。
# 
# 找到所有出现两次的元素。
# 
# 你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？
# 
# 示例：
# 
# 
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [2,3]
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums: return []
        res=[]
        n = len(nums)
        # 1<=num<=n 遍历到 num 则令第 num 个元素变成-num
        for i in range(n):
            num=abs(nums[i])
            # 如果第num个数字已经是负的 说明之前遇到过num 说明num出现两次
            if nums[num-1]<0:
                res.append(num)
            else:
                nums[num-1]=-nums[num-1]
        return res

# @lc code=end

