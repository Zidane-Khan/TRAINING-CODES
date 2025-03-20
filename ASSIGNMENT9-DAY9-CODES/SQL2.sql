-- Write a SQL query to select only the unique values from a column named "city" in the "customers" table.

create table Customers( Id Int, Name varchar(10), city varchar(10));

insert into Customers values(1	,'John Doe'	,'Pune'),
(2,	'Jane Smith',	'Mumbai'),
(3	,'Mike Brown',	'Pune'),
(4	,'Emma Wils',	'Chennai'),
(5	,'Liam Davis'	,'Kolkata');
select * from Customers;

-- select Distinct city from Customers;

select city from Customers group by city
having count(*)=1;




