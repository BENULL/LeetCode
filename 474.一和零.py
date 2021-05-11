#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
# https://leetcode-cn.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (55.81%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    38.7K
# Total Submissions: 69.1K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# 给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
# 
# 
# 请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
# 
# 如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
# 输出：4
# 解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
# 其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于
# n 的值 3 。
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["10", "0", "1"], m = 1, n = 1
# 输出：2
# 解释：最大的子集是 {"0", "1"} ，所以答案是 2 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 1 
# strs[i] 仅由 '0' 和 '1' 组成
# 1 
# 
# 
#

# @lc code=start
class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dfs
        # maxLen = 0 

        # def counter(strs):
        #     c = Counter(''.join(strs))
        #     return c['0']<=m and c['1']<=n

        # def dfs(strs,res):
        #     if not strs: return
        #     nonlocal maxLen
        #     if counter(res):
        #         s = strs[0]
        #         res.append(s)
        #         if counter(res):
        #             maxLen = max(maxLen,len(res))
        #             dfs(strs[1:],res)
        #         res.pop()
        #         dfs(strs[1:],res)

        # dfs(strs,[])
        # return maxLen


        N=len(strs)
        @lru_cache(None)
        def dfs(index,m,n,t):
            if m<0 or n<0:
                return t-1
            if index==N:
                return t
            t=max(dfs(index+1,m,n,t),dfs(index+1,m-strs[index].count('0'),n-strs[index].count('1'),t+1))
            return  t
        return dfs(0,m,n,0)

    
# @lc code=end

