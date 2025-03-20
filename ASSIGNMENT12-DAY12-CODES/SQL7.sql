-- Indexes and Performance
-- What indexes would you create to optimize 
 -- the performance of a query that retrieves the total amount
 -- spent by a customer in the last 6 months from the orders table?

create table orders3 (orderid int primary key, cust_name varchar(10),  amount int , order_date date);
insert into orders3 values (1,'zid',2000, '2003-02-12'), (2,'khn',2500,'2003-04-12'),
 (3,'zid',10000,'2003-08-12'), (4,'man',2000,'2003-10-12');
 
select cust_name, sum(amount) as total_spent from orders3 where order_date>=curdate()-interval 6 month
group by cust_name;
