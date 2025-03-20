-- Problem # 7:
-- Write a query to display city name and count of branches in that city.
--  Give the count of branches an alias name of Count_Branch.
select bcity,count(bcity) as Count_Branch from branch group by bcity;
select * from branch;
