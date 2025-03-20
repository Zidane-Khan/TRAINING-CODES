-- Write an SQL query to find the total   number of orders and the average order amount for each customer.

-- insert into schee_order values (1,'Maggi','DEF'),(2,'Colgate','ABC'), (3,'Tissue','EFG'),(4,'LAPTOP','HIJ'),
--  (5,'Maggi','ABC'),(6,'Watch','ABC');

create table orders_schema(order_id int,order_name varchar(10) ,amount int ,cust_name varchar(10));
insert into orders_schema values(1,'Maggi',3000,'ABC'),(2,'Colgate',5000,'DEF'),(3,'Tissue',4500,'HIJ'),
(4,'LAPtop',7000,'JKL'),(5,'Watch',6500,'XYZ'),(6,'Pen',2300,'BTR');

select count(order_id), avg(amount) from orders_schema group by cust_name;
--  

 
--  select count(*) order_id,