-- Implement a transaction in SQL to tra0nsfer funds from one bank account to another, e
-- nsuring atomicity and consistency

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    balance DECIMAL(10, 2) NOT NULL
);



START TRANSACTION;

-- Step 1: Subtract funds from the sender's account
UPDATE accounts
SET balance = balance - @amount
WHERE account_id = @sender_account
AND balance >= @amount; -- Ensures the sender has enough funds

-- Step 2: Add funds to the receiver's account
UPDATE accounts
SET balance = balance + @amount
WHERE account_id = @receiver_account;

-- Step 3: Check for errors or insufficient funds
IF ROW_COUNT() = 0
BEGIN
    ROLLBACK; -- Rollback if no rows were updated (e.g., insufficient funds)
    SELECT 'Transaction failed' AS status;
    RETURN;
END

-- Step 4: Commit the transaction if everything was successful
COMMIT;

