class Solution:
    """
    我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

    示例:

    输入: n = 10
    输出: 12
    解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
    说明:  

    1 是丑数。
    n 不超过1690。
    注意：本题与主站 264 题相同：https://leetcode-cn.com/problems/ugly-number-ii/



    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/chou-shu-lcof
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1]*n, 0, 0, 0
        for i in range(1,n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]