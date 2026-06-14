-- Basic SELECT
SELECT name, email FROM users;

-- Filter with WHERE
SELECT * FROM users WHERE user_id > 5;

-- Aggregation with GROUP BY
SELECT users.name,
       COUNT(orders.order_id) as total_orders,
       COALESCE(SUM(orders.amount), 0) as total_spent
FROM users
LEFT JOIN orders ON users.user_id = orders.user_id
GROUP BY users.name
HAVING total_spent > 0
ORDER BY total_spent DESC;

-- Window Function
SELECT 
    users.name,
    orders.amount,
    SUM(orders.amount) OVER() as grand_total,
    ROUND(orders.amount * 100.0 / SUM(orders.amount) OVER(), 2) as percentage
FROM users
INNER JOIN orders ON users.user_id = orders.user_id;
