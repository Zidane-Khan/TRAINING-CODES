# Create tables for a Library Management System with proper primary keys, foreign keys, and constraints.

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title VARCHAR(50),
    Author VARCHAR(50)
);

CREATE TABLE Members (
    MemberID INT PRIMARY KEY,
    Name VARCHAR(50)
);

CREATE TABLE BorrowedBooks (
    BorrowID INT PRIMARY KEY,
    BookID INT,
    MemberID INT,
    BorrowDate DATE,
    DueDate DATE,
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);