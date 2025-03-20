-- Write a SQL query to add a unique constraint on a column named "email" in a table named "users"

select * from users;

alter table users add constraint  unique(email) ;
