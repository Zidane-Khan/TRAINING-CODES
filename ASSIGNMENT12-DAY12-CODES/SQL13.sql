-- Handling Null Values
-- How would you ensure data integrity when dealing 
 -- with NULL values in the date_of_birth column of the employees table?
 
 create table employs ( empid int primary key , empname varchar(10), date_of_birth varchar(10) not null);
 
 insert into employs values (1,'zid', '12-2-3004'), (2,'khn', Null);
 
 -- using not null i can  handle data integrity...

-- 0	80	03:23:02	insert into employs values (1,'zid', '12-2-3004'), (2,'khn', Null)	E
-- 0	80	03:23:02	insert into employs values (1,'zid', '12-2-3004'), (2,'khn', Null)	E
-- rror Code: 1048. Column 'date_of_birth' cannot be null	0.000 sec