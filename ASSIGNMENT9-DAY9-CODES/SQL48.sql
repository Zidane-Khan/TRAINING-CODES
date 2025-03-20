# Implement a transaction in SQL to tra0nsfer funds from one bank account to another, ensuring atomicity and consistency. 
DELIMITER $$

CREATE PROCEDURE transfer_funds(
     IN sender_id INT, 
     IN receiver_id INT, 
     IN transfer_amount DECIMAL(10,2)
 )
BEGIN
     DECLARE sender_balance DECIMAL(10,2);

--     -- Start transaction
     START TRANSACTION;

--     -- Check sender's balance
     SELECT balance INTO sender_balance FROM accounts WHERE account_id = sender_id;

    IF sender_balance < transfer_amount THEN
--         -- Rollback if insufficient funds
       ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient funds';
     ELSE
--         -- Deduct from sender
        UPDATE accounts SET balance = balance - transfer_amount WHERE account_id = sender_id;

--         -- Add to receiver
       UPDATE accounts SET balance = balance + transfer_amount WHERE account_id = receiver_id;

--         -- Commit transaction
       COMMIT;
    END IF;
 END $$

 DELIMITER ;