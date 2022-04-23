class Solution:
    """
    一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

    示例 1：

    输入：nums = [4,1,4,6]
    输出：[1,6] 或 [6,1]
    示例 2：

    输入：nums = [1,2,10,4,1,4,3,3]
    输出：[2,10] 或 [10,2]
     

    限制：

    2 <= nums.length <= 10000

    """
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = functools.reduce(lambda x, y: x^y, nums)
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
