-- You have the following tables:
-- customers (customer_id, customer_name)
-- orders (order_id, customer_id, order_date)
-- order_items (order_item_id, order_id, product_id, quantity)
-- products (product_id, product_name, price)

-- Task: Write a query to retrieve the names of 
-- customers, the IDs of their orders, and the product name of the most expensive product they ordered.
create table customers_asses (customer_id  int primary key, customer_name varchar(20));

create table orders_asses (order_id int primary key, customer_id int, 
foreign key(customer_id) references customers_asses(customer_id));

create table order_items (order_item_id int primary key, order_id int, product_id int, quantity int,
foreign key(order_id) references orders_asses(order_id),
foreign key(product_id) references products_asses(product_id));

create table products_asses (product_id int primary key, product_name varchar(20), price int);

-- Task: Write a query to retrieve the names of 
-- customers, the IDs of their orders, and the product name of the most expensive product they ordered.

select customers_asses.customer_name,orders_asses.order_id, products_asses.product_name from customers_asses inner join orders_asses 
on customers_asses.customer_id=orders_asses.order_id inner join products_asses 
on products_asses.product_id=orders_asses.order_id   group by customer_name;

