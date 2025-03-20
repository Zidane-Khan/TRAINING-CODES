-- Perform an UPDATE operation on employee salaries and commit only if no errors occur.

CREATE TABLE Employees_operation (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(100),
    Salary INT
);

INSERT INTO Employees_operation  VALUES
(1, 'John', 50000),
(2, 'Jane', 60000),
(3, 'Alice ', 55000);

START TRANSACTION;

UPDATE Employees_operation
SET Salary = Salary + 5000
WHERE EmployeeID = 1;

UPDATE Employees_operation
SET Salary = Salary + 3000
WHERE EmployeeID = 2;

UPDATE Employees_operation
SET Salary = Salary + 4000
WHERE EmployeeID = 3;

COMMIT;
select * from Employees_operation;

-- ROLLBACK: Undoes the INSERT operation. Since we call ROLLBACK, 
-- the change (insertion of Bob Brown) will not be committed to the database.

# Demonstrate the use of ROLLBACK by executing an INSERT statement and undoing it before committing.

START TRANSACTION;

INSERT INTO Employees_operation (EmployeeID, Name, Salary) VALUES (4, 'Bob', 45000);

ROLLBACK;

COMMIT;
