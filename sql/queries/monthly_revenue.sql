-- Monthly Revenue Trends
SELECT 
    DATE_TRUNC('month', date) AS month,
    SUM(total_amount) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;
