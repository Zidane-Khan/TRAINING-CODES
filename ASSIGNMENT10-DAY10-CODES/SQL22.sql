# Write an SQL transaction for a bank transfer from Account A to Account B, ensuring ACID properties.

CREATE TABLE Acountss (
    AccountID INT PRIMARY KEY,
    Balance int
);
CREATE TABLE Transactionss (
    TransactionID INT PRIMARY KEY,
    AccountID int,
    Amount int,
    FOREIGN KEY (AccountID) REFERENCES Acountss(AccountID)
);

INSERT INTO Acountss VALUES
(1, 5000),   
(2, 2500);   

START TRANSACTION;

UPDATE Acountss
SET Balance = Balance - 100
WHERE AccountID = 1 ;

UPDATE Acountss
SET Balance = Balance + 100
WHERE AccountID = 2;

INSERT INTO Transactionss(TransactionID, AccountID, Amount) VALUES
(1, 1, -100),
(2, 2, 100);

COMMIT;
select * from Acountss;