#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (46.25%)
# Likes:    2500
# Dislikes: 95
# Total Accepted:    232.8K
# Total Submissions: 476K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard
# such that no two queens attack each other.
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [["Q"]]
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
from typing import *
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
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
            if row == n:
                res.append(board[:])
                return 
            for col in range(n):
                if not isValid(board,row,col):
                    continue
                board[row]=board[row][:col]+'Q'+board[row][col+1:]
                backtrack(board,row+1)
                board[row]=board[row][:col]+'.'+board[row][col+1:]

        backtrack(board,0)
        return res
        
if __name__ == "__main__":
    s = Solution()
    s.solveNQueens(1)

# @lc code=end
