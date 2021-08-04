#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#
# https://leetcode-cn.com/problems/integer-replacement/description/
#
# algorithms
# Medium (37.55%)
# Likes:    96
# Dislikes: 0
# Total Accepted:    13.2K
# Total Submissions: 35.3K
# Testcase Example:  '8'
#
# 给定一个正整数 n ，你可以做如下操作：
# 
# 
# 如果 n 是偶数，则用 n / 2替换 n 。
# 如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
# 
# 
# n 变为 1 所需的最小替换次数是多少？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 8
# 输出：3
# 解释：8 -> 4 -> 2 -> 1
# 
# 
# 示例 2：
# 
# 
# 输入：n = 7
# 输出：4
# 解释：7 -> 8 -> 4 -> 2 -> 1
# 或 7 -> 6 -> 3 -> 2 -> 1
# 
# 
# 示例 3：
# 
# 
# 输入：n = 4
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:

    # recursive
    # @functools.lru_cache(None)
    # def integerReplacement(self, n: int) -> int:
    #     if n==1: return 0
    #     if n==2: return 1
    #     if n%2==0:
    #         return 1 + self.integerReplacement(n//2)
    #     else:
    #         return 1+min(self.integerReplacement(n+1),self.integerReplacement(n-1))

    def integerReplacement(self, n: int) -> int:
        # bit
        # count = 0
        # while n != 1:
        #     # 偶数(0bXX0)直接右移
        #     if (n & 1) == 0:
        #         n >>= 1
        #     else:
        #         #大于1的奇数格式为XX01或者XX11，对于前一种格式直接-1，对于后一种格式直接+1
        #         #单且仅当只有两位时候0b01(十进制的1)和0b11（十进制的3）时候，对于3，最少的步数应该是-1，因为3 - 1 = 2 / 2 = 1（三步）                #如果+1的话是3 + 1= 4 /2 =  2 / 2 = 1（四步），造成3这个数字比较特殊的原因是因为3的二进制只有2bit(0b11)
        #         n += -1 if (n & 2) == 0 or n == 3 else 1  
        #     count += 1
        # return count


        # bfs
        count = 0
        queue = [(n,0)]
        while queue:
            num, k = queue.pop(0)
            if num==1:
                return k
            if num%2==0:
                queue.append((num//2,k+1))
            else:
                queue.append((num+1,k+1))
                queue.append((num-1,k+1))
        return -1

        

 



# @lc code=end

