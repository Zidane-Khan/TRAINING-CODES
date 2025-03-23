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

SELECT 
    customers_joins.name AS customer_name,
    orders_join.order_id,
    orders_join.order_date,
    products_joins.product_name,
    order_items.quantity,
    products_joins.price,
    (order_items.quantity * products_joins.price) AS total_price
FROM 
    customers_joins
INNER JOIN 
    orders_join ON customers_joins.customer_id = orders_join.customer_id
INNER JOIN 
    order_items ON orders_join.order_id = order_items.order_id
INNER JOIN 
    products_joins ON order_items.product_id = products_joins.product_id;
