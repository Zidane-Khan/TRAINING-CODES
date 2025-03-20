-- Write a SQL query to select all columns from a table named "employees".

create table employees ( Emp_id int, emp_name varchar(20), Salary int);
insert into employees values(1	,'John Doe'	,50000),
(2,	'Jane Smith',	60000),
(3	,'Mike Brown',	70000),
(4	,'Emma Wilson',	55000),
(5	,'Liam Davis'	,80000);

select * from employees;
