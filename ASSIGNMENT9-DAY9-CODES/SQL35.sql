-- Add a foreign key constraint to enforce referential integrity between the "orders" table and the "customers" table.

CREATE TABLE customers_integrity (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE orders_integrity (
    order_id INT PRIMARY KEY ,
    customer_id INT,
    order_date DATETIME,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers_integrity(customer_id)

);
