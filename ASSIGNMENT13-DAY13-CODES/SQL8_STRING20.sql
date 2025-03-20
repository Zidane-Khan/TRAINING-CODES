-- Write a query to find products whose product codes contain the string _20 ,
-- \ you can use the pattern. Table Name: products 

create table products ( proid int primary key, proname varchar(10), productCode varchar(20));
insert into products values(1,'Dairy','ABC_10'),
(2,'Laptop','ABC_20'),(3,'Jersey','ABC_5'),(4,'Nike shoes','ABC_20');

select proid, proname,productCode from products where productCode like '%_20';