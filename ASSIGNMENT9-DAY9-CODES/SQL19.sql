-- Write a SQL query to join three tables named "customers", "orders", and "products" 
-- on their respective foreign key columns.

CREATE TABLE customers_joins(
    customer_id INT PRIMARY KEY,
    name VARCHAR(100));
CREATE TABLE products_joins(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price INT
);
CREATE TABLE orders_join (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers_joins(customer_id)
);
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders_join(order_id),
    FOREIGN KEY (product_id) REFERENCES products_joins(product_id)
);
