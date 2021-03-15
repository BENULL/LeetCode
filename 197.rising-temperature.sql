--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--
-- https://leetcode.com/problems/rising-temperature/description/
--
-- database
-- Easy (38.29%)
-- Likes:    493
-- Dislikes: 253
-- Total Accepted:    147.1K
-- Total Submissions: 367.7K
-- Testcase Example:  '{"headers": {"Weather": ["Id", "RecordDate", "Temperature"]}, "rows": {"Weather": [[1, "2015-01-01", 10], [2, "2015-01-02", 25], [3, "2015-01-03", 20], [4, "2015-01-04", 30]]}}'
--
-- Table: Weather
-- 
-- 
-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | recordDate    | date    |
-- | temperature   | int     |
-- +---------------+---------+
-- id is the primary key for this table.
-- This table contains information about the temperature in a certain day.
-- 
-- 
-- 
-- 
-- Write an SQL query to find all dates' id with higher temperature compared to
-- its previous dates (yesterday).
-- 
-- Return the result table in any order.
-- 
-- The query result format is in the following example:
-- 
-- 
-- Weather
-- +----+------------+-------------+
-- | id | recordDate | Temperature |
-- +----+------------+-------------+
-- | 1  | 2015-01-01 | 10          |
-- | 2  | 2015-01-02 | 25          |
-- | 3  | 2015-01-03 | 20          |
-- | 4  | 2015-01-04 | 30          |
-- +----+------------+-------------+
-- 
-- Result table:
-- +----+
-- | id |
-- +----+
-- | 2  |
-- | 4  |
-- +----+
-- In 2015-01-02, temperature was higher than the previous day (10 -> 25).
-- In 2015-01-04, temperature was higher than the previous day (20 -> 30).
-- 
-- 
--

-- @lc code=start
# Write your MySQL query statement below

SELECT t1.Id
FROM Weather t1,Weather t2 
WHERE TO_DAYS(t1.recordDate) = TO_DAYS(t2.recordDate) + 1 and t1.temperature > t2.temperature
-- @lc code=end

