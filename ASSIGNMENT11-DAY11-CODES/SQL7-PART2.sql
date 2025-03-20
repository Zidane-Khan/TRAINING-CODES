#Write an SQL query to create a view that shows only high-value customers 
# e.g., customers with transactions above $10,000).

# I have used 2500 instead
Create view high_value1 AS
SELECT Customers.name, accounts.balance
FROM Customers
INNER JOIN accounts ON Customers.cust_id = accounts.acc_id where accounts.balance>2500;

select * from high_value1;
