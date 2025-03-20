-- Problem # 6:
-- Write a query to display the female customers firstname, city and account number
--  who are not into business, service or studies.

select customer.fname , customer.city, 
account.acnumber from customer inner join account
 on customer.custid = account.custid where customer.occupation='Housewife';
 
 select * from customer;
 select * from account;