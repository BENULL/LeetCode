#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (42.91%)
# Likes:    4299
# Dislikes: 185
# Total Accepted:    454.9K
# Total Submissions: 1.1M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input
# prerequisites.
# 1 <= numCourses <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    # build graph and detect ring
    # Topological sort

    def buildGraph(self,numCourses,prerequisites):
        adjList = [[] for _ in range(numCourses)]
        for c1, c2 in prerequisites:
            adjList[c2].append(c1)
        return adjList

    def topoBFS(self,numCourses,prerequisites):
        adjList = self.buildGraph(numCourses, prerequisites)
        inDegrees = [0] * numCourses
        for v1, _ in prerequisites:
            inDegrees[v1] += 1
        
        queue = []
        topoOrder = []
        count = 0
        for v in range(numCourses):
            if inDegrees[v] == 0:
                queue.append(v)

        while queue:
            v = queue.pop(0)
            topoOrder.append(v)
            count += 1
            for des in adjList[v]:
                inDegrees[des] -= 1
                if inDegrees[des] == 0:
                    queue.append(des)
        if count != numCourses:
            return None  # graph has at least one cycle
        else:
            return topoOrder




    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return True if self.topoBFS(numCourses, prerequisites) else False
        
        
        
# @lc code=end

