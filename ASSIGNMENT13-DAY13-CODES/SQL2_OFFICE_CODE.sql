-- Write a query finds employees who are located in offices whose office code is from 1 to 3. 
-- Table Name: employees. 

create table employees_wwe (Empid int primary key, Empname varchar(10), office_code int);
insert into employees_wwe values (1, 'John', 3),(2, 'Randy', 1),
(3, 'Undertaker', 2),
(4, 'Rock', 4),
(5, 'Brock', 6),
(6, 'Roman', 1);
select * from employees_wwe;

select Empid , Empname,office_code from employees_wwe where office_code between 1 and 3;


