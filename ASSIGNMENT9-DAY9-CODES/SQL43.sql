-- Add a foreign key constraint to enforce referential integrity 
-- between the "order_items" table and the "products" table.

select * from inventory;
select * from orders_schema;
ALTER TABLE inventory
ADD CONSTRAINT fk_order_id
FOREIGN KEY (order_id)
REFERENCES orders_schema(order_id)