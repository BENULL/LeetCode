#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (72.79%)
# Likes:    392
# Dislikes: 0
# Total Accepted:    41.2K
# Total Submissions: 56.7K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。
# 
# 
# 
# 进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [1,2,1,3,2,5]
# 输出：[3,5]
# 解释：[5, 3] 也是有效的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [-1,0]
# 输出：[-1,0]
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [0,1]
# 输出：[1,0]
# 
# 
# 提示：
# 
# 
# 2 
# -2^31 
# 除两个只出现一次的整数外，nums 中的其他数字都出现两次
# 
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # return list(map(operator.itemgetter(0),filter(lambda x: x[1]==1,collections.Counter(nums).items())))
        # return list(map(operator.itemgetter(0),collections.Counter(nums).most_common()[-2:]))


        # 分组异或
        ret = functools.reduce(operator.xor, nums)
        div = 1
        while div & ret == 0:
            div <<= 1
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]

# @lc code=end

