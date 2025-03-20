-- Write a SQL query to update the "price" column of a table named 
-- "products" to 10.99 where the "category" column is 'electronics'.

create table products ( P_id int, category varchar(20), price int);
insert into products values(1	,'Grocery'	, 50000),
(2,	'Spare parts',	60000),
(3	,'Hardware',	70000),
(4	,'Electronics',	55000);

select * from products;

update products set price=10000 where category='Electronics';
