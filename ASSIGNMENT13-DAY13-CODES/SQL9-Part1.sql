-- Set up sample tables 

-- First, create two tables called members and committees: 

CREATE TABLE members1 ( 
    member_id INT AUTO_INCREMENT, 
    name VARCHAR(100), 
    PRIMARY KEY (member_id) 
); 
 
CREATE TABLE committees1 ( 
    committee_id INT AUTO_INCREMENT, 
    name VARCHAR(100), 
    PRIMARY KEY (committee_id) 
);

INSERT INTO members1(name) 
VALUES('John'),('Jane'),('Mary'),('David'),('Amelia'); 
INSERT INTO committees1(name) 
VALUES('John'),('Mary'),('Amelia'),('Joe'); 

select * from members1;
select name from members1 where name in(select name from committees1);


-- Write a query to find members who are also the committee members. 
-- Write a query to find customers who have no order. 
-- Write a query to displays only the employees who have a manager. 
-- Write a query to returns the order numbers and the total amount of each order. 