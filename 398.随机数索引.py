#
# @lc app=leetcode.cn id=398 lang=python3
#
# 水塘抽样法[398] 随机数索引
#
# https://leetcode-cn.com/problems/random-pick-index/description/
#
# algorithms
# Medium (63.68%)
# Likes:    103
# Dislikes: 0
# Total Accepted:    11.3K
# Total Submissions: 17.7K
# Testcase Example:  '["Solution","pick","pick","pick"]\n[[[1,2,3,3,3]],[3],[1],[3]]'
#
# 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。
# 
# 注意：
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
# 
# 示例:
# 
# 
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
# solution.pick(3);
# 
# // pick(1) 应该返回 0。因为只有nums[0]等于1。
# solution.pick(1);
# 
# 
#

# @lc code=start

class Solution:

    def __init__(self, nums: List[int]):
        # self._dict = collections.defaultdict(list)
        # for i,n in enumerate(nums):
        #     self._dict[n].append(i)
        self.nums = nums

    def pick(self, target: int) -> int:
        # index = self._dict[target]

        # return index[random.randint(0,len(index)-1)]

        ll = [i for i in range(len(self.nums)) if self.nums[i] == target]
        # return ll[random.randint(0, len(ll) - 1)] 
        return random.choice(ll)

        # 水塘抽样法
        # i = 1
        # res = None
        # for idx,v in enumerate(self.nums):
        #     if v == target:
        #         if random.randint(1, i) == 1:   # 取1的概率为1/i
        #             res = idx
        #         i += 1
        # return res







# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

