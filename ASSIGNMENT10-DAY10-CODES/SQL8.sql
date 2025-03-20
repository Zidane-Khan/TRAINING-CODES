-- Use transactions to ensure Isolation by 
-- running two concurrent transactions and ensuring they don't interfere with each other.
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE account_id = 1;
BEGIN;
UPDATE accounts SET balance = balance - 50 WHERE account_id = 1;

-- Commit Transaction 2 (Only after Transaction 1 is completed)
COMMIT;

-- Commit Transaction 1
COMMIT;

select* from accounts;
