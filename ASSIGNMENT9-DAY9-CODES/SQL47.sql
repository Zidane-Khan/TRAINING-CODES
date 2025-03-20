
-- Add a unique constraint to the "email" column of the "customers" table to enforce uniqueness of email addresses.




ALTER TABLE customers3
ADD COLUMN email VARCHAR(10);
ALTER TABLE customers3
ADD CONSTRAINT unique_email UNIQUE (email);


select * from customers3