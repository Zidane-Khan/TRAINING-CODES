
-- Problem # 9:
-- Write a query to display the customer’s number, customer’s firstname, 
-- branch id and loan amount for people who have taken loans.

select * from loan;

select customer.fname , customer.mobileno,loan.bid,loan.loan_amount
from customer inner join loan
 on customer.custid = loan.custid where loan.loan_amount is not null;
