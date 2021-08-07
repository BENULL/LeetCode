#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#
# https://leetcode-cn.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (35.88%)
# Likes:    300
# Dislikes: 0
# Total Accepted:    31.4K
# Total Submissions: 87.4K
# Testcase Example:  '3\n5\n4'
#
# 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
# 
# 如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
# 
# 你允许：
# 
# 
# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空
# 
# 
# 示例 1: (From the famous "Die Hard" example)
# 
# 输入: x = 3, y = 5, z = 4
# 输出: True
# 
# 
# 示例 2:
# 
# 输入: x = 2, y = 6, z = 5
# 输出: False
# 
# 
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:

        # bfs
        if x + y < z:
            return False
        queue = [(0, 0)]
        seen = set((0, 0))

        while(len(queue) > 0):
            a, b = queue.pop(0)
            if a ==z or b == z or a + b == z:
                return True
            states = set()

            states.add((x, b))
            states.add((a, y))
            states.add((0, b))
            states.add((a, 0)) 
            states.add((min(x, b + a), 0 if b < x - a else b - (x - a))) 
            states.add((0 if a + b < y else a - (y - b), min(b + a, y)))
            for state in states:
                if state in seen:
                    continue
                queue.append(state)
                seen.add(state)
        return False

# @lc code=end

