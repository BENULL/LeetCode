#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#
# https://leetcode-cn.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (72.73%)
# Likes:    331
# Dislikes: 0
# Total Accepted:    44.9K
# Total Submissions: 61.7K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# 给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。
# 
# 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。
# 
# 
# 
# 示例 1:
# 
# 输入: [[1,1],2,[1,1]]
# 输出: [1,1,2,1,1]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
# 
# 示例 2:
# 
# 输入: [1,[4,[6]]]
# 输出: [1,4,6]
# 解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
# 
# 
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# def flatten(nestedList: [NestedInteger]):
#     for x in nestedList:
#         if x.isInteger():
#             yield x.getInteger()
#         else:
#             yield from flatten(x.getList())

# class NestedIterator:
#     def __init__(self, nestedList: [NestedInteger]):
#         # self.iterator = iter(nestedList)
#         self._hasNext = True

#         # flatten
#         self.iterator = flatten(nestedList)

#     def next(self) -> int: 
#         return self.theNext

#     def hasNext(self) -> bool:
#         if self._hasNext:
#             try: 
#                 self.theNext = next(self.iterator)
#             except StopIteration: 
#                 self._hasNext = False
#         return self._hasNext


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = []
        def dfs(nestedList):
            for item in nestedList:
                if item.isInteger() == True:
                    self.queue.append(item.getInteger())
                else:
                    dfs(item.getList())
        dfs(nestedList)
    
    def next(self) -> int:
        if self.hasNext() == True:
            return self.queue.pop(0)
        else:
            return -1
    
    def hasNext(self) -> bool:
        if not self.queue:
            return False
        else:
            return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

