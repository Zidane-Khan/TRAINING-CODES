#fact-stores quantitayive data (revenue,sales)
#dimension-store descriptive data (name,product)

-- Retrieve total sales for a given month.

create table sales_facts( sales_id int, pro_id int, cust_id int, revenue int, total_sales int);
create table sales_dimens( pro_id int , pro_category varchar(10), pro_name varchar(10), cust_name varchar(10), month varchar(10));

insert into  sales_facts values(1, 1, 1, 30000, 20),(2,2,2,40000,30),(3,3,3,40500,10),(4,4,4,40000,15);
insert into  sales_dimens values(1,'electron','laptop','zid','FEB'),
(2,'grocery','tomao','khn','JAN'), 
(3,'food','maggi','ghi','FEB'), 
(4,'clothes','jeans','abc','MAR'), 
(5,'dairy','milk','zid','JAN');

select sum(sales_facts.total_sales), sales_dimens.month from sales_facts inner join sales_dimens 
on sales_facts.pro_id=sales_dimens.pro_id group by sales_dimens.month;