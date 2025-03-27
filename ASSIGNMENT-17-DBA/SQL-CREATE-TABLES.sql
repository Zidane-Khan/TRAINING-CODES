# train tabl-
create table trains (train_id int primary key , train_name
varchar(50), train_type varchar(50), total_seats int, 
available_seats int , status varchar(20));


--  Stations – Stores station details. 
create table Stations (station_id int primary key , 
station_name varchar(50), city varchar(50), state varchar(50), zone varchar(50)) ;

-- Train_Schedule – Stores train schedules and timings. 
create table Train_Schedule(schedule_id int primary key, train_id int,
 departure_station_id int, arrival_station_id int, departure_time datetime,
 arrival_time datetime, 
 journey_duration time, frequency varchar(20), 
 foreign key (train_id) references trains(train_id),
 foreign key (departure_station_id) references Stations(station_id),
 foreign key (arrival_station_id) references Stations(station_id));


-- Routes – Stores train routes with intermediate stops. 
create table Routes (route_id int primary key, train_id int, station_id int, 
arrival_time datetime, departure_time datetime, sequence_number int,
 foreign key (train_id) references trains(train_id),
 foreign key (station_id) references Stations(station_id));


-- Passengers – Stores passenger details. 
create table Passengers (passenger_id int primary key , name varchar(20),
 age int, gender varchar(10), 
contact varchar(15) unique, 
email  varchar(20) unique,
 address text, loyalty_points int, created_at timestamp default current_timestamp) ;

-- Bookings – Stores ticket booking records. 
create table Bookings (booking_id int primary key, passenger_id int, train_id int, 
journey_date date, 
seat_number varchar(10), class varchar(10), 
total_fare int, booking_status varchar(10), 
booking_time timestamp  default current_timestamp, payment_id int unique,
foreign key (passenger_id) references Passengers(passenger_id),
 foreign key (train_id) references trains(train_id));
 

-- Payments – Stores payment transactions for ticket bookings. 
create table Payments (payment_id int primary key, booking_id int unique, 
payment_method varchar(10), 
transaction_status varchar(10), payment_date timestamp default current_timestamp, 
 amount_paid int, foreign key (booking_id) references Bookings(booking_id)) ;

-- Cancellations – Stores cancellation records and refunds. 
Create table cancellation (cancellation_id int primary key, 
booking_id int unique, cancellation_date timestamp default current_timestamp , 
refund_amount int, refund_status varchar(10),
foreign key (booking_id) references Bookings(booking_id)) ; 

-- Train_Tracking – Stores real-time GPS locations of trains.
-- create table Train_Tracking(tracking_id int primary key, 
-- train_id int, latitude decimal(10,2), longitude decimal(10,2), 
--  foreign key (train_id) references trains(train_id));

--   Seats – Stores seat details per train and class type.

Create table Seats (seat_id int primary key, train_id int, seat_number varchar(10), 
class varchar(10), is_reserved varchar(10));



