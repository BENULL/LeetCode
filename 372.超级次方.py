#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#
# https://leetcode-cn.com/problems/super-pow/description/
#
# algorithms
# Medium (49.79%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    12.4K
# Total Submissions: 24.9K
# Testcase Example:  '2\n[3]'
#
# 你的任务是计算 a^b 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：a = 2, b = [3]
# 输出：8
# 
# 
# 示例 2：
# 
# 
# 输入：a = 2, b = [1,0]
# 输出：1024
# 
# 
# 示例 3：
# 
# 
# 输入：a = 1, b = [4,3,3,8,5,2]
# 输出：1
# 
# 
# 示例 4：
# 
# 
# 输入：a = 2147483647, b = [2,0,0]
# 输出：1198
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# 0 
# b 不含前导 0
# 
# 
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # 快速幂取模
        # https://leetcode-cn.com/problems/super-pow/solution/you-qian-ru-shen-kuai-su-mi-suan-fa-xiang-jie-by-l/
        base = 1337

        if not b:
            return 1
        last = b.pop()

        part1 = (a ** last) % base
        part2 = (self.superPow(a, b) ** 10) % base

        return (part1 * part2) % base


# @lc code=end

