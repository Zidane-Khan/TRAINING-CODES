-- Write -  query finds the employees whose last names end with the string 'son'. Table Name: employees. 

show tables;
create table employees_wwe1 (Empid int primary key, first_name varchar(10), last_name varchar(10),
office_code int);
insert into employees_wwe1 values (1, 'John','Cena', 3),(2, 'Randy','Orton',1),
(3, 'Undertaker','night', 2),
(4, 'Rock','Joshson' ,4),
(5, 'Brock','Lesnar', 6),
(6, 'Roman','reigns', 1);

select Empid, first_name, last_name from  employees_wwe1 where last_name  like '%son';