-- Convert the following ER model into SQL tables: 
-- Employees (EmpID, Name, Age, DepartmentID), Departments (DeptID, DeptName), Projects (ProjID, ProjName, DeptID).


-- Creating the Departments table
CREATE TABLE Departmentss (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(10) 
);

-- Creating the Employees table
CREATE TABLE Employeees (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(10),
    Age INT,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DeptID)
);

-- Creating the Projects table
CREATE TABLE Projects (
    ProjID INT PRIMARY KEY,
    ProjName VARCHAR(10),
    DeptID INT,
    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID)
);
