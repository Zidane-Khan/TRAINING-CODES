-- Write a SQL query to group rows in a table named "sales" by the "product_id" column and 
-- calculate the sum of the "quantity" column.

select * from inventory;
select sum(quantity), pro_name from inventory group by pro_name;
-- SELECT COUNT(CustomerID), Country
-- FROM Customers
-- GROUP BY Country;
select sum(quantity) from inventory;

