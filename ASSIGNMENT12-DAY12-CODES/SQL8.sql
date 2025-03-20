#oin Optimization
 #How would you optimize a query that retrieves 
 #employee names from the employees table who work in the 'Sales' department, assuming large datasets?

select * from employee;
ALTER TABLE employee
DROP COLUMN dept_name;
select * from employee;
create table departmentt ( id int primary key , dept_name varchar(10), Emp_id int,
foreign key (Emp_id) references employee(Emp_id));
insert departmentt values (1,'HR',2),(2,'SALES',1),(3,'DEV',3),(4,'TESTER',4),(5,'SALES',2),(6,'HR',1);
select * from departmentt;
select employee.name , departmentt.dept_name from employee inner join 
departmentt on employee.Emp_id=departmentt.id where departmentt.dept_name='SALES';