-- Foreign Key Constraints
--  How do foreign key constraints help maintain data integrity
--  when inserting data into the enrollments table, 
--  where student_id and course_id must exist in their respective tables?

select * from students;
create table course ( course_id int primary key, course_name varchar(10), student_id int,
foreign key (student_id) references students(student_id));

create table enrollments ( enrollment_name varchar(10), student_id int,course_id int,
foreign key (student_id) references students(student_id),
foreign key (course_id) references course(course_id));