-- Use SAVEPOINT to update multiple tables in
--  a transaction and roll back only specific changes while keeping others.
-- Implement a scenario where multiple updates 
-- occur in a transaction, but a condition check decides whether to COMMIT or ROLLBACK.


CREATE TABLE Employees_savept (
    EmployeeID INT PRIMARY KEY,
    Name VARCHAR(10),
    Salary INT,
    DeptID INT
);

CREATE TABLE Departments_savept (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(10)
);

INSERT INTO Employees_savept (EmployeeID, Name, Salary, DeptID) VALUES
(1, 'Joh', 50000, 1),
(2, 'Jan', 60000, 2);

INSERT INTO Departments_savept (DeptID, DeptName) VALUES
(1, 'HR'),
(2, 'DEV');

DELIMITER //

CREATE PROCEDURE UpdateEmployeeSalariess()
BEGIN
    START TRANSACTION;
-- Update Employee 1
    UPDATE Employees_savept
    SET Salary = 55000, DeptID = 2
    WHERE EmployeeID = 1;

    -- Create a savepoint after updating Employee 1
    SAVEPOINT BeforeEmployee2Update;

    -- Update Employee 2
    UPDATE Employees_savept
    SET Salary = 65000, DeptID = 1
    WHERE EmployeeID = 2;

    -- Condition Check
    IF (SELECT Salary FROM Employees_savept WHERE EmployeeID = 2) > 60000 THEN
        -- Rollback only the changes to Employee 2
        ROLLBACK TO SAVEPOINT BeforeEmployee2Update;
    END IF;

    -- Commit the changes
    COMMIT;
END //

DELIMITER ;

select * from Employees_savept


DELIMITER //

CREATE PROCEDURE UpdateEmployeeSalariesn()
BEGIN
    START TRANSACTION;

    -- Update Employee 1's salary and department
    UPDATE Employees
    SET Salary = 55000, DeptID = 2
    WHERE EmployeeID = 1;

    -- Create a savepoint after updating Employee 1
    SAVEPOINT BeforeEmployee2Update;

    -- Update Employee 2's salary and department
    UPDATE Employees
    SET Salary = 65000, DeptID = 1
    WHERE EmployeeID = 2;

    -- Condition Check: If total salary in Dept 1 exceeds 100000, rollback all changes

    IF (SELECT SUM(Salary) FROM Employees WHERE DeptID = 1) > 100000 THEN
        -- Rollback only the changes to Employee 2
        ROLLBACK TO SAVEPOINT BeforeEmployee2Update;
    END IF;

    -- Commit the changes
    COMMIT;
END //

DELIMITER ;

select * from employees
