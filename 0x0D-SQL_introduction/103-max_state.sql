-- This is a script that displays the max temperature of each state (ordered by State name) by importing table_dump.sql in hbtn_0c_0 database
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
