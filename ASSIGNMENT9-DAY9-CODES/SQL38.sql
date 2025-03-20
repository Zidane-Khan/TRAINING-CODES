-- ALTER TABLE orders
-- ADD CONSTRAINT fk_order_items_products
-- FOREIGN KEY (pro_id) REFERENCES products(pro_id);
-- Write an SQL query to find all orders placed on a specific date, sorted by the total order amount.
-- Create the customers table
CREATE TABLE customerss_date (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100) 
);


CREATE TABLE ordersss_date (
    order_id INT PRIMARY KEY,
    order_date DATETIME,
    total_amount INT);
    
    
-- Insert sample customers
INSERT INTO customerss_date values (1, 'John Doe', 'john@example.com'), (2, 'Jane Smith', 'jane@example.com');

INSERT INTO ordersss_date  VALUES
(1, '2025-03-16 08:30:00', 20000),
(2, '2025-03-16 09:45:00', 15000),
(3, '2025-03-16 11:00:00', 25000),
(4, '2025-03-17 10:00:00', 30000);


SELECT order_id, order_date, total_amount
FROM ordersss_date
WHERE DATE(order_date) = '2025-03-16'  -- Specify the desired date here
ORDER BY total_amount DESC;  -- Sort by total amount in descending order

