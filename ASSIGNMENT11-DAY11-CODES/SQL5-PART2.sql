-- Fact Table: Stores quantitative data 
-- (e.g., sales, revenue, transactions). It often contains foreign keys pointing to dimension tables.
-- Dimension Tables: Store descriptive or categorical 
-- information (e.g., products, time, customers). 
-- These tables are typically smaller and provide context to the facts.
-- Design and implement a conceptual schema for a banking system with customers, accounts, and transactions.
create table Customers(cust_id int primary key, name varchar(10));
create table accounts(acc_id int primary key, balance int, cust_id int, 
foreign key(cust_id) references Customers(cust_id));
create table Transaction(Tra_id int primary key, amount int, acc_id int, 
foreign key(acc_id) references accounts(acc_id));

insert into Customers values (1, 'John'),(2, 'Jane'),(3, 'Mike');
insert into accounts values (1, 2000,1),(2, 3000,2), (3,2500,3);
insert into Transaction values (1, 200,1),(2, 300,2), (3,250,3);

select * from Customers;
select * from accounts;
select * from Transaction;

-- drop table Customers;
-- drop table accounts;
-- drop table Transaction;

