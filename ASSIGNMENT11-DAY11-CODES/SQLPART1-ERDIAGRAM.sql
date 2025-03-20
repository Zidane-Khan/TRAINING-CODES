-- #ER DIAGRAM
-- #ENTITIES

create table user( userID int primary key , Name varchar(10));
create table orders( orderId int primary key, userID int, Amount int,
 foreign key (userID) references user(userID));
 
 
create table products( productId int primary key,
 orderID int, Quantity int,
 foreign key (orderID) references orders(orderID));
 
 
 