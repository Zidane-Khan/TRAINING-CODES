-- Write a SQL query to delete all rows from a table named
--  "products" where the "category" column is 'clothing' or 'accessories'.

select * from products;
delete from products where category='Grocery' or category='Dairy';
