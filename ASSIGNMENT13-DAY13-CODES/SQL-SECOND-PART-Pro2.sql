-- Write a query to display the customer’s number, first name, and middle name.
--  The customer’s who don’t have a middle name, for them display 
-- the last name. Give the alias name as Cust_Name.

select fname,mname ,ltname, Coalesce (mname,ltname) as Cust_Name from customer;