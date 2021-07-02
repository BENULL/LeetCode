#
# @lc app=leetcode.cn id=475 lang=python3
#
# [475] 供暖器
#
# https://leetcode-cn.com/problems/heaters/description/
#
# algorithms
# Medium (32.56%)
# Likes:    202
# Dislikes: 0
# Total Accepted:    18.1K
# Total Submissions: 55.6K
# Testcase Example:  '[1,2,3]\n[2]'
#
# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
# 
# 在加热器的加热半径范围内的每个房屋都可以获得供暖。
# 
# 现在，给出位于一条水平线上的房屋 houses 和供暖器 heaters 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。
# 
# 说明：所有供暖器都遵循你的半径标准，加热的半径也一样。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: houses = [1,2,3], heaters = [2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
# 
# 
# 示例 2:
# 
# 
# 输入: houses = [1,2,3,4], heaters = [1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
# 
# 
# 示例 3：
# 
# 
# 输入：houses = [1,5], heaters = [2]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 
# 
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 1. 距离每间房屋最近的供暖器距离 （二分查找或双指针 
        # 2. 这些距离中的最长距离极为最小加热半径
        
        houses.sort()
        heaters.sort()
        res = 0
        for house in houses:
            left, right = 0, len(heaters)-1
            while left<right:
                mid = left + (right - left)//2
                if heaters[mid]<house:
                    left = mid + 1
                else:
                    right = mid
            if heaters[left]==house:
                house_res = 0
            elif heaters[left] < house:
                house_res = house - heaters[left]
            else:
                if left == 0:
                    house_res = heaters[left] - house 
                else:
                    house_res = min(heaters[left]-house,house-heaters[left-1])
            
            res = max(res, house_res)
        return res


        


# @lc code=end

