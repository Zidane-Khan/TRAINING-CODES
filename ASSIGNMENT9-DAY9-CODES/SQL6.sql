-- Write a SQL query to create a new table
--  named "students" with columns for "id" (integer), "name" (text), and "age" (integer).

create table students( id Int, Name varchar(10), age int);
insert into students values(1	,'John'	,22),
 (2,	'Jane',	19),
 (3	,'Mike', 20);

select* from students;

