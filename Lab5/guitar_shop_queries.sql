USE my_guitar_shop;

-- Simple Single Table Queries
-- 1. List all products with their price and discount
SELECT product_name, list_price, discount_percent
FROM products;

-- 2. Find all customers from California (CA)
SELECT first_name, last_name, email_address
FROM customers c
JOIN addresses a ON c.customer_id = a.customer_id
WHERE a.state = 'CA';

-- 3. Show all categories available
SELECT category_id, category_name
FROM categories;

-- Queries with Inner Joins
-- 4. List all orders with customer names and order dates
SELECT o.order_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;

-- 5. Get each order’s items with product names and quantities
SELECT o.order_id, p.product_name, oi.quantity
FROM order_items oi
INNER JOIN orders o ON oi.order_id = o.order_id
INNER JOIN products p ON oi.product_id = p.product_id;

-- 6. List products with their category name
SELECT p.product_name, c.category_name
FROM products p
INNER JOIN categories c ON p.category_id = c.category_id;

-- 7. Find customers with their shipping addresses
SELECT c.first_name, c.last_name, a.line1, a.city, a.state
FROM customers c
INNER JOIN addresses a ON c.shipping_address_id = a.address_id;

-- 8. Show administrators with their emails
SELECT first_name, last_name, email_address
FROM administrators;

-- Queries with Functions or GROUP BY
-- 9. Find total sales (sum of item_price * quantity) per customer
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       SUM(oi.item_price * oi.quantity) AS total_spent
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.customer_id;

-- 10. Find average product price per category
SELECT c.category_name, AVG(p.list_price) AS avg_price
FROM categories c
INNER JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_id;

-- 11. Count how many orders each customer has placed
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

-- 12. Find highest and lowest priced product
SELECT MAX(list_price) AS highest_price, MIN(list_price) AS lowest_price
FROM products;

-- 13. Get number of products per category
SELECT c.category_name, COUNT(p.product_id) AS product_count
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_id;
