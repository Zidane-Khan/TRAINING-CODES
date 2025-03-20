-- Create a transaction where a product 
-- is added to inventory, and a corresponding supplier payment is recorded. Use ROLLBACK if any issue occurs.


CREATE TABLE Productss (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(10),
    price INT
);

CREATE TABLE Inventory_products (
    inventory_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);


CREATE TABLE Suppliers (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(10)
);


CREATE TABLE SupplierrPayments (
    payment_id INT PRIMARY KEY,
    supplier_id INT,
    payment_amount INT,
    FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
);

DELIMITER $$

CREATE PROCEDURE AddPayment()
BEGIN
    -- Declare a handler to catch errors
    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
        ROLLBACK;

    -- Start the transaction
    START TRANSACTION;

    -- Insert product into Products table
    INSERT INTO Products (product_id, product_name, price)
    VALUES (1, 'Colgate', 1000);

    -- Insert inventory details into Inventory table
    INSERT INTO Inventory (inventory_id, product_id, quantity)
    VALUES (1, 1, 12);

    -- Record payment to supplier in SupplierrPayments table
    INSERT INTO SupplierrPayments (payment_id, supplier_id, payment_amount, payment_date)
    VALUES (1, 1, 5000, CURRENT_DATE);

    -- If no errors, commit the transaction
    COMMIT;
END $$

DELIMITER ;
