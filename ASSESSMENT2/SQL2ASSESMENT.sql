-- You have the following tables:
-- customers (customer_id, customer_name)
-- orders (order_id, customer_id, order_date)
-- order_items (order_item_id, order_id, product_id, quantity)
-- products (product_id, product_name, price)

-- Task: Write a query to retrieve the names of 
-- customers, the IDs of their orders, and the product name of the most expensive product they ordered.

-- drop table customers_asses;
-- drop table orders_asses;
-- drop table order_items;
-- drop table products_asses;
create table customers_asses (customer_id  int primary key, customer_name varchar(20));

create table orders_asses (order_id int primary key, customer_id int, 
foreign key(customer_id) references customers_asses(customer_id));

create table order_items (order_item_id int primary key, order_id int, product_id int, quantity int,
foreign key(order_id) references orders_asses(order_id),
foreign key(product_id) references products_asses(product_id));

create table products_asses (product_id int primary key, product_name varchar(20), price int);

-- Task: Write a query to retrieve the names of 
-- customers, the IDs of their orders, and the product name of the most expensive product they ordered.
insert into customers_asses  values (1, 'John'),
 (2, 'Randy'),
  (3, 'hhh'),
   (4, 'broack');
insert into orders_asses values (1,1),(2,2),(3,3),(4,4),(5,1);
insert into order_items values (1, 1, 1, 10),
(2, 2, 2, 11),
(3, 3, 3, 12),
(4, 4, 4, 14),
(5, 4, 1, 14);
insert into  products_asses values (1, 'laptop', 1000),
(2, 'DAIRY', 2000),
(3, 'Tisuue', 100),
(4, 'Mobl2', 3000);

select * from products_asses;

select customers_asses.customer_name,orders_asses.order_id, products_asses.product_name from customers_asses inner join orders_asses 
on customers_asses.customer_id=orders_asses.order_id inner join products_asses 
on products_asses.product_id=orders_asses.order_id 
where products_asses.price=(select max(price) from products_asses );

