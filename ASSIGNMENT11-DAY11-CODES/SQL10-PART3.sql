-- Create an index on the "email" column of a "users" table.
-- Write a SQL query to create an index on a column named "name" in a table named "products.


create table users ( name varchar(10), email varchar(11));
create index email_ind on users(email);