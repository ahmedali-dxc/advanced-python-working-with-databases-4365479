CREATE DATABASE red30;

CREATE TABLE Sales (
    order_num INT(11) NOT NULL AUTO_INCREMENT,
    cust_name VARCHAR(255) NOT NULL,
    prod_number VARCHAR(255) NOT NULL,
    prod_name VARCHAR(255) NOT NULL,
    quantity INT(11) NOT NULL,
    price DECIMAL(6, 2) NOT NULL,
    discount DECIMAL(4, 2) NOT NULL,
    order_total DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (order_num)
);