
-- Aggregate Functions and Optimization
--  How would you optimize a query to calculate total sales \
--  for each product from the sales table in the last year, considering a large dataset?

create table sales ( salesid int primary key, products varchar(10), amount int);
insert into sales values (1,'laptop',1000),(2,'phone',500),(3,'phone',500),(4,'laptop',1000),(5,'laptop',100),(6,'Tablet',600);


select products, sum(amount) as total_sales from sales group by products;