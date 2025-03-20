-- Transactional Integrity
--  What steps will you take to ensure both an insert into a
--  transactions table and an update to a bank_accounts table 
--  happen as a single transaction, and can be rolled back if one action fails?

-- Use ROLLBACK to undo changes.
create table  account2( Account_id Int primary key , balance int, Account_holder_name varchar(10));
CREATE TABLE transaction1 (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY, 
    Account_id INT,  
    amount INT,  
    FOREIGN KEY (Account_id) REFERENCES account2(Account_id)  
);
insert into account2 values(1,2000,'zid'),(2,1000,'khn');
start transaction;
insert into transaction1 values (2,1,500);

-- Step 1: Update the balance of an account (Account_id = 1, reducing balance by 100)
-- UPDATE account2
-- SET balance = balance - 500
-- WHERE Account_id = 1;  

UPDATE account2
SET balance = balance - 5100
WHERE Account_id = 6;  

rollback;

select * from transaction1;
select * from account2;

