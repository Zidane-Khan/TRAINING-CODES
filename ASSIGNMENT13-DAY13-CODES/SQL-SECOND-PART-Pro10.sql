-- Problem # 10:
-- Write a query to display customer number, customer name, a
-- ccount number where the account status is terminated.

select account.acnumber,customer.fname , customer.mobileno,account.astatus
from customer inner join account
 on customer.custid = account.custid where account.astatus='terminated';
