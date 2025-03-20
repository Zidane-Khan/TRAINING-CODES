CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(10)
);

CREATE TABLE Courses (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(10)
);

CREATE TABLE Student_Courses (
    StudentID INT,
    CourseID INT,
    PRIMARY KEY (StudentID, CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

INSERT INTO Students (StudentID, StudentName) VALUES (1, 'John');
INSERT INTO Students (StudentID, StudentName) VALUES (2, 'Jane');
INSERT INTO Students (StudentID, StudentName) VALUES (3, 'Emily');

INSERT INTO Courses (CourseID, CourseName) VALUES (101, 'Math');
INSERT INTO Courses (CourseID, CourseName) VALUES (102, 'Phys');
INSERT INTO Courses (CourseID, CourseName) VALUES (103, 'Chem');

INSERT INTO Student_Courses (StudentID, CourseID) VALUES (1, 101);
INSERT INTO Student_Courses (StudentID, CourseID) VALUES (1, 102);
INSERT INTO Student_Courses (StudentID, CourseID) VALUES (2, 101);
INSERT INTO Student_Courses (StudentID, CourseID) VALUES (2, 103);
INSERT INTO Student_Courses (StudentID, CourseID) VALUES (3, 102);
