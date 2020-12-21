/*
 * @lc app=leetcode id=208 lang=scala
 *
 * [208] Implement Trie (Prefix Tree)
 *
 * https://leetcode.com/problems/implement-trie-prefix-tree/description/
 *
 * algorithms
 * Medium (48.82%)
 * Likes:    4006
 * Dislikes: 62
 * Total Accepted:    373.3K
 * Total Submissions: 729K
 * Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
 *
 * Implement a trie with insert, search, and startsWith methods.
 * 
 * Example:
 * 
 * 
 * Trie trie = new Trie();
 * 
 * trie.insert("apple");
 * trie.search("apple");   // returns true
 * trie.search("app");     // returns false
 * trie.startsWith("app"); // returns true
 * trie.insert("app");   
 * trie.search("app");     // returns true
 * 
 * 
 * Note:
 * 
 * 
 * You may assume that all inputs are consist of lowercase letters a-z.
 * All inputs are guaranteed to be non-empty strings.
 * 
 * 
 */

// @lc code=start
class Trie() {

    /** Initialize your data structure here. */

    case class STrie(term:Boolean,m:Map[Char,STrie])

    var tree = STrie(false,Map())

    private def insert(word: List[Char], t:STrie):STrie = word match {
        case Nil => STrie(true,t.m)
        case x :: xs =>  t.m.get(x) match {
            case None => STrie(t.term,t.m + (x->insert(xs,STrie(false,Map()))))
            case Some(sub) => STrie(t.term,t.m + (x -> insert(xs,sub)))
        }
    }

    @scala.annotation.tailrec
    private def search(word:List[Char],t:STrie):Boolean = word match {
        case Nil => t.term
        case x::xs => t.m.get(x) match {
            case None => false
            case Some(sub) => search(xs,sub)
        }
    }

    @scala.annotation.tailrec
    private def startWith(word: List[Char], t: STrie): Boolean = word match {
        case Nil => true
        case x :: xs => t.m.get(x) match {
            case None => false
            case Some(sub) => startWith(xs, sub)
        }
    }

    /** Inserts a word into the trie. */
    def insert(word: String) {
        val newTree = insert(word.toList,tree)
        tree = newTree
    }

    /** Returns if the word is in the trie. */
    def search(word: String): Boolean = {
        search(word.toList,tree)
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    def startsWith(prefix: String): Boolean = {
        startWith(prefix.toList,tree)
    }

}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
// @lc code=end

