# Write an SQL query to find the average order amount for each month in the past year.
CREATE TABLE orderss_month (
    order_id INT PRIMARY KEY,
    order_date DATE,
    order_amount INT);
INSERT INTO orderss_month  VALUES
(1,  '2023-01-15', 2000),
(2,  '2023-02-10', 3000),
(3,  '2023-03-05', 1500),
(4,  '2023-04-20', 2500),
(5,  '2023-05-10', 3500),
(6,  '2023-06-15', 5000),
(7,  '2023-07-10', 4000),
(8,  '2023-08-05', 4500),
(9,  '2023-09-20', 3000),
(10,  '2023-10-10', 6000),
(11,  '2023-11-15', 2500),
(12, '2023-12-05', 5500);


SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    AVG(order_amount) AS avg_order_amount
FROM
    orderss_month
WHERE
    order_date >= CURDATE() - INTERVAL 1 YEAR
GROUP BY
    YEAR(order_date),
    MONTH(order_date)
ORDER BY
    year DESC, month DESC;
