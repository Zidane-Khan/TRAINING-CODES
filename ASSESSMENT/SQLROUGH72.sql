DELIMITER $$

CREATE PROCEDURE AddProductAndPayment(
    IN p_product_name VARCHAR(100),
    IN p_quantity INT,
    IN p_price DECIMAL(10,2),
    IN p_supplier_id INT,
    IN p_payment_amount DECIMAL(10,2)
)
BEGIN
    DECLARE product_id INT;
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        -- Rollback if an error occurs
        ROLLBACK;
        SELECT 'Transaction rolled back due to an error' AS status;
    END;

    -- Start the transaction
    START TRANSACTION;

    -- Insert new product into Inventory
    INSERT INTO Inventory (product_name, quantity, price)
    VALUES (p_product_name, p_quantity, p_price);

    -- Get the last inserted product_id
    SET product_id = LAST_INSERT_ID();

    -- Insert payment record for the supplier
    INSERT INTO SupplierPayments (product_id, supplier_id, amount)
    VALUES (product_id, p_supplier_id, p_payment_amount);

    -- Commit if everything is successful
    COMMIT;
    SELECT 'Transaction committed successfully' AS status;
END $$

DELIMITER ;
