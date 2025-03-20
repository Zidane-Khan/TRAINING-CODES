-- Write a SQL query to count the number of rows in a table named "orders".
create table Orders( Id Int, Product_Name varchar(10));
insert into Orders values(1	,'Maagi'),
(2,	'Colgate'),
(3	,'Milk-Brown');
select * from Orders;

select Count(*) from Orders as No_of_rows;

