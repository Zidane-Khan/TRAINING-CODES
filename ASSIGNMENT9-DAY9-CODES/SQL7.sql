
-- Write a SQL query to add a new column named "email" (text) to an existing table named "users".

create table users( id Int, Name varchar(10), age int);
insert into users values(1	,'John'	,22),
 (2,	'Jane',	19),
 (3	,'Mike', 20);

ALter table users add column email varchar(10);
select * from users;