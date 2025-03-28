-- 4. Indexing & Performance Optimization
-- Create an index on the train_id column in Bookings to speed up searches.


create index train_id_index on trains (train_id);