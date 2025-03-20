-- Write a query to display the number of customer’s from Delhi.
--  Give the count an alias name of Cust_Count.

select count(*) from customer where city='Delhi';
