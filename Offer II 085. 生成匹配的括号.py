class Solution:
    """
    正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

    示例 1：

    输入：n = 3
    输出：["((()))","(()())","(())()","()(())","()()()"]
    示例 2：

    输入：n = 1
    输出：["()"]
     

    提示：

    1 <= n <= 8
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrace(S, left, right):
            if len(S)==2*n:
                res.append(''.join(S))
                return 
            if left<n:
                S.append('(')
                backtrace(S, left+1, right)
                S.pop()
            if right<left:
                S.append(')')
                backtrace(S, left, right+1)
                S.pop()

        backtrace([], 0, 0)
        return res