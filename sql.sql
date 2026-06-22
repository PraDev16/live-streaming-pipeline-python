select*from production.brands;
select*from production.categories;
select*from production.products;
select*from production.stocks;
select*from sales.customers;
select*from sales.order_items;
select*from sales.orders;
select*from sales.staffs;
select*from sales.stores;

SELECT @@SERVERNAME;

CREATE TABLE stream_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    last_updated DATETIME DEFAULT GETDATE()
);

SELECT * FROM stream_products;