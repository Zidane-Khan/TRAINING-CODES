-- Simulate a failed transaction by updating two related tables but introducing an intentional error. 
-- Use ROLLBACK to undo changes.
CREATE TABLE accounts_transactions (
    Account_id INT AUTO_INCREMENT PRIMARY KEY, 
    balance INT,
    Account_holder_name VARCHAR(50) 
);
INSERT INTO accounts_transactions VALUES (1,10000, 'Zidane'),(2,20000, 'Khan');



CREATE TABLE transaction (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY, 
    Account_id INT,  
    amount INT,  
    transaction_type VARCHAR(10), 
    FOREIGN KEY (Account_id) REFERENCES accounts_transactions(Account_id)  
);
INSERT INTO transaction (Account_id, amount, transaction_type)
VALUES 
    (1, -100, 'debit'),  
    (2, 500, 'credit'); 

START TRANSACTION;

-- Step 1: Update the balance of an account (Account_id = 1, reducing balance by 100)
UPDATE accounts_transactions
SET balance = balance - 100
WHERE Account_id = 1; 


INSERT INTO transaction (Account_id, amount, transaction_type)
VALUES (1, -100, 'debit');

-- This will cause an error because Account_id 999 does not exist
INSERT INTO transaction (Account_id, amount, transaction_type)  -- Correct table name here: 'transaction'
VALUES (999, -50, 'debit');  -- This will fail due to the foreign key constraint

ROLLBACK;  -
