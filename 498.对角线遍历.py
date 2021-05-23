#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
# https://leetcode-cn.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (43.17%)
# Likes:    185
# Dislikes: 0
# Total Accepted:    33K
# Total Submissions: 76.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
# 
# 
# 
# 示例:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# 输出:  [1,2,4,7,5,3,6,8,9]
# 
# 解释:
# 
# 
# 
# 
# 
# 说明:
# 
# 
# 给定矩阵中的元素总数不会超过 100000 。
# 
# 
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        # res = list(map(lambda x:list(filter(lambda elem:elem is not None ,x)),
        #         itertools.zip_longest(*map(lambda x:[None]*x[0]+x[1] ,
        #             [(index,_list) for index,_list in enumerate(mat)]))))
        
        # res[::2] = list(map(lambda x:x[::-1],res[::2]))
        # return list(itertools.chain.from_iterable(res))

        # Check for empty matrices
        if not matrix or not matrix[0]:
            return []
        
        # Variables to track the size of the matrix
        N, M = len(matrix), len(matrix[0])
        
        # The two arrays as explained in the algorithm
        result, intermediate = [], []
        
        # We have to go over all the elements in the first
        # row and the last column to cover all possible diagonals
        for d in range(N + M - 1):
            
            # Clear the intermediate array everytime we start
            # to process another diagonal
            intermediate.clear()
            
            # We need to figure out the "head" of this diagonal
            # The elements in the first row and the last column
            # are the respective heads.
            r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
            
            # Iterate until one of the indices goes out of scope
            # Take note of the index math to go down the diagonal
            while r < N and c > -1:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1
            
            # Reverse even numbered diagonals. The
            # article says we have to reverse odd 
            # numbered articles but here, the numbering
            # is starting from 0 :P
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result

# @lc code=end

