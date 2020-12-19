/*
 * @lc app=leetcode id=289 lang=scala
 *
 * [289] Game of Life
 *
 * https://leetcode.com/problems/game-of-life/description/
 *
 * algorithms
 * Medium (54.13%)
 * Likes:    2193
 * Dislikes: 310
 * Total Accepted:    204.5K
 * Total Submissions: 363.2K
 * Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
 *
 * According to the Wikipedia's article: "The Game of Life, also known simply
 * as Life, is a cellular automaton devised by the British mathematician John
 * Horton Conway in 1970."
 * 
 * Given a board with m by n cells, each cell has an initial state live (1) or
 * dead (0). Each cell interacts with its eight neighbors (horizontal,
 * vertical, diagonal) using the following four rules (taken from the above
 * Wikipedia article):
 * 
 * 
 * Any live cell with fewer than two live neighbors dies, as if caused by
 * under-population.
 * Any live cell with two or three live neighbors lives on to the next
 * generation.
 * Any live cell with more than three live neighbors dies, as if by
 * over-population..
 * Any dead cell with exactly three live neighbors becomes a live cell, as if
 * by reproduction.
 * 
 * 
 * Write a function to compute the next state (after one update) of the board
 * given its current state. The next state is created by applying the above
 * rules simultaneously to every cell in the current state, where births and
 * deaths occur simultaneously.
 * 
 * Example:
 * 
 * 
 * Input: 
 * [
 * [0,1,0],
 * [0,0,1],
 * [1,1,1],
 * [0,0,0]
 * ]
 * Output: 
 * [
 * [0,0,0],
 * [1,0,1],
 * [0,1,1],
 * [0,1,0]
 * ]
 * 
 * 
 * Follow up:
 * 
 * 
 * Could you solve it in-place? Remember that the board needs to be updated at
 * the same time: You cannot update some cells first and then use their updated
 * values to update other cells.
 * In this question, we represent the board using a 2D array. In principle, the
 * board is infinite, which would cause problems when the active area
 * encroaches the border of the array. How would you address these problems?
 * 
 * 
 */

// @lc code=start
object Solution {
    //not in-place
    def gameOfLife(board: Array[Array[Int]]): Unit = {
        def numberOfNeighbors(row:Int,column:Int):Int = {
            def isNeighboard(row: Int, column: Int): Boolean = {
                row >= 0 && row < board.length && column >= 0 && column < board(row).length && board(row)(column) == 1
            }
            (for {
                vertical <- Seq(-1,0,1)
                horizontal <- Seq(-1,0,1)
                if vertical!=0 || horizontal!=0
                if isNeighboard(row+vertical,column+horizontal)
            } yield () ).length

        }

        val nextState : Array[Array[Int]]  = Array.ofDim[Int](board.length,board(0).length)
        for {
            row <- board.indices
            column <- board(row).indices
        }{
            nextState(row)(column) =  (board(row)(column), numberOfNeighbors(row,column)) match {
                case (_,neighbors) if neighbors<2 => 0 
                case (1,neighbors) if neighbors==2 || neighbors==3 => 1
                case (1,neighbors) if neighbors>3 => 0 
                case (0,3) => 1
                case _ => 0 
            }
        }

        for {
            row <- board.indices
            column <- board(row).indices
        }{
            board(row)(column) =  nextState(row)(column)
        }

        
    }
}
// @lc code=end

