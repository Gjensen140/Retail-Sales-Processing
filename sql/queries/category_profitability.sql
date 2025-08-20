-- Product Category Profitability (total revenue - cost)

SELECT 
    p.category,
    SUM(s.total_amount) AS total_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
