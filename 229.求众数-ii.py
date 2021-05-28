#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
# https://leetcode-cn.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (45.41%)
# Likes:    358
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 64K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的整数数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
# 
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[3,2,3]
# 输出：[3]
# 
# 示例 2：
# 
# 
# 输入：nums = [1]
# 输出：[1]
# 
# 
# 示例 3：
# 
# 
# 输入：[1,1,1,3,3,2,2,2]
# 输出：[1,2]
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^9 
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
       
        # there can be at most two majority elements
        # think of 3 segments: m, n, l
        # m & n is some candidate number
        # l is anything else
        # if l is longer than m, m stops being majority (majority becomes n and l)
        # elif l is longer than n, n stops being majority (majority becomes m and l)
        # elif l is same length as m & n, there's no majority
        
        # a number isn't necessarily a majority just because it survives the pair off 
        # but if a number doesn't survive pair off, it definitely can't be a majority
		
		# if a number is a majority, it will always survive the pair off or come back later
        
        # key idea is that if a number is over n/3, the ratio of it versus the rest is at least 1:2 and it always comes back as a candidate
        
        m, m_count, n, n_count = 0, 0, 1, 0
        for num in nums: 
            # adds to lead of m
            if num == m:
                m_count += 1
            # adds to lead of n
            elif num == n:
                n_count += 1
            
            # l is the same length as m
            elif m_count == 0:
                # set a new candidate (previous candidate can always come back)
                m = num
                m_count = 1
                
            # l is the same length as n
            elif n_count == 0:
                # set a new candidate
                n = num
                n_count = 1
                
            # close the gap between l and m/n
            else:
                m_count -= 1
                n_count -= 1
        third = len(nums)/3
        res = []
        
        if m_count > 0:
            if nums.count(m) > third:
                res.append(m)
        if n_count > 0:
            if nums.count(n) > third:
                res.append(n)
        return res

# @lc code=end

