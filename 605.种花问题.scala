/*
 * @lc app=leetcode.cn id=605 lang=scala
 *
 * [605] 种花问题
 *
 * https://leetcode-cn.com/problems/can-place-flowers/description/
 *
 * algorithms
 * Easy (33.46%)
 * Likes:    383
 * Dislikes: 0
 * Total Accepted:    106.6K
 * Total Submissions: 318.5K
 * Testcase Example:  '[1,0,0,0,1]\n1'
 *
 * 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
 * 
 * 给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n
 * ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。
 * 
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：flowerbed = [1,0,0,0,1], n = 1
 * 输出：true
 * 
 * 
 * 示例 2：
 * 
 * 
 * 输入：flowerbed = [1,0,0,0,1], n = 2
 * 输出：false
 * 
 * 
 * 
 * 
 * 提示：
 * 
 * 
 * 1 
 * flowerbed[i] 为 0 或 1
 * flowerbed 中不存在相邻的两朵花
 * 0 
 * 
 * 
 */

// @lc code=start
object Solution {
    def canPlaceFlowers(flowerbed: Array[Int], n: Int): Boolean = {
        // greedy
        // var res = n 
        // for(i <- 0 until flowerbed.length if flowerbed(i)==0){
        //     if ((i==0 || flowerbed(i-1)==0) && (i==flowerbed.length-1 || flowerbed(i+1)==0)){
        //         res -= 1
        //         flowerbed(i) = 1
        //     }   
        // }
        // res<=0
        var i = 0 
        var res = n
        while(i < flowerbed.length && res > 0){
            if (flowerbed(i) == 1) {
                i += 2
            }else if(i == flowerbed.length - 1 || flowerbed(i + 1) == 0){
                res -= 1
                i += 2
            }else{
                i += 3
            }
        }
        res <=0 
    }
}
// @lc code=end

