#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (48.59%)
# Likes:    9714
# Dislikes: 148
# Total Accepted:    661.8K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 0 <= n <= 3 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
from pip import main


class Solution:
    # brute force
    # def trap(self, height: List[int]) -> int:
    #     if not height:
    #         return 0
    #     index = height.index(max(height))
    #     return self.helper(height[:index+1])+self.helper(height[:index-len(height)-1:-1])

        
    # def helper(self,height):
    #     res = 0
    #     if len(height)<3:
    #         return res
    #     i = 0
    #     while i < len(height)-1:
    #         if height[i]>0:
    #             firstMaxIndex = i + 1
    #             while firstMaxIndex <len(height) and height[firstMaxIndex]<height[i]:
    #                 firstMaxIndex += 1
    #             if firstMaxIndex <len(height):
    #                 res += (min(height[i],height[firstMaxIndex])*(firstMaxIndex-i-1))-sum(height[i+1:firstMaxIndex])
    #                 i = firstMaxIndex
    #             else:
    #                 i += 1
    #         else:
    #             i += 1
    #     return res


    # two pointer
    """
    使用 height[left]\textit{height}[\textit{left}]height[left] 和 height[right]\textit{height}[\textit{right}]height[right] 的值更新 leftMax\textit{leftMax}leftMax 和 rightMax\textit{rightMax}rightMax 的值；

如果 height[left]<height[right]\textit{height}[\textit{left}]<\textit{height}[\textit{right}]height[left]<height[right]，则必有 leftMax<rightMax\textit{leftMax}<\textit{rightMax}leftMax<rightMax，下标 left\textit{left}left 处能接的雨水量等于 leftMax−height[left]\textit{leftMax}-\textit{height}[\textit{left}]leftMax−height[left]，将下标 left\textit{left}left 处能接的雨水量加到能接的雨水总量，然后将 left\textit{left}left 加 111（即向右移动一位）；

如果 height[left]≥height[right]\textit{height}[\textit{left}] \ge \textit{height}[\textit{right}]height[left]≥height[right]，则必有 leftMax≥rightMax\textit{leftMax} \ge \textit{rightMax}leftMax≥rightMax，下标 right\textit{right}right 处能接的雨水量等于 rightMax−height[right]\textit{rightMax}-\textit{height}[\textit{right}]rightMax−height[right]，将下标 right\textit{right}right 处能接的雨水量加到能接的雨水总量，然后将 right\textit{right}right 减 111（即向左移动一位）。
    """
    def trap(self, height) -> int:
        # left, right = 0, len(height)-1
        # ans = 0
        # left_max, right_max = 0, 0 
        # while left<=right:
        #     if left_max<right_max:
        #         ans+=max(0,left_max-height[left])
        #         left_max=max(left_max,height[left])
        #         left+=1
        #     else:
        #         ans+=max(0,right_max-height[right])
        #         right_max=max(right_max,height[right])
        #         right-=1
        # return ans
    
        # dp
        # 预处理 
        # 得到leftMax 和 rightMax数组
        # min(leftMax[i],rightMax[i])−height[i]）


        # if not height:
        #     return 0
            
        # n = len(height)
        # leftMax = [height[0]] + [0] * (n - 1)
        # for i in range(1, n):
        #     leftMax[i] = max(leftMax[i - 1], height[i])

        # rightMax = [0] * (n - 1) + [height[n - 1]]
        # for i in range(n - 2, -1, -1):
        #     rightMax[i] = max(rightMax[i + 1], height[i])

        # ans = sum(min(leftMax[i], rightMax[i]) - height[i] for i in range(n))
        # return ans


        # 单调栈 计算行雨水量 上面的计算列的雨水量
        stack = []
        res = 0
        # n = len(height)
        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                curWidth = i-left-1
                curHeight = min(height[left], h)-height[top]
                res += curWidth*curHeight
            stack.append(i)
        return res

if __name__ == '__main__':
    s = Solution()
    s.trap([0,1,0,2,1,0,1,3,2,1,2,1])



        
# @lc code=end

