-- 
-- Write a SQL query to create a new table named 
-- "orders" with columns for "id" (integer) and 
-- "customer_id" (integer) and set the "customer_id" column as a foreign key.

--     
--     PRIMARY KEY (OrderID),
--     FOREIGN KEY (PersonID) REFERENCES Persons(PersonID)
-- );
create table customer00 ( cust_id int primary key ,name varchar(50));

create table order99 (or_id int primary key ,  FOREIGN KEY (cust_id) references customers0);