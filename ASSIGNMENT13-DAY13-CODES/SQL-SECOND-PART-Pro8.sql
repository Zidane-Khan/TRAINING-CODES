-- Problem # 8:
-- Write a query to display account id, customer’s firstname,
--  customer’s lastname for the customer’s whose account is Active.

select account.acnumber,customer.fname , customer.ltname,account.astatus
from customer inner join account
 on customer.custid = account.custid where account.astatus='Active';
 
 select * from account;

