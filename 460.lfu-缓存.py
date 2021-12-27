#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#
# https://leetcode-cn.com/problems/lfu-cache/description/
#
# algorithms
# Hard (43.45%)
# Likes:    469
# Dislikes: 0
# Total Accepted:    36.9K
# Total Submissions: 85K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
# 
# 实现 LFUCache 类：
# 
# 
# LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
# int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。
# void put(int key, int value) -
# 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除
# 最近最久未使用 的键。
# 
# 
# 注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。
# 
# 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
# 
# 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put
# 操作，使用计数器的值将会递增。
# 
# 
# 
# 示例：
# 
# 
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# 解释：
# // cnt(x) = 键 x 的使用计数
# // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
# LFUCache lFUCache = new LFUCache(2);
# lFUCache.put(1, 1);   // cache=[1,_], cnt(1)=1
# lFUCache.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lFUCache.get(1);      // 返回 1
# ⁠                     // cache=[1,2], cnt(2)=1, cnt(1)=2
# lFUCache.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
# ⁠                     // cache=[3,1], cnt(3)=1, cnt(1)=2
# lFUCache.get(2);      // 返回 -1（未找到）
# lFUCache.get(3);      // 返回 3
# ⁠                     // cache=[3,1], cnt(3)=2, cnt(1)=2
# lFUCache.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
# ⁠                     // cache=[4,3], cnt(4)=1, cnt(3)=2
# lFUCache.get(1);      // 返回 -1（未找到）
# lFUCache.get(3);      // 返回 3
# ⁠                     // cache=[3,4], cnt(4)=1, cnt(3)=3
# lFUCache.get(4);      // 返回 4
# ⁠                     // cache=[3,4], cnt(4)=2, cnt(3)=3
# 
# 
# 
# 提示：
# 
# 
# 0 
# 最多调用 10^5 次 get 和 put 方法
# 
# 
# 
# 
# 进阶：你可以为这两种操作设计时间复杂度为 O(1) 的实现吗？
# 
#

# @lc code=start

class Node:
  def __init__(self, key, val, pre=None, nex=None, freq=0):
    self.pre = pre
    self.nex = nex
    self.freq = freq
    self.val = val
    self.key = key
      
  def insert(self, nex):
    nex.pre = self
    nex.nex = self.nex
    self.nex.pre = nex
    self.nex = nex
  
def create_linked_list():
  head = Node(0, 0)
  tail = Node(0, 0)
  head.nex = tail
  tail.pre = head
  return (head, tail)


class LFUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.size = 0
    self.minFreq = 0
    self.freqMap = collections.defaultdict(create_linked_list)
    self.keyMap = {}

  def delete(self, node):
      if node.pre:
          node.pre.nex = node.nex
          node.nex.pre = node.pre
          if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][-1]:
              self.freqMap.pop(node.freq)
      return node.key

  
  def increase(self, node):
    node.freq += 1
    self.delete(node)
    self.freqMap[node.freq][-1].pre.insert(node)
    if node.freq == 1:
        self.minFreq = 1
    elif self.minFreq == node.freq - 1:
        head, tail = self.freqMap[node.freq - 1]
        if head.nex is tail:
            self.minFreq = node.freq
    
  def get(self, key: int) -> int:
    if key in self.keyMap:
          self.increase(self.keyMap[key])
          return self.keyMap[key].val
    return -1


  def put(self, key: int, value: int) -> None:
    if self.capacity != 0:
      if key in self.keyMap:
          node = self.keyMap[key]
          node.val = value
      else:
          node = Node(key, value)
          self.keyMap[key] = node
          self.size += 1
      if self.size > self.capacity:
          self.size -= 1
          deleted = self.delete(self.freqMap[self.minFreq][0].nex)
          self.keyMap.pop(deleted)
      self.increase(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

