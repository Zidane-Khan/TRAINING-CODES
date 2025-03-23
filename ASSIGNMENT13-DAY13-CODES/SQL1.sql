-- Write a query selects the order line items from the orderdetails table. 
-- It should calculates the subtotal for each line item and sorts the result set based on the subtotal. 

create table orderdetails ( orderid int primary key, ordname varchar(10), amount int, quantity int);
insert into orderdetails values (1,'Dairy',1000,12),
(2,'Laptop',2000,10),(3,'Dairy',1000,9),(4,'Nike shoes',500,8),(5,'Laptop',2000,7);

select amount*quantity as sub_total from orderdetails order by sub_total;

select * from products;