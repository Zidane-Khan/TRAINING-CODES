-- Write an SQL query to fetch all customers who have made at least three orders.

insert into sche_customers values (1,'ABC'),(2,'DEF'), (3,'EFG'),(4,'HIJ'), (5,'ABC'),(6,'JKL');
 
 
 create table schee_order (order_id int , ord_name varchar(20), cust_name varchar(10));
insert into schee_order values (1,'Maggi','DEF'),(2,'Colgate','ABC'), (3,'Tissue','EFG'),(4,'LAPTOP','HIJ'),
 (5,'Maggi','ABC'),(6,'Watch','ABC');

select cust_name from schee_order  group by cust_name having count(order_id)>=3;