USE my_guitar_shop;

CREATE OR REPLACE VIEW v_all_products AS
SELECT product_name, list_price, discount_percent
FROM products;

CREATE OR REPLACE VIEW v_customers_ca AS
SELECT c.first_name, c.last_name, c.email_address
FROM customers c
JOIN addresses a ON c.customer_id = a.customer_id
WHERE a.state = 'CA';

CREATE OR REPLACE VIEW v_categories AS
SELECT category_id, category_name
FROM categories;

CREATE OR REPLACE VIEW v_orders_customer AS
SELECT o.order_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_name, o.order_date
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;

CREATE OR REPLACE VIEW v_order_items_details AS
SELECT o.order_id, p.product_name, oi.quantity
FROM order_items oi
INNER JOIN orders o ON oi.order_id = o.order_id
INNER JOIN products p ON oi.product_id = p.product_id;

CREATE OR REPLACE VIEW v_products_with_category AS
SELECT p.product_name, c.category_name
FROM products p
INNER JOIN categories c ON p.category_id = c.category_id;

CREATE OR REPLACE VIEW v_customers_shipping_addresses AS
SELECT c.first_name, c.last_name, a.line1, a.city, a.state
FROM customers c
INNER JOIN addresses a ON c.shipping_address_id = a.address_id;

CREATE OR REPLACE VIEW v_administrators AS
SELECT first_name, last_name, email_address
FROM administrators;

CREATE OR REPLACE VIEW v_total_sales_per_customer AS
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       SUM(oi.item_price * oi.quantity) AS total_spent
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.customer_id;

CREATE OR REPLACE VIEW v_avg_product_price_per_category AS
SELECT c.category_name, AVG(p.list_price) AS avg_price
FROM categories c
INNER JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_id;

CREATE OR REPLACE VIEW v_order_count_per_customer AS
SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
       COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

CREATE OR REPLACE VIEW v_high_low_priced_products AS
SELECT MAX(list_price) AS highest_price, MIN(list_price) AS lowest_price
FROM products;

CREATE OR REPLACE VIEW v_product_count_per_category AS
SELECT c.category_name, COUNT(p.product_id) AS product_count
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id
GROUP BY c.category_id;
