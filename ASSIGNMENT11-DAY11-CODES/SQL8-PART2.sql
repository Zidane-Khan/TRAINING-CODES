-- Implement a logical schema for an employee management system and create tables using SQL.

create table employee( Emp_id int primary key, name varchar(10), dept_name varchar(10), dept_id int,
foreign key (dept_id) references department(dept_id));
create table department( dept_id int primary key, dept_name varchar(10));
create table salary (Emp_id int primary key, Sal int, foreign key (Emp_id) references Employee(Emp_id));

insert into  department values(1,'HR'),(2,'DEV'),(3,'Tester'),(4,'Accountant'),(5,'Manger');
insert into  employee values(1,'ABC','DEV',2),(2,'GHI','HR',1),(3,'JKL','Tester',3),(4,'XYZ','Accountant',4),(5,'Manger','MNO',5);
