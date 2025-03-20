-- Write a query using the WHERE clause with the IN operator to find
--  employees who are located in the office with office code 1. 

select * from employees_wwe1;
select office_code , first_name , last_name from employees_wwe1 where office_code in (1);