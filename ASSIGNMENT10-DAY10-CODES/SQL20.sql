-- Implement an Employee-Manager hierarchy
--  where an employee reports to another employee using Self-Join.
CREATE TABLE Employees (
    EmployeeID INT  PRIMARY KEY, 
    FirstName VARCHAR(10) ,
   Designation VARCHAR(10),                      
    ManagerID INT,                              
    CONSTRAINT FK_Manager FOREIGN KEY (ManagerID) REFERENCES Employees(EmployeeID) 
);
INSERT INTO Employees  VALUES
(1, 'John',  'CEO', NULL),
(2, 'Jane',  'Manager', 1),
(3, 'Emily', 'Developer', 2),
(4, 'Michael',  'Developer', 2),
(5, 'Alice', 'tester', 3);

SELECT e1.EmployeeID AS EmployeeID,
       e1.FirstName AS EmployeeFirstName,
       e1.designation AS Designation,
       e2.FirstName AS ManagerFirstName,
       e2.designation AS ManagerDesignation
FROM Employees e1
LEFT JOIN Employees e2 ON e1.ManagerID = e2.EmployeeID
ORDER BY e1.EmployeeID;
