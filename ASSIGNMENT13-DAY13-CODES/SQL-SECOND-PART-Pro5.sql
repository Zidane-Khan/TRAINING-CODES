-- Problem # 5:
-- Write a query to display  the customer number, 
-- customer firstname,account number for the customer’s whose accounts were created after 15th of any month.

select customer.fname , customer.mobileno, 
account.acnumber from customer inner join account
 on customer.custid = account.custid where aod>  ;
 
 select * from account



