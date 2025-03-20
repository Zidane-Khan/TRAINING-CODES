-- Check Constraints
-- Write a CHECK constraint for the products table to 
-- ensure that the price of each product is always greater than 0. Why is this important for data integrity?


CREATE TABLE Products2 (
    proid int primary key,
    proname varchar(10),
    price int,
    CHECK (price>0)
);

insert into Products2 values( 1,'Zid',100),( 2,'khn',200);

insert into products2 values (3, 'man' , 0);
-- 0	83	03:28:21	insert into products2 values (3, 'man' , 0)	
-- Error Code: 3819. Check constraint 'products2_chk_1' is violated.	0.000 sec