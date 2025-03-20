-- Write an SQL query to create a composite index on "last_name" and "first_name" in an "employees" table.

create table employees ( first_name varchar(10), last_name varchar (10));
select * from employees;

create index composite_index on employees(first_name , last_name);
