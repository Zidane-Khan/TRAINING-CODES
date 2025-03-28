
-- 2. Query Operations: Retrieving and Manipulating Data
-- Write MySQL queries to perform the following operations:

# Adding new records:
# Insert a new train schedule into the database.
# Add a new passenger and book a ticket for a specific train.
# Update seat availability when a new booking is made.


# Insert a new train schedule into the database.
insert into trains values(1,'Rajdhani Express',
'Super fast',200,500,'Available');
insert into Stations values(10,'Jaipur Junction','Jaipur','Rajasthan','West');
insert into Stations values(11,'Mumbai Junction','Mumbai','Maharashtra','South');
insert into train_schedule values(101,1,10,11,'2025-04-26 11:00:00',
'2025-04-26 10:00:','01:00:00','Every day');
#----------------------------------------------------------------------------------------------------

# Add a new passenger and book a ticket for a specific train.
insert into Passengers values (1001 , 'John Cena',
 35, 'Male', 87886745262, 'ucanseeme@gmail.com', 'westnewberry masechuseets', 50,now()); 
insert into Bookings values (1, 1001 ,1,'2025-04-26', 'A110','First-C', 3000 , 'Completed',  now(),1);
select * from bookings;
select * from passengers;

insert into Passengers values (1002 , 'Cm punk',
 35, 'Male', 878867452262, 'mitbe@gmail.com', 'westnewberry aew', 20,now()); 
 
 select * from bookings;
 insert into Bookings values (2, 1002 ,2,'2025-04-26', 'A111','Second-C', 2000 , 'Completed',  now(),2);
 
 select * from train_schedule;
 select * from trains;


#----------------------------------------------------------------------------------------------------

-- Update seat availability when a new booking is made.
insert into seats values (1,1,'A110','First-C','YES');
select * from seats;


