-- Write a SQL query to calculate the total count of rows 
-- in a table named "orders" grouped by the "customer_id" column.

select * from orders;

select count(*) as total_count_rows from orders group by id ;
