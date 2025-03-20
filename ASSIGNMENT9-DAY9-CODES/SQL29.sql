-- Write a SQL query to create an index on multiple columns,
--  "first_name" and "last_name", in a table named "users".

select * from  users;
create index mul_indx on users(Name, age);