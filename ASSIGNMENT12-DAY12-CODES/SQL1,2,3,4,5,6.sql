-- Implement a clustered index on the "order_id" column of an "orders" table. 
select * from orders;
# if key_name = primary is clustered index

-- Implement a non-clustered index on the "product_name" column of a "products" table. 
alter table products add column product_name varchar(10);
select * from products;
CREATE INDEX index_product_name 
ON products (product_name);
# if key_name =! primary is non clustered index

-- Create a hash-based index for a "customer_id" column in a "transactions" table. 

CREATE TABLE products1 (
    product_id INT,
    product_name VARCHAR(20),
    INDEX product_id_index USING HASH (product_id)
);

-- Implement a full-text index on a "description" 
-- column in a "products" table and write a query to search for a keyword.
create table prodcts( proid int primary key , proname varchar(10), description text);
insert into prodcts values (1,'laptop','intel hard core 124'),(2,'dairy','amul milk 200 ml pasteurized'),
(3,'laptop','intel hard cor');
CREATE FULLTEXT INDEX description_index ON prodcts (description);
select * from prodcts where match (description) against ('intel');

-- ⦁	Write an SQL query to analyze the impact of indexing on query 
-- performance by running queries before and after creating indexes. 

create table see_index ( ind_id int, ind_name varchar(10));
insert into see_index values (1, 'zid'),(2,'khn'),(3,'Man');

select ind_name from see_index where ind_id=1;

create index speed_index on see_index (ind_id);

select ind_name from see_index where ind_id=1;



-- 3	121	04:32:52	select ind_name from see_index where ind_id=1
--  LIMIT 0, 1000	1 row(s) returned	0.000 sec / 0.000 sec
--  
--  3	123	04:33:45	select ind_name from see_index where ind_id=1
--  LIMIT 0, 1000	1 row(s) returned	0.000 sec / 0.000 sec

-- ⦁	Compare the performance of indexed vs. non-indexed queries using EXPLAIN ANALYZE.

create table compare (orderid int primary key, cust_name varchar(10),  amount int , order_date date);
insert into compare values (1,'zid',2000, '2003-02-12'), (2,'khn',2500,'2003-04-12'),
 (3,'zid',10000,'2003-08-12'), (4,'man',2000,'2003-10-12');
 
 
explain analyze
select cust_name from compare where orderid=1;
-- Rows fetched before execution  (cost=0..0 rows=1) (actual time=300e-6..400e-6 rows=1 loops=1)
create index compare_index on compare(cust_name , orderid);
explain analyze
select cust_name from compare where orderid=1;
-- Rows fetched before execution  (cost=0..0 rows=1) (actual time=500e-6..600e-6 rows=1 loops=1)
 
 
 


 



