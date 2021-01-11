#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (57.55%)
# Likes:    709
# Dislikes: 172
# Total Accepted:    150.4K
# Total Submissions: 252.2K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as
# shown.
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 9
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        board = ['.'*n]*n

        def isValid(board,row,col):
            for i in range(n):
                if board[i][col]=='Q':
                    return False
            for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
                if board[i][j]=='Q':
                    return False
            for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
                if board[i][j]=='Q':
                    return False
            return True

        def backtrack(board,row):
            nonlocal res
            if row == n:
                res+=1
                return 
            for col in range(n):
                if not isValid(board,row,col):
                    continue
                board[row]=board[row][:col]+'Q'+board[row][col+1:]
                backtrack(board,row+1)
                board[row]=board[row][:col]+'.'+board[row][col+1:]

        backtrack(board,0)
        return res
        
# @lc code=end

