class Solution:
    """
    剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

    

    示例：

    输入：nums = [1,2,3,4]
    输出：[1,3,2,4] 
    注：[3,1,2,4] 也是正确的答案之一。
    

    提示：

    0 <= nums.length <= 50000
    0 <= nums[i] <= 10000
    通过次数246,018提交次数380,780

    """
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1
        while i<j:
            while i<j and nums[i] & 1 == 1: i+=1
            while i<j and nums[j] & 1 == 0: j-=1
            nums[i], nums[j] = nums[j], nums[i]
        return nums