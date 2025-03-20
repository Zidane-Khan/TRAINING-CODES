# Insert multiple rows into an inventory table and ensure all inserts are committed only if all succeed.

CREATE TABLE Inventory (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(10),
    Quantity INT,
    Price INt
);
DELIMITER //

-- CREATE PROCEDURE InsertMultipleProducts()
-- BEGIN
    -- Start the transaction
    START TRANSACTION;

    -- Insert multiple products into the Inventory table
    INSERT INTO Inventory (ProductID, ProductName, Quantity, Price)
    VALUES (1, 'Lapto', 10, 1000);

    INSERT INTO Inventory (ProductID, ProductName, Quantity, Price)
    VALUES (2, 'Colgate', 12, 1200);

    INSERT INTO Inventory (ProductID, ProductName, Quantity, Price)
    VALUES (3, 'Tisause', 15, 1500);

    -- If all insert statements succeed, commit the transaction
    COMMIT;

-- EXCEPTION
--     -- If any error occurs, rollback the transaction
--     WHEN OTHERS THEN
--         ROLLBACK;
--         -- Optionally, log the error or raise an error message
--         SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'An error occurred, transaction rolled back';

-- END //

-- DELIMITER ;
