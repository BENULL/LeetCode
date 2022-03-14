import itertools
class Solution:
    """
    给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。



 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

    """
    
    def exist(self, board, word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, length, visited):
            if length==len(word):
                return True
            visited[i][j] = True
            for x, y in [(-1,0), (1,0), (0, 1), (0, -1)]:
                x, y = x+i, y+j
                if 0<=x<m and 0<=y<n and not visited[x][y] and board[x][y]==word[length]:
                    if dfs(x, y, length+1, visited):
                        return True
                    else:
                        visited[x][y] = False

            return False
        for i,j in itertools.product(range(m), range(n)):
            if board[i][j] == word[0]:
                visited=[[False]*n for _ in range(m)]
                res = dfs(i,j, 1, visited)
                if res:
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]],"ABCESEEEFS"))