

create table order1 ( order_id int primary key, ordname varchar(10), amount int );
create table customers1( cust_id int primary key, cust_name varchar(10), order_id int,
foreign key (order_id) references order1(order_id));
insert into order1 values(1,'Dairy',1000),
(2,'Laptop',2000),(3,'Dairy',1000),(4,'Nike shoes',500),(5,'Laptop',2000);
insert into customers1 values(1,'John',1),
(2,'Cena',2),(3,'Randy',2),(4,'Nike',1),(5,'Happy',Null);
-- Write a query to returns the order numbers and the total amount of each order. dro[alter
select ordname, sum(amount) as total_amount_each from order1 group by ordname, amount;
-- Write a query to find customers who have no order.
select cust_name from customers1 where order_id  is Null

