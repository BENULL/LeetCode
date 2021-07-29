#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#
# https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (44.63%)
# Likes:    193
# Dislikes: 0
# Total Accepted:    16.5K
# Total Submissions: 36.9K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# 给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。
# 
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。
# 
# 找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。
# 
# 示例 1:
# 
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
# ⁠    [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# 
# 示例 2:
# 
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# 
# 示例 3:
# 
# 输入: nums1 = [1,2], nums2 = [3], k = 3 
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # brute force (TLE)
        # all = list(itertools.product(nums1,nums2))
        # all.sort(key=lambda x:x[0]+x[1])
        # return all if len(all)<k else all[:k]

        # return sorted(itertools.product(nums1, nums2), key=sum)[:k]

        #return list(map(list, heapq.nsmallest(k, itertools.product(nums1, nums2), key=sum)))

        # heap prior queue
        queue = []
        res = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue,[nums1[i]+nums2[j], i, j])
        
        push(0, 0)
        while queue and len(res)<k:
            _, i, j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])
            push(i, j+1)
            if j==0:
                push(i+1, 0)
        return res
        




# @lc code=end

