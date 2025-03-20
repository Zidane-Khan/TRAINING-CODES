-- Primary Key Constraints
-- What happens when you try to insert a 
-- duplicate value into a student_id column that has a primary key constraint?

drop table students;
create table students ( student_id int primary key , student_name varchar(10));
insert into students values (1,'ZID'),(2,'SAM'),(3,'KHN');

-- duplicate value into a student_id column that has a primary key constraint?
insert into students values(1,'MAN')

# This is error,.
-- 0	72	03:11:33	insert into students values(1,'MAN')	
-- Error Code: 1062. Duplicate entry '1' for key 'students.PRIMARY'	0.000 sec