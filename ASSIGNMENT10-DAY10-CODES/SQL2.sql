-- Implement a transaction to insert a new order into an Orders
--  table and update the corresponding customer's total purchase amount.

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique customer identifier
    name VARCHAR(20),                           -- Customer's name                         -- Customer's email
    purchase_amount int -- Total amount of purchases made by the customer
);
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,    
    customer_id INT,                           
    order_amount INT,             
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)  -- Foreign key to Customers table
);

select * from orders;

INSERT INTO Customers VALUES (5,'Zidan',3000);

INSERT INTO Orders VALUES  (1,1,2000);




-- Begin the transaction
START TRANSACTION;

-- Insert the new order into the Orders table
INSERT INTO Orders (order_id, customer_id, order_amount)
VALUES (2, 5, 25000);

-- Update the corresponding customer's total purchase amount
UPDATE Customers
SET purchase_amount = purchase_amount + 25000
WHERE customer_id = 5;

-- If everything is fine, commit the transaction
COMMIT;

select * from orders;
