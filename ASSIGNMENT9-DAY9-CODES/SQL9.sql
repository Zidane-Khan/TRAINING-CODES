-- Write a SQL query to create a foreign key constraint between  two tables
-- two tables named "orders" and "customers" using the "customer_id" column.orders\

CREATE TABLE customers_constrainit (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100)
);
CREATE TABLE orders_constraint (
    order_id INT PRIMARY KEY,
    order_amount INT,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers_constrainit(customer_id)
);
