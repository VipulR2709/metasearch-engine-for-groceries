# Target

CREATE TABLE `target_products_details` (
  `product_id` text,
  `product_title` text,
  `product_url` text,
  `vendor_ids` text,
  `oos_all_store` text,
  `shipping_min_date` text,
  `shipping_max_date` text,
  `two_days_shipping_availability` text,
  `store_ids` int DEFAULT NULL,
  `pickup_date` text,
  `delivery_availability` text
);

CREATE TABLE `target_products_pricing` (
  `product_title` text,
  `price` double DEFAULT NULL
);


CREATE TABLE `target_store_name_mapping` (
  `store_ids` int DEFAULT NULL,
  `store_names` text
) ;


#Walgreens:

CREATE TABLE `walgreens_products_details` (
`product_title` VARCHAR(100),
`availability_list` VARCHAR(100),
`ratings_list` double DEFAULT NULL,
`product_url` VARCHAR(200),
`packet_size_list` VARCHAR(100),
`prod_type_list` VARCHAR(100),
`packet_size_unit_list` VARCHAR(100),
`product_ids` VARCHAR(100),
PRIMARY KEY (product_ids),
CONSTRAINT FK_product_title FOREIGN KEY (product_title) REFERENCES walgreens_products_details(product_ids)
) ;

CREATE TABLE `walgreens_products_pricing` (
`product_title` VARCHAR(100),
`price` VARCHAR(100),
PRIMARY KEY(product_title),
CONSTRAINT FK_product_title FOREIGN KEY (product_title) REFERENCES walgreens_products_details(product_ids)
)

# Star Market:

CREATE TABLE `starmarket_products_details` (
`product_ids` VARCHAR(100),
`product_title` VARCHAR(100), 
`delivery_availability_list` VARCHAR(100),
`ratings_list` int DEFAULT NULL,
`packet_size_unit_list` VARCHAR(100), 
`prod_type_list` VARCHAR(100),
`inStore_availability_list` BOOLEAN, 
`pickup_availability_list` VARCHAR(100),
PRIMARY KEY (product_ids),
CONSTRAINT FK_product_title FOREIGN KEY (product_title) REFERENCES starmarket_products_details(Product_ID)
);

CREATE TABLE `starmarket_products_pricing` (
`product_title` VARCHAR(100),
`price` double DEFAULT NULL,
CONSTRAINT FK_product_title FOREIGN KEY (product_title) REFERENCES starmarket_products_details(product_ids)
);

# Traderjoes:

CREATE TABLE `traderjoes_products_details` (
`product_title` VARCHAR(100),
`availability_list` VARCHAR(100),
`product_url` VARCHAR(100),
`packet_size_list` double DEFAULT NULL,
`packet_size_unit_list` VARCHAR(100),
`product_ids` VARCHAR(100),
`ingredient_list` VARCHAR(100),
PRIMARY KEY(product_title),
CONSTRAINT FK_product_title FOREIGN KEY (product_title) REFERENCES traderjoes_products_details(product_ids)
) ;

CREATE TABLE `traderjoes_products_pricing` (
`product_title` VARCHAR(100),
`price` double DEFAULT NULL,
CONSTRAINT FK_product_title FOREIGN KEY (product_title) REFERENCES traderjoes_products_details(product_ids)
);

# Walmart: 

CREATE TABLE `walmart_products_details` (
  `PRODUCT_URL` text,
  `PRODUCT_SIZE` double DEFAULT NULL,
  `product_title` text,
  `CATEGORY` text,
  `BRAND` text,
  `product_ids` text
) ;

CREATE TABLE `walmart_category_mapping` (
  `DEPARTMENT` text,
  `CATEGORY` text
) ;

CREATE TABLE `walmart_products_pricing` (
  `product_title` text,
  `price` double DEFAULT NULL
) ;


# Mega_Store
CREATE TABLE `mega_store_data_final` (
`product_title` VARCHAR(100),
`availability_list` VARCHAR(100),
`product_url` VARCHAR(200),
`product_ids` VARCHAR(100),
`price` double DEFAULT NULL,
`Store` VARCHAR(100),
PRIMARY KEY (product_ids)
) ;
