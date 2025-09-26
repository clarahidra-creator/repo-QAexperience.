-- Reconciliation: staging vs warehouse
WITH s AS (
  SELECT order_id, CAST(order_date AS date) AS order_date, amount FROM etl_staging_orders
),
w AS (
  SELECT order_id, CAST(order_date AS date) AS order_date, amount_usd AS amount FROM dwh_fact_orders
)
SELECT
  'missing_in_warehouse' AS issue,
  s.order_id, s.order_date, s.amount
FROM s LEFT JOIN w ON s.order_id = w.order_id
WHERE w.order_id IS NULL

UNION ALL

SELECT
  'mismatched_total' AS issue,
  s.order_id, s.order_date, s.amount
FROM s JOIN w ON s.order_id = w.order_id
WHERE ABS(s.amount - w.amount) > 0.01;

-- Quality gates
-- 1) PK uniqueness
SELECT order_id, COUNT(*) c FROM etl_staging_orders GROUP BY order_id HAVING COUNT(*) > 1;
-- 2) Non-null criticals
SELECT * FROM etl_staging_orders WHERE order_id IS NULL OR order_date IS NULL OR amount IS NULL;
-- 3) Date sanity
SELECT * FROM etl_staging_orders WHERE order_date > GETDATE();