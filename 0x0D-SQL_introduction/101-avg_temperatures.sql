-- This is a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending) by importing table_dump.sql table in hbtn_0c_0 database
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
