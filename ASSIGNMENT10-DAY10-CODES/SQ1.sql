drop table accounts;
create table  accounts( Account_id Int, balance int, Account_holder_name varchar(10));
insert into Accounts values(1,10000,'zidane'),(2,20000,'khn');

START TRANSACTION;

-- Deduct $150 from Account A
UPDATE Accounts
SET Balance = Balance - 150
WHERE Account_iD = 1;

-- Add $150 to Account B
UPDATE Accounts
SET Balance = Balance + 150
WHERE Account_iD = 2;

-- Commit the transaction if both operations succeed
COMMIT;

select * from Accounts;