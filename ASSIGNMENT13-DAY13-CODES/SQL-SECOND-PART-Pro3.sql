-- Problem#3:
-- Write a query to display account number, 
-- customer’s number, customer’s firstname,lastname,account opening date


select customer.fname ,customer.ltname, customer.mobileno, 
account.acnumber,account.aod from customer inner join account
 on customer.custid = account.custid  ;



--       acnumber VARCHAR(6),
--       custid  VARCHAR(6),
--       bid VARCHAR(6),
--       opening_balance INT(7),
--       aod DATE,

