
-- Demonstrate Atomicity by performing a transaction that 
-- deducts and adds funds but rolls back if an error occurs. 

select * from accounts;
BEGIN;

-- Deduct funds from Account A
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;

-- Add funds to Account B
UPDATE accounts SET balance = balance + 100 WHERE account_id = 2;

-- Simulating an error (e.g., Account B does not exist or balance is insufficient)
-- ROLLBACK will occur if there's any issue, reverting the entire transaction.
-- For demonstration, we intentionally cause an error by updating a non-existent account.
UPDATE accounts SET balance = balance + 100 WHERE account_id = 999;

-- If no error occurs, commit the transaction
COMMIT;
