-- 40.	Implement a transaction in SQL to transfer inventory from one 
-- warehouse to another, ensuring data consistency and integrity.


START TRANSACTION;

SELECT quantity 
INTO @inventory_stock 
FROM inventory 
WHERE  product_id = 456;

-- 2. Deduct the stock from the source warehouse (warehouse_id = 1)
UPDATE inventory 
SET quantity = quantity - @inventory_stock 
WHERE   product_id = 456;

-- 3. Add the stock to the destination warehouse (warehouse_id = 2)
UPDATE inventory 
SET quantity = quantity + @inventory_stock 
WHERE  product_id = 456;

-- 4. Commit the transaction to ensure changes are saved
COMMIT;
