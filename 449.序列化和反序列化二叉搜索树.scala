/*
 * @lc app=leetcode.cn id=449 lang=scala
 *
 * [449] 序列化和反序列化二叉搜索树
 *
 * https://leetcode-cn.com/problems/serialize-and-deserialize-bst/description/
 *
 * algorithms
 * Medium (55.51%)
 * Likes:    193
 * Dislikes: 0
 * Total Accepted:    13.6K
 * Total Submissions: 24.5K
 * Testcase Example:  '[2,1,3]'
 *
 * 序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。
 * 
 * 设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。
 * 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。
 * 
 * 编码的字符串应尽可能紧凑。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：root = [2,1,3]
 * 输出：[2,1,3]
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：root = []
 * 输出：[]
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 树中节点数范围是 [0, 10^4]
 * 0 
 * 题目数据 保证 输入的树是一棵二叉搜索树。
 * 
 * 
 * 
 * 
 * 注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode(var _value: Int) {
 *   var value: Int = _value
 *   var left: TreeNode = null
 *   var right: TreeNode = null
 * }
 */

class Codec {
    // Encodes a list of strings to a single string.
    def serialize(root: TreeNode): String = {
        def preorderTraversal(root: TreeNode):List[Int]={
            Option(root) match {
                case Some(node) => List(node.value) ++ preorderTraversal(node.left) ++ preorderTraversal(node.right)
                case _ => List()
            }
        }
        val pre_res = preorderTraversal(root)
        pre_res.mkString(",")
    }
    
    // Decodes a single string to a list of strings.
    def deserialize(data: String): TreeNode = {
        if (data.length() == 0) return null
        val preorder = data.split(",").map(_.toInt)
        val inorder = preorder.sorted
        var index = 0
        def buildTreeNode(from:Int,to:Int) : TreeNode = {
            if (from>to) return null
            val value = preorder(index)
            index += 1
            val inorderIndex =inorder.indexOf(value,from)
            val left = buildTreeNode(from,inorderIndex-1)
            val right = buildTreeNode(inorderIndex+1,to)
            new TreeNode(value,left,right)
        }
        buildTreeNode(0, inorder.length-1)
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * val ser = new Codec()
 * val deser = new Codec()
 * val tree: String = ser.serialize(root)
 * val ans = deser.deserialize(tree)
 * return ans
 */
// @lc code=end

