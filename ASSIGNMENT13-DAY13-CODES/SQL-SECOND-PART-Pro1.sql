-- Problem#1:
-- Write a query to display the customer number, firstname,
--  customer’s date of birth. Display in sorted order of date of 
--  birth year and within that sort by firstname.
select fname,mobileno, dob from customer
ORDER BY year(dob), fname;
 
--  SQL-SECOND-PART-Pro1