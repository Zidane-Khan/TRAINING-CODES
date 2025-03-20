-- Write a query to displays only the employees who have a manager. 

create table manager( manager_id int primary key, manager_name varchar(10));
create table employees_foot(empid int primary key, emp_name varchar(10), manager_id int ,
foreign key(manager_id) references manager(manager_id));


insert  into manager values(1,'RONALDO'),
(2,'Messi'),(3,'Neymar');
insert  into employees_foot values(1,'JOhn',1),
(2,'Cena',2),(3,'hhh', Null);
select emp_name from employees_foot where manager_id is not null;



-- CREATE DATABASE bank;

-- USE bank;
-- Creating table customer
-- CREATE TABLE customer
--    (
--        custid VARCHAR(6),
--        fname VARCHAR(30),
--        mname VARCHAR(30),
--        ltname VARCHAR(30),
--        city VARCHAR(15),
--        mobileno VARCHAR(10),
--        occupation VARCHAR(10),
--        dob DATE,
--       CONSTRAINT customer_custid_pk PRIMARY KEY(custid)   
--    );

-- The customer table is created successfully, now we will create the next table "branch".

-- Creating table branch
-- CREATE TABLE branch
--    (
--     bid VARCHAR(6),
--     bname VARCHAR(30),
--     bcity VARCHAR(30),
--     CONSTRAINT branch_bid_pk PRIMARY KEY(bid) 
--    );

-- Creating table account
-- CREATE TABLE account
--    (
--       acnumber VARCHAR(6),
--       custid  VARCHAR(6),
--       bid VARCHAR(6),
--       opening_balance INT(7),
--       aod DATE,
--       atype VARCHAR(10),
--       astatus VARCHAR(10),
--       CONSTRAINT account_acnumber_pk PRIMARY KEY(acnumber),
--       CONSTRAINT account_custid_fk FOREIGN KEY(custid) REFERENCES customer(custid),
--       CONSTRAINT account_bid_fk FOREIGN KEY(bid) REFERENCES branch(bid) 
--     );

-- reating table trandetails
-- CREATE TABLE trandetails
--     (   
--      tnumber VARCHAR(6),
--      acnumber VARCHAR(6),
--      dot DATE,
--      medium_of_transaction VARCHAR(20),
--      transaction_type VARCHAR(20),
--      transaction_amount INT(7),    
--      CONSTRAINT trandetails_tnumber_pk PRIMARY KEY(tnumber),
--      CONSTRAINT trandetails_acnumber_fk FOREIGN KEY(acnumber) REFERENCES account(acnumber)  
--     );

-- Creating table loan
-- CREATE TABLE loan
--    (
--    
--     custid VARCHAR(6),
--     bid VARCHAR(6),
--     loan_amount INT(7),
--     CONSTRAINT loan_customer_custid_bid_pk PRIMARY KEY(custid,bid),
--     CONSTRAINT loan_custid_fk FOREIGN KEY(custid) REFERENCES  customer(custid),
--     CONSTRAINT loan_bid_fk FOREIGN KEY(bid) REFERENCES  branch(bid)
--    );


