-- Write a transaction to delete a customer 
-- and their related orders, ensuring data integrity is maintained.
select * from customers;
select * from orders;

-- Start a transaction
START TRANSACTION;

-- Delete the related orders for the customer
DELETE FROM orders WHERE customer_id = 1;

-- Delete the customer
DELETE FROM customers WHERE customer_id = 1;

-- Commit the transaction to ensure changes are persistent
COMMIT;

select * from  customers;

