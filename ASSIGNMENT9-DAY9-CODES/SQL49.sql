# 49.	Implement a transaction in SQL to update customer information and log the changes in an audit table for tracking purposes.


CREATE TABLE trigger_table (
    name VARCHAR(10)
);

CREATE TABLE second_table (
    name VARCHAR(10)
);
INSERT INTO trigger_table (name) VALUES ('John');


DELIMITER //
CREATE TRIGGER after_insert_trigger
AFTER INSERT ON trigger_table
FOR EACH ROW


BEGIN
    INSERT INTO second_table (name) VALUES (NEW.name);
END //
DELIMITER ;
SELECT * FROM second_table;
