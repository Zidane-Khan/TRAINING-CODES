# Write a SQL query to delete all rows from a 
# table named "customers" where the "last_name" column is 'Smith'.

create table Customers3( Id Int, Name varchar(10), last_name varchar(10));

insert into Customers3 values(1	,'John'	,'Doe'),
 (2,	'Jane',	'Smith'),
 (3	,'Mike',	'Brown');


select * from Customers3;

delete from Customers3 where last_name='Smith';

select * from customers3;