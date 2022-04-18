class Solution:
    """
    统计一个数字在排序数组中出现的次数。

     

    示例 1:

    输入: nums = [5,7,7,8,8,10], target = 8
    输出: 2
    示例 2:

    输入: nums = [5,7,7,8,8,10], target = 6
    输出: 0
     

    提示：

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums 是一个非递减数组
    -109 <= target <= 109
    """
    def search(self, nums: List[int], target: int) -> int:

        def helper(tar):
            left, right = 0, len(nums)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] <= tar:
                    left = mid + 1
                else:
                    right = mid -1
            return left
        return helper(target) - helper(target-1)