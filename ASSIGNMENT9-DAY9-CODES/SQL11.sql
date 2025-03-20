-- Write a SQL query to select all columns from 
-- two tables named "users" and "orders" and join them on the "user_id" column

select* from users;
select * from orders;
ALTER TABLE orders
RENAME COLUMN id to de;

select * from users inner join orders on users.id=orders.id;
