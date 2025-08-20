-- Top 5 Customers by Spend
SELECT 
    c.customer_id,
    SUM(s.total_amount) AS total_spend
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_spend DESC
LIMIT 5;
