-- Write a SQL query to create a new table named 
-- "categories" with columns for "id" (integer) 
-- and "name" (text) and set the "id" column as the primary key.

create table categories(id int primary key , name varchar(20));
insert into categories values (1	,'John Doe'),(2	,'Jane Smith'),(3	,'Mike Brown');
select * from categories

