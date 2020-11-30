#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (40.46%)
# Likes:    2978
# Dislikes: 155
# Total Accepted:    334.5K
# Total Submissions: 800.1K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take labelled from 0 to n - 1.
# 
# Some courses may have prerequisites, for example, if prerequisites[i] = [ai,
# bi] this means you must take the course bi before the course ai.
# 
# Given the total number of courses numCourses and a list of the prerequisite
# pairs, return the ordering of courses you should take to finish all courses.
# 
# If there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
# 
# 
# Example 3:
# 
# 
# Input: numCourses = 1, prerequisites = []
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
# 
# 
#

# @lc code=start

class Solution:

    # topologically sort
    #def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #  by degree

        # adj_list = defaultdict(list)
        # indegree = defaultdict(int)
        # for desc, src in prerequisites:
        #     adj_list[src].append(desc)
        #     indegree[desc]+=1
        # zero_degreee_queue = deque([k for k in range(numCourses) if indegree[k]==0])

        # topologically_sorted_order = []

        # while zero_degreee_queue:
        #     vertex = zero_degreee_queue.popleft()
        #     topologically_sorted_order.append(vertex)

        #     if vertex in adj_list:
        #         for neighbor in adj_list[vertex]:
        #             indegree[neighbor]-=1

        #             if indegree[neighbor]==0:
        #                 zero_degreee_queue.append(neighbor)
        # return topologically_sorted_order if len(topologically_sorted_order)==numCourses else []


    
    # by dfs
    WHITE = 1
    GRAY = 2 
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)

        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        color = {k: Solution.WHITE for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return  
            color[node] = Solution.GRAY

            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False
                        
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []

            



        
# @lc code=end

