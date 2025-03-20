-- Write a SQL query to update the "status" column of a table
--  named "orders" to 'completed' where the "order_date" is before a specific date.


update orderss_month set order_date = "completed "
where order_date < '2020-10-2'