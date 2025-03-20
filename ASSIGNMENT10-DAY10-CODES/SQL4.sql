#Demonstrate how to process multiple 
#\product purchases in a single transaction to ensure all products are added to Order_Details

drop table Orders_multiples;
drop table Orders_Details;
CREATE TABLE Orders_multiples (
    OrderID INT PRIMARY KEY,
    CustomerID INT
);


CREATE TABLE Orders_Details (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    Price INT,
    FOREIGN KEY (OrderID) REFERENCES Orders_multiples(OrderID)
);

START TRANSACTION;
INSERT INTO Orders_multiples (OrderID, CustomerID)
VALUES (1, 1);
INSERT INTO Orders_multiples (OrderID, CustomerID)
VALUES (2, 2);

INSERT INTO Orders_Details (OrderDetailID, OrderID, ProductID, Quantity, Price)
VALUES (1, 1, 101, 12, 1900);

INSERT INTO Orders_Details (OrderDetailID, OrderID, ProductID, Quantity, Price)
VALUES (2, 2, 102, 15, 2900);


COMMIT;


