#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
# https://leetcode-cn.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (53.40%)
# Likes:    82
# Dislikes: 0
# Total Accepted:    14.6K
# Total Submissions: 27.3K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
# 
# 假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
# 
# 例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
# 
# 与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
# 
# 现在给定3个参数 — start, end,
# bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。
# 
# 注意：
# 
# 
# 起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
# 如果一个起始基因序列需要多次变化，那么它每一次变化之后的基因序列都必须是合法的。
# 假定起始基因序列与目标基因序列是不一样的。
# 
# 
# 
# 
# 示例 1：
# 
# 
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# 返回值: 1
# 
# 
# 示例 2：
# 
# 
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# 返回值: 2
# 
# 
# 示例 3：
# 
# 
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# 返回值: 3
# 
# 
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 最短路径 -> 单向bfs
        # bank = set(bank)
        # if end not in bank: return -1
        # change = ['A', 'G', 'C', 'T']
        # queue = [[start, 0]]
        # while queue:
        #     dna, times = queue.pop(0)
        #     if dna==end: return times
        #     for i, c in itertools.product(range(8),change):
        #         word = dna[:i]+c+dna[i+1:]
        #         if word in bank:
        #             queue.append([word,times+1])
        #             bank.discard(word)       
        # return -1

        # 双向bfs
        bank = set(bank)
        if end not in bank: return -1
        change = ['A', 'G', 'C', 'T']
        times = 0
        head = [start]
        tail = [end]
        while head and tail:
            times += 1
            if len(head)<len(tail):
                head, tail = tail, head
            tmp = []
            for dna in head:
                for i, c in itertools.product(range(8),change):
                    word = dna[:i]+c+dna[i+1:]
                    if word in tail: return times
                    if word in bank:
                        tmp.append(word)
                        bank.discard(word)  
            head = tmp     
        return -1



        

# @lc code=end

