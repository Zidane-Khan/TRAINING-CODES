-- Write a query to check if a value is NULL or not, don’t use the equal operator (=). Table Name: employees. 
insert into employees_wwe1 values (5, NULL,NULL,NULL);
select * from employees_wwe1;
select Empid from employees_wwe1 where first_name is Null;