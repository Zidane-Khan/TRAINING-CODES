-- Crea-- te an index on multiple columns (e.g., "last_name" and "city") 
-- of the "customers" table to improve performance for complex queries involving those columns.

CREATE INDEX index_customers
ON customers (Name, city);
select * from customers;

-- Create an index on the "last_name" column of the "customers" table to improve search performance.
CREATE INDEX index_customers
ON customer00 (name);
select * from customer00;