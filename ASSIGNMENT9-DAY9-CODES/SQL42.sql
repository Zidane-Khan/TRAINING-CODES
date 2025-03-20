-- Write an SQL query to calculate the total revenue generated for each product category.
select * from inventory;
alter table inventory add column order_id int;
select * from orders_schema;
select  sum(orders_schema.amount* inventory.quantity) from orders_schema inner join inventory on inventory.order_id=orders_schema.order_id;