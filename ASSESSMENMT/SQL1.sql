-- You have a table employees with the following columns: id, name, department, salary, Status(Active/Inactive), hire_date.
-- Write a query to retrieve all employees whose salary is greater than the average salary in the company.
-- Write a query to find the departments that have more than 3 employees.
-- Write a query to delete all employees who are no longer active.
-- Write a query to find employees who have worked for more than 5 years.

create table employees_asses( emp_id int primary key, emp_name varchar(20),department varchar(10),
Salary int,Status varchar(10));

insert into employees_asses  values(1, 'John Cena','HR',8000,'Active'),
(2, 'Randy Orton','Tester',7000,'Active'),
(3, 'Triple H','Manger',10000,'Active'),
(4, 'Brock','Dev',7500,'Inactive'),
(5, 'Ambrose','Finance',50000,'Inactive');
select * from employees_asses ;

-- Write a query to retrieve all employees whose salary
--  is greater than the average salary in the company.

select emp_name,salary from employees_asses where salary >(select avg(salary) from employees_asses);
-- Write a query to delete all employees who are no longer active.

delete from employees_asses where status='Inactive';
select * from employees_asses; 
# deleted

-- Write a query to find the departments that have more than 3 employees.

-- create table employees_asses_more( emp_id int primary key, emp_name varchar(20),
-- dept_id int, foreign key (dept_id) references departments_asses (dept_id));
create table departments_asses( dept_id int primary key, dept_name varchar(20),
 quatmtituy_of_employees int);
 insert into departments_asses  values(1, 'HR',3),
(2, 'Tester',2),
(3, 'Manger',3),
(4, 'Dev',1);
select * from departments_asses;

# here insetead of theree i took more thn 2
select dept_name from departments_asses where  quatmtituy_of_employees>2;

-- Write a query to find employees who have worked for more than 5 years.

create table employees_asses_hire( emp_id int primary key, emp_name varchar(20),department varchar(10),
Salary int,Status varchar(10), hire_year int);


insert into employees_asses_hire  values(1, 'John Cena','HR',8000,'Active',2005),
(2, 'Randy Orton','Tester',7000,'Active',2000),
(3, 'Triple H','Manger',10000,'Active',2010),
(4, 'Brock','Dev',7500,'Inactive',2011),
(5, 'Ambrose','Finance',50000,'Inactive',2012);

select emp_name from employees_asses_hire where  hire_year>2005;