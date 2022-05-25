class Solution:
    """
        在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。例如，在数组{5, 8, 4, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷  的交替顺序排序。

    示例:

    输入: [5, 3, 1, 2, 3]
    输出: [5, 1, 3, 2, 3]
    提示：

    nums.length <= 10000

    """
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-1):
            if (i&1==1 and nums[i]<nums[i+1]) or (i&1==0 and nums[i]>nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
         