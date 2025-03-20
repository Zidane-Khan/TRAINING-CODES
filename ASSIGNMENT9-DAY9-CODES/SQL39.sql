-- Write an  Write an SQL query to find the top five customers with the highest total order amounts.
-- create table orderr (cust_id int, name varchar(20),amount int) ;
-- insert into orderr values (1,'abc',3000),(2,'def',5000),(3,'hij',7000),(4,'klm',2000),(5,'xyz',1000);

SELECT name,amount FROM orderr order by amount DESC limit 5;


