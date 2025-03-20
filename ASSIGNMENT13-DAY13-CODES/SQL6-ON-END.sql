-- Write a query to find all employees whose last names contain the substring “on”. Table Name: employees.

select Empid, first_name, last_name from  employees_wwe1 where last_name  like '%on'; 

