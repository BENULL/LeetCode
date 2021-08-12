#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#
# https://leetcode-cn.com/problems/string-compression/description/
#
# algorithms
# Medium (42.66%)
# Likes:    196
# Dislikes: 0
# Total Accepted:    31.5K
# Total Submissions: 73.7K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# 给定一组字符，使用原地算法将其压缩。
# 
# 压缩后的长度必须始终小于或等于原数组长度。
# 
# 数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
# 
# 在完成原地修改输入数组后，返回数组的新长度。
# 
# 
# 
# 进阶：
# 你能否仅使用O(1) 空间解决问题？
# 
# 
# 
# 示例 1：
# 
# 输入：
# ["a","a","b","b","c","c","c"]
# 
# 输出：
# 返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
# 
# 说明：
# "aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
# 
# 
# 示例 2：
# 
# 输入：
# ["a"]
# 
# 输出：
# 返回 1 ，输入数组的前 1 个字符应该是：["a"]
# 
# 解释：
# 没有任何字符串被替代。
# 
# 
# 示例 3：
# 
# 输入：
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 
# 输出：
# 返回 4 ，输入数组的前4个字符应该是：["a","b","1","2"]。
# 
# 解释：
# 由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
# 注意每个数字在数组中都有它自己的位置。
# 
# 
# 
# 
# 提示：
# 
# 
# 所有字符都有一个ASCII值在[35, 126]区间内。
# 1 <= len(chars) <= 1000。
# 
# 
#

# @lc code=start
class Solution:
    def compress(self, chars) -> int:
        # brute force pass
        # res = ''
        # cnt = 0
        # prev = 34
        # for c in chars:
        #     if ord(c)!=prev:
        #         if cnt>1:
        #             res = res + str(cnt) + c
        #             cnt = 1
        #         else:
        #             res = res + c
        #             cnt = 1
        #         prev = ord(c)
        #     else:
        #         cnt+=1

        # if cnt>1:
        #     res+=str(cnt)
                
        # for i in range(len(res)):
        #     chars[i]=res[i]
        # return len(res)

        # 三指针
        write, anchor = 0, 0
        for read, c in enumerate(chars):
            if read+1==len(chars) or  c!=chars[read+1]:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write







if __name__=='__main__':
    s = Solution()
    print(s.compress(["a","a","b","b","c","c","c"]))

# @lc code=end

