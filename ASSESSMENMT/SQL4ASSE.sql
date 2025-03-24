-- You are implementing a banking system where a customer can transfer money from one account to another. When a transfer occurs:
-- The sender's account balance should decrease by the transfer amount.
-- The receiver's account balance should increase by the transfer amount.
-- A record of the transaction should be inserted into the transactions table for both the sender and receiver.
-- If any issue occurs (such as insufficient funds), the entire transaction should be rolled back.
-- Task: Write a SQL transaction to handle the money transfer process from one account to another.
create table sender_trans (send_id int, send_transfer_amount int);
create table receiver_trans (rec_id int, rec_withdraw_amount int);
insert into sender_trans values(1,2000);
insert into receiver_trans values(1,1000);

start transaction;

update sender_trans set send_transfer_amount=send_transfer_amount-1000;

update receiver_trans set rec_withdraw_amount=rec_withdraw_amount+1000;
insert into sender_trans values(2,1000); # new entries added
insert into receiver_trans values(2,2000); # new entries added

commit;
select * from sender_trans;
