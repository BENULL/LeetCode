class Solution:
    """
    给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
    示例 1:

    输入: 12258
    输出: 5
    解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

    """
    def translateNum(self, num: int) -> int:
        # dp
        num = str(num)
        n = len(num)
        dp = [1]*(n+1)
        for i in range(2, n+1):
            if num[i-2] =='1' or (num[i-2]=='2' and num[i-1]<='5'):
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]



