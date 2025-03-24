-- You have the following tables:
-- orders (order_id, customer_id, order_date, total_amount, status)
-- order_items (order_item_id, order_id, product_id, quantity, price)
-- inventory (product_id, quantity_in_stock)
-- Task: Write a transaction that:
-- Creates a new order in the orders table with a status of 'Pending'.
-- Inserts items into the order_items table.
-- Updates the inventory to reflect the quantity of products purchased.
-- If the order creation or inventory update fails, the entire transaction should be rolled back
create table orders_trans (order_id int primary key, customer_id int, total_amount int, status varchar(15));
-- foreign key(customer_id) references customers_asses(customer_id));

create table order_items_trans (order_item_id int primary key, customer_id int, product_id int, quantity int,
price int,foreign key(product_id) references inventory_trans(product_id));

create table inventory_trans (product_id int primary key , quantity_in_stock int);
-- foreign key(order_id) references orders_asses(order_id),
-- foreign key(product_id) references products_asses(product_id));
insert into inventory_trans values (1,10);

START transaction;
insert into orders_trans  values (2, 1, 1000, 'Pending');
insert into order_items_trans values (2,1, 1, 10,1000);
update inventory_trans set quantity_in_stock=10 where product_id =1;

update inventory_trans set quantity_in_stock=10 where product_id =3;


commit;



START transaction;
insert into orders_trans  values (2, 1, 1000, 'Pending');
insert into order_items_trans values (2,1, 1, 10,1000);
update inventory_trans set quantity_in_stock=10 where product_id =1;

update inventory_trans set quantity_in_stock=10 where product_id =999;


rollback


-- Creates a new order in the orders table with a status of 'Pending'.
-- -- Inserts items into the order_items table.
-- -- Updates the inventory to reflect the quantity of products purchased.
-- -- If the order creation or inventory update fails, the entire transaction should be rolled back

