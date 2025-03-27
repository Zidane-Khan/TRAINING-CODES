CREATE TABLE Users (
    UserID INT PRIMARY KEY,  
    FirstName VARCHAR(10) ,      
    Email VARCHAR(255) UNIQUE NOT NULL,     
    Password VARCHAR(255) NOT NULL,         
    DateCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,             
    ShippingAddress VARCHAR(255),          
    PaymentMethod VARCHAR(100),               
    FOREIGN KEY (CustomerID) REFERENCES Users(UserID) ON DELETE CASCADE 
);
CREATE TABLE Admins (
    AdminID INT PRIMARY KEY,                 
    Role VARCHAR(100),                          
    Permissions TEXT,                           
    FOREIGN KEY (AdminID) REFERENCES Users(UserID) ON DELETE CASCADE 
);

