-- Optimize a physical schema by adding necessary indexes and
--  partitions for a customer database with millions of records. ,MNAUAL-=-
-- CREATE TABLE employ (
--     id INT NOT NULL,
--     fname VARCHAR(30),
--     lname VARCHAR(30),
--     hired DATE NOT NULL DEFAULT '1970-01-01',
--     separated DATE NOT NULL DEFAULT '9999-12-31',
--     job_code INT NOT NULL,
--     store_id INT NOT NULL
-- )
-- PARTITION BY RANGE (store_id) (
--     PARTITION p0 VALUES LESS THAN (6),
--     PARTITION p1 VALUES LESS THAN (11),
--     PARTITION p2 VALUES LESS THAN (16),
--     PARTITION p3 VALUES LESS THAN (21)
-- );