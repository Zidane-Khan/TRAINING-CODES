# Write an SQL query to find all products that are out of stock.

create table schee_productss (pro_id int, pro_name varchar(10),availability varchar(20));
insert into schee_productss values (1,'Maggi','IN-STOCK'),(2,'Colgate','OUT-OF-STOCK'),(3,'Tissue','IN-STOCK'),
(4,'LAPtop','OUT-OF-STOCK'),(5,'Watch','IN-STOCK'),(6,'Pen','IN-STOCK');

select pro_name from  schee_productss where availability='OUT-OF-STOCK';

-- Implement a transaction in SQL to update inventory q
-- uantities and generate a purchase order for low-stock items.

-- Create the inventory table to track stock quantities
CREATE TABLE schee_inventory (
    pro_id INT PRIMARY KEY,
    pro_name VARCHAR(100),
    quantity INT
);

-- Create the purchase orders table to track purchase orders
CREATE TABLE purchase_orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    pro_id INT,
    order_quantity INT,
    order_date DATETIME,
    FOREIGN KEY (pro_id) REFERENCES schee_inventory(pro_id)
);

-- Insert sample data into the schee_inventory table
INSERT INTO schee_inventory (pro_id, pro_name, quantity) 
VALUES
(1, 'Maggi', 15),      -- Stock 15 units
(2, 'Colgate', 0),     -- Stock 0 units (Out of Stock)
(3, 'Tissue', 10),     -- Stock 10 units
(4, 'Laptop', 1),      -- Stock 1 unit (Low Stock)
(5, 'Watch', 8),       -- Stock 8 units
(6, 'Pen', 3);         -- Stock 3 units (Low Stock)


START TRANSACTION;

-- Step 1: Find products with low stock (less than 5 units)
SELECT pro_id, pro_name, quantity
FROM schee_inventory
WHERE quantity < 5;

-- Step 2: Update the inventory for low-stock items (add 10 units to each)
UPDATE schee_inventory
SET quantity = quantity + 10
WHERE quantity < 5;

-- Step 3: Generate a purchase order for each low-stock product (ordering 10 units)
INSERT INTO purchase_orders (pro_id, order_quantity, order_date)
SELECT pro_id, 10, NOW()
FROM schee_inventory
WHERE quantity < 5;

-- Step 4: Commit the transaction if everything is successful
COMMIT;


