USE shopping_db;
-- REVENUE GENRATED BY GENDER
SELECT gender,SUM(purchase_amount) as revenue 
FROM customer_shopping_behavior
GROUP BY gender;

-- customer use a discount but still spent more than average purchase amount
SELECT customer_id,purchase_amount
from customer_shopping_behavior 
WHERE discount_applied='YES' and purchase_amount>=(SELECT AVG(purchase_amount) from customer_shopping_behavior);

-- top 5 products with the highest average review rating
SELECT item_purchased,ROUND(AVG(review_rating),2) as 'average product rating'
FROM customer_shopping_behavior
group by item_purchased
order by AVG(review_rating) desc
limit 5;

-- COMPARE AVG PURCHASE AMOUNTS BTW STD AND SHIPPING
select shipping_type,ROUND(avg(purchase_amount),2)
from customer_shopping_behavior
where shipping_type in ('Standard','Express')
group by shipping_type;

select subscription_status,count(customer_id) as total_customers,
ROUND(AVG(purchase_amount),2) AS avg_spend,
ROUND(SUM(purchase_amount),2) as total_revenue
from customer_shopping_behavior
group by subscription_status 
order by total_revenue,avg_spend desc;

--
