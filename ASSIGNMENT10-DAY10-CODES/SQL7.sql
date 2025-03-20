-- Show Consistency by enforcing a foreign key constraint within a 
-- transaction and ensuring the rollback happens if the constraint fails.

BEGIN;

-- Create Parent and Child tables
CREATE TABLE parent_table (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE child_tablee (
    id INT PRIMARY KEY,
    parent_id INT,
    name VARCHAR(255),
    FOREIGN KEY (parent_id) REFERENCES parent_table(id)
);

-- Insert a record into the parent table
INSERT INTO parent_table (id, name) VALUES (1, 'Parent 1');


INSERT INTO child_tablee (id, parent_id, name) VALUES (1, 1, 'Child record for Parent 1');


INSERT INTO child_tablee (id, parent_id,name) VALUES (2, 999, 'Child record for a non-existing Parent');

-- Since the foreign key constraint fails, the transaction will be rolled back, keeping the database consistent
ROLLBACK;
