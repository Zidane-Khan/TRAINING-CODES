-- Retrieving critical data:
-- Find the next 5 trains departing from a specific station.
-- Get all available seats for a train based on class and journey date.
-- Retrieve a passenger’s complete booking history.
-- Display all trains running late (by checking real-time tracking data).
-- Get the total revenue generated per train in the last 30 days.

insert into Stations values(12,'Agra Junction','Lucknow','Delhi','West'),
(13,'Thane Junction','Mumbai','Maharashtra','West'),
(14,'Pune Junction','Pune','Maharashtra','South'),
(15,'Thane Junction','Mumbai','Maharashtra','West'),
(16,'Thane Junction','Mumbai','Maharashtra','West');

 
insert into trains values (3,'Chennai Express','sleeper-AC',500,150,'Available');
insert into train_schedule values(102,2,15,12,'2025-04-26 11:00:00',
'2025-04-26 10:00:','01:00:00','Every day'),
(103,3,15,14,'2025-04-27 11:00:00',
'2025-04-27 10:00:','01:00:00','Occasional');

--  Find the next 5 trains departing from a specific station.
select trains.train_id,trains.train_name, train_schedule.departure_station_id, stations.station_name 
from trains 
inner join train_schedule on trains.train_id=train_schedule.train_id 
inner join stations on stations.station_id=train_schedule.departure_station_id 
where train_schedule.departure_station_id=15;
#---------------------------------------------------
-- Retrieve a passenger’s complete booking history.
select * from passengers;
select * from bookings;
select  passengers.name, passengers.passenger_id, passengers.email,passengers.loyalty_points,
bookings.booking_id, bookings.passenger_id, bookings.train_id, bookings.journey_date,
bookings.seat_number, bookings.class, bookings.total_fare,bookings.booking_status
 from  passengers inner join bookings on passengers.passenger_id=bookings.passenger_id;
 
--  #---------------------------------------------------
-- Get the total revenue generated per train in the last 30 days.
select * from bookings;
select * from payments;
-- select bookings.total_fare as revenue, trains.train_id, trains.train_name 
-- from  trains inner join bookings on trains.train_id=bookings.train_id;
select payments.amount_paid as revenue, bookings.train_id, bookings.passenger_id 
from  payments inner join bookings on bookings.booking_id=payments.booking_id
where payments.payment_date>=now()-interval 30 day;



-- Payments – Stores payment transactions for ticket bookings. 
insert into payments  values(1, 1,'UPI','Complete', now(), 3000);

-- Get all available seats for a train based on class and journey date.
select * from seats;
 select * from trains;
 select * from bookings;
 select bookings.seat_number, bookings.journey_date, bookings.class,trains.available_seats from
 bookings inner join trains on trains.train_id=bookings.train_id where bookings.class='Second-C' 
 and bookings.journey_date='2025-04-26';
 
 
 -- Display all trains running late (by checking real-time tracking data).
 select * from train_schedule;
 select trains.train_id, trains.train_name from trains 
 inner join train_schedule on trains.train_id=train_schedule.train_id where  train_schedule.frequency='Occasional'
 
 




