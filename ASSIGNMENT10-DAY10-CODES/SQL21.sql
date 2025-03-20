-- Implement a supertype-subtype relationship for Users (with Customers and Admins as subtypes).

CREATE TABLE stores (
    UserID INT PRIMARY KEY,
    Name VARCHAR(50),
    UserType VARCHAR(10)
);

CREATE TABLE Customerss (
    UserID INT PRIMARY KEY,
    MembershipDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

CREATE TABLE personal_customers (
    UserID INT PRIMARY KEY,
    AdminLevel INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);
