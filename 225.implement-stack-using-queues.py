#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (44.84%)
# Likes:    984
# Dislikes: 670
# Total Accepted:    213.6K
# Total Submissions: 448.3K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a last in first out (LIFO) stack using only two queues. The
# implemented stack should support all the functions of a normal queue (push,
# top, pop, and empty).
# 
# Implement the MyStack class:
# 
# 
# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# 
# 
# Notes:
# 
# 
# You must use only standard operations of a queue, which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may
# simulate a queue using a list or deque (double-ended queue), as long as you
# use only a queue's standard operations.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
# 
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
# 
# 
# 
# Constraints:
# 
# 
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
# 
# 
# 
# Follow-up: Can you implement the stack such that each operation is amortized
# O(1) time complexity? In other words, performing n operations will take
# overall O(n) time even if one of those operations may take longer. You can
# use more than two queues.
# 
#

# @lc code=start
class MyStack:

    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.q1 = []
    #     self.q2 = []    

    # def push(self, x: int) -> None:
    #     """
    #     Push element x onto stack.
    #     """
    #     q = self.q1 or self.q2
    #     q.append(x)

    # def pop(self) -> int:
    #     """
    #     Removes the element on top of the stack and returns that element.
    #     """
    #     eq = self.q1 and self.q2
    #     hq = self.q1 or self.q2
    #     while len(hq)>1:
    #         eq.append(hq.pop(0))
    #     return hq.pop(0)

    # def top(self) -> int:
    #     """
    #     Get the top element.
    #     """
    #     # if not self.empty():
    #     eq = self.q1 and self.q2
    #     hq = self.q1 or self.q2
    #     while len(hq)>1:
    #         eq.append(hq.pop(0))
    #     res = hq[0]
    #     eq.append(hq.pop(0))
    #     return res
        

    # def empty(self) -> bool:
    #     """
    #     Returns whether the stack is empty.
    #     """
    #     return not self.q1 and not self.q2

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.topval = 0
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        self.topval = x
        
        
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) > 1:
            self.topval = self.queue1.pop(0)
            self.queue2.append(self.topval)
        
        ele = self.queue1.pop(0)
        self.queue1 = self.queue2
        self.queue2 = []
        return ele
        
        

    def top(self) -> int:
        return self.topval
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if len(self.queue1) == 0 else False
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

