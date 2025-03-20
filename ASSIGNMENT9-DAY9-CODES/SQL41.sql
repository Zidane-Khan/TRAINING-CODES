-- Create an index on the "order_date" column of the "orders"
--  table to improve query performance for date-based searches.

select * from orders;
alter table orders add column order_date DATE;
CREATE INDEX order_index
ON orders (order_date);