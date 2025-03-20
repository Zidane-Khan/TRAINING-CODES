-- Subqueries and Performance
--  How can you optimize a query that retrieves products in the ‘Electronics’ category by using a subquery?

create table retails ( ret_id int primary key , category varchar (10) );
create table retriever(retr_id int primary key, ret_id int, products_name varchar(10),
foreign key (ret_id) references retails(ret_id));

insert into retails values (1,'Electroncs'),(2,'grocery'),(3,'dairy'),(4,'Electroncs');
insert into retriever values( 1,2,'tomato'),( 2,1,'laptop'),( 3,3,'milk'),( 4,1,'phone');
select * from retails;
select * from retriever;

SELECT products_name 
FROM retriever 
WHERE ret_id IN (SELECT ret_id FROM retails WHERE category = 'Electroncs');


-- select products_name from retriever where 
-- ret_id IN (select category from retails where category='Electroncs');