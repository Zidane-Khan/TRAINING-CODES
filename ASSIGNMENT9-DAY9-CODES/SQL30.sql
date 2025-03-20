-- Write a SQL query to rename a column 
-- named "age" to "years_old" in a table named "students". 

select*from students;
alter table students rename column age to years_old;