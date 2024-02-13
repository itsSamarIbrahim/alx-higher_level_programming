-- This is a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending) by importing dump_table_2.sql in hbtn_0c_0 database
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
