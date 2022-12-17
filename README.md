# Meta-Search Engine for Groceries/Food/Household Items

A platform to check and compare grocery prices from different retailers


#### Background

The idea behind this project occurs from the rising price variety of different food and grocery items across supermarkets. As international students, we have experienced this issue and understand the hassle that one has to go through, in order to find the cheapest grocery items. Hence, comes the need for a database that can be used as a single source of information to take cost-effective decisions.

#### Objective
The goal was to create a database that will have the following information about multiple foods and grocery items:

•	Product Information (Category, sub-category, etc.)

•	Product availability at different retail stores

•	Price at different stores

•	Stores available within a specific area

•	Substitutes for the required product

#### Entity-Relationship Diagram

![image](https://user-images.githubusercontent.com/114368590/208225373-b27d2faf-5ea7-4a58-bfd8-a9c0959bf078.png)

#### Final Database
![image](https://user-images.githubusercontent.com/114368590/208225402-fb25359c-2be5-41a7-93fd-4b2aaf004da2.png)
![image](https://user-images.githubusercontent.com/114368590/208225410-8368afb3-c532-43ee-b17f-c38703f88526.png)

The final database contains tables and views as mentioned in the above screenshots.
The Mega Store table can be used to determine the cheapest option available.

![image](https://user-images.githubusercontent.com/114368590/208225579-9c230d38-caf6-473b-943b-78476da3521a.png)


#### Major Use-cases

A few major user questions that can be answered from the database are as follow:

1.	Use Case: Types of availability for fruits and vegetables
Description: User should be able to view availability for fruits and vegetables
Actor: User
Precondition: User should have selected fruits and fresh foods category
Steps:
Actor action: User should be able to view availability for the selected category
System Responses: Displays the modes of availability for selected category on screen
Post Conditions: User can see a list of products within the selected category

##### SQL Query: 
CREATE VIEW categorycheck AS
SELECT a.product_title,a.prod_type_list,b.price, a.pickup_eligibility_list,a.delivery_eligibility_list,a.instore_eligibility_list
FROM starmarket_products_details AS a
INNER JOIN starmarket_products_pricing AS b
ON a.product_title = b.product_title
WHERE a.prod_type_list LIKE '%Fruits & Vegetables%' AND ( a.pickup_eligibility_list OR a.delivery_eligibility_list OR a.instore_eligibility_list) = 'TRUE'
ORDER BY price;

![image](https://user-images.githubusercontent.com/114368590/208225638-31b5351a-e91c-45e5-8738-49a2e851a9d8.png)

2.	Use Case: Cheapest coffee available at any store
Description: User should be able to view cheapest coffee
Actor: User
Precondition: User should know coffee category
Steps:
Actor action: User should be able to view the cheapest coffee available 
System Responses: Displays the cheapest coffee
Post Conditions: User can see a list of coffee with the cheapest coffee on top

##### SQL Query:
CREATE VIEW coffee AS
SELECT product_title, Store, price
FROM mega_store_data_final
WHERE product_title
LIKE "%coffee%"
ORDER BY price LIMIT 2;

![image](https://user-images.githubusercontent.com/114368590/208225648-8715883b-dc05-4022-b8e8-02886bf689bd.png)

3.	Use Case: Cheapest coffee available at any store
Description: User should be able to view cheapest coffee
Actor: User
Precondition: User should coffee category
Steps:
Actor action: User should be able to view the cheapest coffee available 
System Responses: Displays the cheapest coffee
Post Conditions: User can see a list of coffee with the cheapest coffee on top
 
##### SQL Query:
CREATE VIEW milk AS
SELECT product_title, Store, price
FROM mega_store_data_final
WHERE product_title
LIKE "%milk%"
ORDER BY price
LIMIT 2;

4.	Use Case: Stores with Bananas in stock
Description: User should be able to see all the stores with bananas in stock
Actor: User
Precondition: User must have entered into fruits and fresh foods category
Steps:
Actor action: User views stores with various banana types
System Responses: Displays bananas that are in stock at stores
Post Condition: User can view all the stores in which bananas are in stock

##### SQL Query:
CREATE VIEW banana AS
SELECT product_title, Store, price
FROM mega_store_data_final
WHERE product_title
LIKE "%banana%" AND availability_list = "IN_STOCK" ORDER BY price ;

![image](https://user-images.githubusercontent.com/114368590/208225656-d851fccf-977a-4de6-8f59-d18a567fe54a.png)
	 
5.	Use Case: Availability of eggs in Megastore
Description: User should be able to see availability of eggs
Actor: User
Precondition: User must have selected dairy and poultry category
Steps:
Actor action: User views eggs of various protein types at megastore
System Responses: Displays price, title and protein types of eggs
Post Condition: User can view multiple eggs 
 
##### SQL Query:
CREATE VIEW egg AS
SELECT product_title, Store, price
FROM mega_store_data_final
WHERE product_title
LIKE "%egg%"
ORDER BY price
LIMIT 2;

6.	Checking all cheese products with ratings more than 3 at Walgreens and having price less than $5

##### SQL Query:
CREATE VIEW walgreenscheese AS
SELECT DISTINCT(a.product_title),a.ratings_list,b.price,a.product_ids
FROM walgreens_products_details as a
JOIN walgreens_products_pricing as b
ON a.product_title = b.product_title
WHERE a.ratings_list >3 and b.product_title LIKE "%cheese%" AND b.price < 5;

![image](https://user-images.githubusercontent.com/114368590/208225659-67d7a9d9-3432-40a3-88aa-3c8fe12cf6f0.png)

 

7.	Use Case: Products with ratings greater than 3 at walgreens
	Description: User should select walgreens as store and filter it by products with rating greater than 3
	Actor: User
	Precondition: Walgreens should be selected as store
	Steps:
	Actor action: User will select walgreens as store and select filter by ratings more than 3
	System Responses: If the customer can see products with ratings more than 3
	Post Conditions: User can see all the products with multiple category and variety with ratings greater than 3
	
	##### SQL Query:
	CREATE VIEW ratings AS
	SELECT DISTINCT(a.product_title),a.ratings_list,b.price,a.product_ids
	FROM walgreens_products_details as a
	JOIN walgreens_products_pricing as b
	ON a.product_title = b.product_title WHERE a.ratings_list >3
	ORDER by ratings_list; 
  
  ![image](https://user-images.githubusercontent.com/114368590/208225665-9f69cead-0f77-4c86-baf0-69ca98d5c61c.png)


#### Steps performed to get the final database
1.	Web scraping from different stores’ websites
2.	Data cleaning and munging
3.	Checking normalization forms and data processing
##### Data Sources
Fetched data from: Star Market, Target, Walgreens and Trader Joes
Reference Links - 
1.	https://www.target.com           
2.	https://www.starmarket.com
3.	https://www.walgreens.com
4.	https://www.traderjoes.com
5.	https://www.kaggle.com/

![image](https://user-images.githubusercontent.com/114368590/208225719-8dfba9c6-b84a-4366-8457-7cb628e1aeb9.png)
![image](https://user-images.githubusercontent.com/114368590/208225732-d62d1ae1-9ba0-426a-bc9c-c8b1b644203e.png)

We fetched the URL responses and converted those JSONs into data frames and eventually into csv datafiles/tables. Above is the screenshot of sample function used to convert JSON into python dictionary with required keys.

##### Audit Validity and Data Cleaning:

Checking count of null values in all columns

![image](https://user-images.githubusercontent.com/114368590/208225742-dbc2667a-a442-4470-ba4e-fed466b73947.png)

Checking anomalies in price column

![image](https://user-images.githubusercontent.com/114368590/208225755-74a30b63-5d06-4af2-9713-90782940f466.png)

 
Checking possibilities for null values and filling appropriate values
![image](https://user-images.githubusercontent.com/114368590/208225764-07abe9df-3894-4ded-b56e-2d36a197c214.png)

 
Filling null values in rating field with average ratings
![image](https://user-images.githubusercontent.com/114368590/208225771-094e3b11-0548-408b-9db3-ca178809b07d.png)

 
#### Conclusion
The final created database can be widely used by all types user to decide where to buy items from. This will help users to save their time as well hard-earned money.

#### Contributors
1.	Vipul Rajderkar (rajderkar.v@northeastern.edu, 002700991)
2.	Raj Sarode (sarode.r@northeastern.edu, 002762015)
3.	Tanmay Zope	(zope.t@northeastern.edu, 002767087)
