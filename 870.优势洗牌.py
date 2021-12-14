#
# @lc app=leetcode.cn id=870 lang=python3
#
# [870] 优势洗牌
#
# https://leetcode-cn.com/problems/advantage-shuffle/description/
#
# algorithms
# Medium (43.34%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    16.4K
# Total Submissions: 37.5K
# Testcase Example:  '[2,7,11,15]\n[1,10,4,11]'
#
# 给定两个大小相等的数组 A 和 B，A 相对于 B 的优势可以用满足 A[i] > B[i] 的索引 i 的数目来描述。
# 
# 返回 A 的任意排列，使其相对于 B 的优势最大化。
# 
# 
# 
# 示例 1：
# 
# 输入：A = [2,7,11,15], B = [1,10,4,11]
# 输出：[2,11,7,15]
# 
# 
# 示例 2：
# 
# 输入：A = [12,24,8,32], B = [13,25,32,11]
# 输出：[24,32,8,12]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # greedy + binary search
        nums1.sort()
        res = []
        for num in nums2:
            index =  bisect.bisect_right(nums1,num)
            if index < len(nums1):
                res.append(nums1[index])
                del nums1[index]
            else:
                res.append(nums1[0])
                del nums1[0]
        return res

        # nums1.sort()
        # ans = []
        # for i in nums2:
        #     j = bisect_right(nums1, i)
        #     if j < len(nums1):
        #         ans.append(nums1[j])
        #         del nums1[j]
        #     else:
        #         ans.append(nums1[0])
        #         del nums1[0]
        # return ans

# @lc code=end

