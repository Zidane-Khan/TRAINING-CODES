-- Convert the following scenario into SQL tables: 
-- A school has students and teachers.
-- Each student has a unique ID, name, and grade.
-- Each teacher has a unique ID, name, and subject expertise.
-- Each teacher can teach multiple students, and each student can be taught by multiple teachers.

-- Write SQL queries to: 
-- Create tables for the above scenario with primary and foreign keys.
-- Insert sample data.
-- Retrieve all students taught by a specific teacher.

create table student( stu_ID int primary key, name varchar(10), grade varchar (5));
create table teachers ( tea_ID int primary key, name varchar(10), subject_expert varchar (15), stu_ID int,
FOREIGN KEY (stu_ID) REFERENCES student(stu_ID));

insert student values (1,'zid','B'),(2,'kar','A+'),(3,'jus','A'),(4,'Roh','A'),(5,'Sonu','B+');
insert teachers values (1,'KHN','MATH',1),(2,'SON','PHYSICS',1),(3,'YASH','ENGLISH',2),(4,'SAH','History',3);
SELECT student.stu_ID, student.name , teachers.name, teachers.subject_expert
FROM student 
INNER JOIN teachers ON student.stu_ID = teachers.stu_ID;

-- Convert the following ER diagram into SQL tables and perform CRUD operations: 
-- A library has books and members.
-- Members can borrow multiple books, but each book can only be borrowed by one member at a time.

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
    FOREIGN KEY (BookID) REFERENCES Books(BookID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID)
);
select * from Books;
select * from Members;
select * from BorrowedBooks;

INSERT INTO Books (BookID, Title, Author) VALUES
(1, 'Dark Knight', 'Nolan'),
(2, 'DC', 'Zack'),
(3, 'Marvel', 'Kevin');

INSERT INTO Members (MemberID, Name) VALUES
(1, 'John'),
(2, 'Jane'),
(3, 'Mike');


INSERT INTO BorrowedBooks (BorrowID, BookID, MemberID, BorrowDate) VALUES
(1, 1, 1, '2025-03-18'),
(2, 2, 2, '2025-03-17'),
(3, 3, 3, '2025-03-16');


SELECT b.BookID, b.Title, m.Name, bb.BorrowDate
FROM BorrowedBooks bb
JOIN Books b ON bb.BookID = b.BookID
JOIN Members m ON bb.MemberID = m.MemberID;

-- Update the return date of a borrowed book
UPDATE Books
SET Author = 'Haley quin'
WHERE BookID = 3;

DELETE FROM BorrowedBooks
WHERE BorrowID = 1;

