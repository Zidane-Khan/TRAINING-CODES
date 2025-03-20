-- Write a SQL query to update the
--  "quantity" column of a table named "inventory" to 0 where the "product_id" is 123.

create table inventory(product_id int, pro_name varchar(40), quantity int);
insert into inventory values (123,'Maggi',2),(456,'Tissue',2),(789,'Ketchup',2),(101,'Bats',3),
(103,'Colgate',1);

select * from inventory;
update inventory set  product_id=0 where pro_name='Maggi';
select * from inventory;


