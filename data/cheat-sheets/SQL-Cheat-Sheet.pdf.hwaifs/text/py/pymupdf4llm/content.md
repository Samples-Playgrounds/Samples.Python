# SQL cheat sheet
## Comprehensive

### **Data Manipulation Language (DML) Commands**








|Command|Description|Syntax|Example|
|---|---|---|---|
|`SELECT`|The SELECT command retrieves<br>data from a database.|`SELECT column1, column2 FROM`<br>`table_name;`|`SELECT first_name, last_name`<br>`FROM customers;`|
|`INSERT`|The INSERT command adds new<br>records to a table.|`INSERT INTO table_name`<br>`(column1, column2) VALUES`<br>`(value1, value2);`|`INSERT INTO customers`<br>`(first_name, last_name)`<br>`VALUES ('Mary', 'Doe');`|
|`UPDATE`|The UPDATE command is used<br>to modify existing records in a<br>table.|`UPDATE table_name SET column1`<br>`= value1, column2 = value2`<br>`WHERE condition;`|`UPDATE employees SET`<br>`employee_name = ‘John Doe’,`<br>`department = ‘Marketing’;`|
|`DELETE`|The DELETE command removes<br>records from a table.|`DELETE FROM table_name WHERE`<br>`condition;`|`DELETE FROM employees WHERE`<br>`employee_name = ‘John Doe’;`|


### **Data Definition Language (DDL) Commands**














|Command|Description|Syntax|Example|
|---|---|---|---|
|`CREATE`|The CREATE command creates a<br>new database and objects, such<br>as a table, index, view, or stored<br>procedure.|`CREATE TABLE table_name`<br>`(column1 datatype1,`<br>`column2 datatype2, ...);`|`CREATE TABLE employees (`<br>`employee_id INT`<br>`PRIMARY KEY,`<br>`first_name`<br>`VARCHAR(50),`<br>`last_name`<br>`VARCHAR(50),`<br>`age INT`<br>`);`|
|`ALTER`|The ALTER command adds,<br>deletes, or modifies columns in<br>an existing table.|`ALTER TABLE table_name`<br>`ADD column_name datatype;`|`ALTER TABLE customers ADD`<br>`email VARCHAR(100);`|
|`DROP`|The DROP command is used to<br>drop an existing table in a<br>database.|`DROP TABLE table_name;`|`DROP TABLE customers;`|
|`TRUNCATE`|The TRUNCATE command is<br>used to delete the data inside a<br>table, but not the table itself.|`TRUNCATE TABLE`<br>`table_name;`|`TRUNCATE TABLE customers;`|



The SQL tool with the highest user satisfaction. `[DBVIS.COM](https://www.dbvis.com/?utm_campaign=sql-cheat-sheet)` `->`


### **Data Control Language (DCL) Commands**



|Command|Description|Syntax|Example|
|---|---|---|---|
|`GRANT`|The GRANT command is used to<br>give specific privileges to users<br>or roles.|`GRANT SELECT, INSERT ON`<br>`table_name TO user_name;`|`GRANT SELECT, INSERT ON`<br>`employees TO ‘John Doe’;`|
|`REVOKE`|The REVOKE command is used<br>to take away privileges<br>previously granted to users or<br>roles.|`REVOKE SELECT, INSERT ON`<br>`table_name FROM`<br>`user_name;`|`REVOKE SELECT, INSERT ON`<br>`employees FROM ‘John`<br>`Doe’;`|

### **Querying Data Commands**














|Command|Description|Syntax|Example|
|---|---|---|---|
|`SELECT` Statement|The SELECT statement is the<br>primary command used to<br>retrieve data from a database|`SELECT column1, column2`<br>`FROM table_name;`|`SELECT first_name,`<br>`last_name FROM customers;`|
|`WHERE` Clause|The WHERE clause is used to<br>filter rows based on a specified<br>condition.|`SELECT * FROM table_name`<br>`WHERE condition;`|`SELECT * FROM customers`<br>`WHERE age > 30;`|
|`ORDER BY` Clause|The ORDER BY clause is used to<br>sort the result set in ascending<br>or descending order based on a<br>specified column.|`SELECT * FROM table_name`<br>`ORDER BY column_name`<br>`ASC|DESC;`|`SELECT * FROM products`<br>`ORDER BY price DESC;`|
|`GROUP BY` Clause|The GROUP BY clause groups<br>rows based on the values in a<br>specified column. It is often<br>used with aggregate functions<br>like COUNT, SUM, AVG, etc.|`SELECT column_name,`<br>`COUNT(*) FROM table_name`<br>`GROUP BY column_name;`|`SELECT category, COUNT(*)`<br>`FROM products GROUP BY`<br>`category;`|
|`HAVING` Clause|The HAVING clause filters<br>grouped results based on a<br>specified condition.|`SELECT column_name,`<br>`COUNT(*) FROM table_name`<br>`GROUP BY column_name`<br>`HAVING condition;`|`SELECT category, COUNT(*)`<br>`FROM products GROUP BY`<br>`category HAVING COUNT(*)`<br>`> 5;`|



The SQL tool with the highest user satisfaction. `[DBVIS.COM](https://www.dbvis.com/?utm_campaign=sql-cheat-sheet)` `->`


|Joining Commands|Col2|Col3|Col4|
|---|---|---|---|
|**Command**|**Description**|**Syntax**|**Example**|
|`INNER JOIN`|The INNER JOIN command<br>returns rows with matching<br>values in both tables.|`SELECT * FROM table1`<br>`INNER JOIN table2 ON`<br>`table1.column =`<br>`table2.column;`|`SELECT * FROM employees`<br>`INNER JOIN departments ON`<br>`employees.department_id =`<br>`departments.id;`|
|`LEFT JOIN/LEFT OUTER JOIN`|The LEFT JOIN command<br>returns all rows from the left<br>table (first table) and the<br>matching rows from the right<br>table (second table).|`SELECT * FROM table1 LEFT`<br>`JOIN table2 ON`<br>`table1.column =`<br>`table2.column;`|`SELECT * FROM employees LEFT`<br>`JOIN departments ON`<br>`employees.department_id =`<br>`departments.id;`|
|`RIGHT JOIN/RIGHT OUTER`<br>`JOIN`|The RIGHT JOIN command<br>returns all rows from the right<br>table (second table) and the<br>matching rows from the left<br>table (first table).|`SELECT * FROM table1`<br>`RIGHT JOIN table2 ON`<br>`table1.column =`<br>`table2.column;`|`SELECT *`<br>`FROM employees`<br>`RIGHT JOIN departments`<br>`ON employees.department_id =`<br>`departments.department_id;`|
|`FULL JOIN/FULL OUTER JOIN`|The FULL JOIN command<br>returns all rows when there is a<br>match in either the left table or<br>the right table.|`SELECT * FROM table1 FULL`<br>`JOIN table2 ON`<br>`table1.column =`<br>`table2.column;`|`SELECT *`<br>`FROM employees`<br>`LEFT JOIN departments ON`<br>`employees.employee_id =`<br>`departments.employee_id`<br>`UNION`<br>`SELECT *`<br>`FROM employees`<br>`RIGHT JOIN departments ON`<br>`employees.employee_id =`<br>`departments.employee_id;`|
|`CROSS JOIN`|The CROSS JOIN command<br>combines every row from the<br>first table with every row from<br>the second table, creating a<br>Cartesian product.|`SELECT * FROM table1`<br>`CROSS JOIN table2;`|`SELECT * FROM employees`<br>`CROSS JOIN departments;`|
|`SELF JOIN`|The SELF JOIN command joins<br>a table with itself.|`SELECT * FROM table1 t1,`<br>`table1 t2 WHERE t1.column`<br>`= t2.column;`|`SELECT * FROM employees t1,`<br>`employees t2`<br>`WHERE t1.employee_id =`<br>`t2.employee_id;`|
|`NATURAL JOIN`|The NATURAL JOIN command<br>matches columns with the<br>same name in both tables.|`SELECT * FROM table1`<br>`NATURAL JOIN table2;`|`SELECT * FROM employees`<br>`NATURAL JOIN departments;`|



The SQL tool with the highest user satisfaction. `[DBVIS.COM](https://www.dbvis.com/?utm_campaign=sql-cheat-sheet)` `->`


|Subqueries in SQL|Col2|Col3|Col4|
|---|---|---|---|
|**Command**|**Description**|**Syntax**|**Example**|
|`IN`|The IN command is used to<br>determine whether a value<br>matches any value in a subquery<br>result. It is often used in the<br>WHERE clause.|`SELECT column(s) FROM`<br>`table WHERE value IN`<br>`(subquery);`|`SELECT * FROM customers`<br>`WHERE city IN (SELECT`<br>`city FROM suppliers);`|
|`ANY`|The ANY command is used to<br>compare a value to any value<br>returned by a subquery. It can<br>be used with comparison<br>operators like =, >, <, etc.|`SELECT column(s) FROM`<br>`table WHERE value < ANY`<br>`(subquery);`|`SELECT * FROM products`<br>`WHERE price < ANY (SELECT`<br>`unit_price FROM`<br>`supplier_products);`|
|`ALL`|The ALL command is used to<br>compare a value to all values<br>returned by a subquery. It can<br>be used with comparison<br>operators like =, >, <, etc.|`SELECT column(s) FROM`<br>`table WHERE value > ALL`<br>`(subquery);`|`SELECT * FROM orders`<br>`WHERE order_amount > ALL`<br>`(SELECT total_amount FROM`<br>`previous_orders);`|










|Aggregate Functions|Commands|Col3|Col4|
|---|---|---|---|
|**Command**|**Description**|**Syntax**|**Example**|
|`COUNT()`|The COUNT command counts<br>the number of rows or non-null<br>values in a specified column.|`SELECT COUNT(column_name)`<br>`FROM table_name;`|`SELECT COUNT(age) FROM`<br>`employees;`|
|`SUM()`|The SUM command is used to<br>calculate the sum of all values in<br>a specified column.|`SELECT SUM(column_name)`<br>`FROM table_name;`|`SELECT SUM(revenue) FROM`<br>`sales;`|
|`AVG()`|The AVG command is used to<br>calculate the average (mean) of<br>all values in a specified column.|`SELECT AVG(column_name)`<br>`FROM table_name;`|`SELECT AVG(price) FROM`<br>`products;`|
|`MIN()`|The MIN command returns the<br>minimum (lowest) value in a<br>specified column.|`SELECT MIN(column_name)`<br>`FROM table_name;`|`SELECT MIN(price) FROM`<br>`products;`|
|`MAX()`|The MAX command returns the<br>maximum (highest) value in a<br>specified column.|`SELECT MAX(column_name)`<br>`FROM table_name;`|`SELECT MAX(price) FROM`<br>`products;`|



The SQL tool with the highest user satisfaction. `[DBVIS.COM](https://www.dbvis.com/?utm_campaign=sql-cheat-sheet)` `->`


### **String Functions in SQL**








|Command|Description|Syntax|Example|
|---|---|---|---|
|`CONCAT()`|The CONCAT command<br>concatenates two or more<br>strings into a single string.|`SELECT CONCAT(string1,`<br>`string2, ...) AS`<br>`concatenated_string FROM`<br>`table_name;`|`SELECT CONCAT(first_name,`<br>`' ', last_name) AS`<br>`full_name FROM employees;`|
|`SUBSTRING()/SUBSTR()`|The SUBSTRING command<br>extracts a substring from a<br>string.|`SELECT SUBSTRING(string`<br>`FROM start_position [FOR`<br>`length]) AS substring`<br>`FROM table_name;`|`SELECT`<br>`SUBSTRING(product_name`<br>`FROM 1 FOR 5) AS`<br>`substring FROM products;`|
|`CHAR_LENGTH()/LENGTH()`|The LENGTH command returns<br>the length (number of<br>characters) of a string.|`SELECT`<br>`CHAR_LENGTH(string) AS`<br>`length FROM table_name;`|`SELECT`<br>`CHAR_LENGTH(product_name)`<br>`AS length FROM products;`|
|`UPPER()`|The UPPER command converts<br>all characters in a string to<br>uppercase.|`SELECT UPPER(string) AS`<br>`uppercase_string FROM`<br>`table_name;`|`SELECT UPPER(first_name)`<br>`AS uppercase_first_name`<br>`FROM employees;`|
|`LOWER()`|The LOWER command converts<br>all characters in a string to<br>lowercase.|`SELECT LOWER(string) AS`<br>`lowercase_string FROM`<br>`table_name;`|`SELECT LOWER(last_name)`<br>`AS lowercase_last_name`<br>`FROM employees;`|
|`TRIM()`|The TRIM command removes<br>specified prefixes or suffixes (or<br>whitespace by default) from a<br>string.|`SELECT TRIM([LEADING |`<br>`TRAILING | BOTH]`<br>`characters FROM string)`<br>`AS trimmed_string FROM`<br>`table_name;`|`SELECT TRIM(TRAILING ' '`<br>`FROM full_name) AS`<br>`trimmed_full_name FROM`<br>`customers;`|
|`LEFT()`|The LEFT command returns a<br>specified number of characters<br>from the left of a string.|`SELECT LEFT(string,`<br>`num_characters) AS`<br>`left_string FROM`<br>`table_name;`|`SELECT`<br>`LEFT(product_name, 5)`<br>`AS left_product_name`<br>`FROM products;`|
|`RIGHT()`|The RIGHT command returns a<br>specified number of characters<br>from the right of a string.|`SELECT RIGHT(string,`<br>`num_characters) AS`<br>`right_string FROM`<br>`table_name;`|`SELECT`<br>`RIGHT(order_number, 4) AS`<br>`right_order_number FROM`<br>`orders;`|
|`REPLACE()`|The REPLACE command<br>replaces occurrences of a<br>substring within a string.|`SELECT REPLACE(string,`<br>`old_substring,`<br>`new_substring) AS`<br>`replaced_string FROM`<br>`table_name;`|`SELECT`<br>`REPLACE(description,`<br>`'old_string',`<br>`'new_string') AS`<br>`replaced_description FROM`<br>`product_descriptions;`|



The SQL tool with the highest user satisfaction. `[DBVIS.COM](https://www.dbvis.com/?utm_campaign=sql-cheat-sheet)` `->`


### **Date and Time SQL Commands**








|Command|Description|Syntax|Example|
|---|---|---|---|
|`CURRENT_DATE()`|The CURRENT_DATE command<br>returns the current date.|`SELECT CURRENT_DATE() AS`<br>`current_date;`|`<-`|
|`CURRENT_TIME()`|The CURRENT_TIME command<br>returns the current time.|`SELECT CURRENT_TIME() AS`<br>`current_time;`|`<-`|
|`CURRENT_TIMESTAMP()`|The CURRENT_TIMESTAMP<br>command returns the current<br>date and time.|`SELECT`<br>`CURRENT_TIMESTAMP() AS`<br>`current_timestamp;`|`<-`|
|`DATE_PART()`|The DATE_PART command<br>extracts a specific part (e.g.,<br>year, month, day) from a date or<br>time.|`SELECT DATE_PART('part',`<br>`date_expression) AS`<br>`extracted_part;`|`SELECT DATE_PART('year',`<br>`'2024-04-11') AS`<br>`extracted_part;`|
|`DATE_ADD()/DATE_SUB()`|The DATE_ADD command adds<br>or subtracts a specified number<br>of days, months, or years<br>to/from a date.|`SELECT`<br>`DATE_ADD(date_expression,`<br>`INTERVAL value unit) AS`<br>`new_date;`|`-- DATE_ADD Example`<br>`SELECT`<br>`DATE_ADD('2024-04-11',`<br>`INTERVAL 1 DAY) AS`<br>`new_date;`<br>`-- DATE_SUB Example`<br>`SELECT`<br>`DATE_SUB('2024-04-11',`<br>`INTERVAL 1 DAY) AS`<br>`new_date;`|
|`EXTRACT()`|The EXTRACT command<br>extracts a specific part (e.g.,<br>year, month, day) from a date or<br>time.|`SELECT EXTRACT(part FROM`<br>`date_expression) AS`<br>`extracted_part;`|`SELECT EXTRACT(YEAR FROM`<br>`'2024-04-11') AS`<br>`extracted_part;`|
|`TO_CHAR()`|The TO_CHAR command<br>converts a date or time to a<br>specified format.|`SELECT`<br>`TO_CHAR(date_expression,`<br>`'format') AS`<br>`formatted_date;`|`SELECT`<br>`TO_CHAR('2024-04-11',`<br>`'YYYY-MM-DD') AS`<br>`formatted_date;`|
|`TIMESTAMPDIFF()`|The TIMESTAMPDIFF command<br>calculates the difference<br>between two timestamps in a<br>specified unit (e.g., days, hours,<br>minutes).|`SELECT`<br>`TIMESTAMPDIFF(unit,`<br>`timestamp1, timestamp2)`<br>`AS difference;`|`SELECT TIMESTAMPDIFF(DAY,`<br>`'2024-04-10',`<br>`'2024-04-11') AS`<br>`difference;`|
|`DATEDIFF()`|The DATEDIFF command<br>calculates the difference in days<br>between two dates.|`SELECT DATEDIFF(date1,`<br>`date2) AS`<br>`difference_in_days;`|`SELECT`<br>`DATEDIFF('2024-04-11',`<br>`'2024-04-10') AS`<br>`difference_in_days;`|



The SQL tool with the highest user satisfaction. `[DBVIS.COM](https://www.dbvis.com/?utm_campaign=sql-cheat-sheet)` `->`


### **Conditional Expressions**








|Command|Description|Syntax|Example|
|---|---|---|---|
|`CASE Statement`|The CASE statement allows you<br>to perform conditional logic<br>within a query.|`SELECT`<br>`column1,`<br>`column2,`<br>`CASE`<br>`WHEN condition1`<br>`THEN result1`<br>`WHEN condition2`<br>`THEN result2`<br>`ELSE`<br>`default_result`<br>`END AS alias`<br>`FROM table_name;`|`SELECT`<br>`order_id,`<br>`total_amount,`<br>`CASE`<br>`WHEN total_amount`<br>`> 1000 THEN 'High Value`<br>`Order'`<br>`WHEN total_amount`<br>`> 500 THEN 'Medium Value`<br>`Order'`<br>`ELSE 'Low Value`<br>`Order'`<br>`END AS order_status`<br>`FROM orders;`|
|`IF() Function`|The IF() function evaluates a<br>condition and returns a value<br>based on the evaluation.|`SELECT IF(condition,`<br>`true_value, false_value)`<br>`AS alias FROM table_name;`|`SELECT`<br>`name,`<br>`age,`<br>`IF(age > 50,`<br>`'Senior', 'Junior') AS`<br>`employee_category`<br>`FROM employees;`|
|`COALESCE() Function`|The COALESCE() function<br>returns the first non-null value<br>from a list of values.|`SELECT COALESCE(value1,`<br>`value2, ...) AS alias`<br>`FROM table_name;`|`SELECT`<br>`COALESCE(first_name,`<br>`middle_name) AS`<br>`preferred_name`<br>`FROM employees;`|
|`NULLIF() Function`|The NULLIF() function returns<br>null if two specified expressions<br>are equal.|`SELECT`<br>`NULLIF(expression1,`<br>`expression2) AS alias`<br>`FROM table_name;`|`SELECT`<br>`NULLIF(total_amount,`<br>`discounted_amount) AS`<br>`diff_amount FROM orders;`|



The SQL tool with the highest user satisfaction. `[DBVIS.COM](https://www.dbvis.com/?utm_campaign=sql-cheat-sheet)` `->`


### **Set Operations**



|Command|Description|Syntax|Example|
|---|---|---|---|
|`UNION`|The UNION operator<br>combines the result sets of<br>two or more SELECT<br>statements into a single<br>result set.|`SELECT column1, column2 FROM`<br>`table1`<br>`UNION`<br>`SELECT column1, column2 FROM`<br>`table2;`|`SELECT first_name, last_name`<br>`FROM customers`<br>`UNION`<br>`SELECT first_name, last_name`<br>`FROM employees;`|
|`INTERSECT`|The INTERSECT operator<br>returns the common rows<br>that appear in both result<br>sets.|`SELECT column1, column2 FROM`<br>`table1`<br>`INTERSECT`<br>`SELECT column1, column2 FROM`<br>`table2;`|`SELECT first_name, last_name`<br>`FROM customers`<br>`INTERSECT`<br>`SELECT first_name, last_name`<br>`FROM employees;`|
|`EXCEPT`|The EXCEPT operator<br>returns the distinct rows<br>from the left result set that<br>are not present in the right<br>result set.|`SELECT column1, column2 FROM`<br>`table1`<br>`EXCEPT`<br>`SELECT column1, column2 FROM`<br>`table2;`|`SELECT first_name, last_name`<br>`FROM customers`<br>`EXCEPT`<br>`SELECT first_name, last_name`<br>`FROM employees;`|

### **Transaction Control Commands**












|Command|Description|Syntax|Example|
|---|---|---|---|
|`COMMIT`|The COMMIT command is<br>used to save all the changes<br>made during the current<br>transaction and make them<br>permanent.|`COMMIT;`|`BEGIN TRANSACTION;`<br>`-- SQL statements and changes within the transaction`<br>`INSERT INTO employees (name, age) VALUES ('Alice',`<br>`30);`<br>`UPDATE products SET price = 25.00 WHERE category =`<br>`'Electronics';`<br>`COMMIT;`|
|`ROLLBACK`|The ROLLBACK command is<br>used to undo all the<br>changes made during the<br>current transaction and<br>discard them.|`ROLLBACK;`|`BEGIN TRANSACTION;`<br>`-- SQL statements and changes within the transaction`<br>`INSERT INTO employees (name, age) VALUES ('Bob', 35);`<br>`UPDATE products SET price = 30.00 WHERE category =`<br>`'Electronics';`<br>`ROLLBACK;`|



The SQL tool with the highest user satisfaction. `[DBVIS.COM](https://www.dbvis.com/?utm_campaign=sql-cheat-sheet)` `->`


|SAVEPOINT|The SAVEPOINT command<br>is used to set a point within<br>a transaction to which you<br>can later roll back.|SAVEPOINT<br>savepoint_n<br>ame;|BEGIN TRANSACTION;<br>INSERT INTO employees (name, age) VALUES ('Carol',<br>28);<br>SAVEPOINT before_update;<br>UPDATE products SET price = 40.00 WHERE category =<br>'Electronics';<br>SAVEPOINT after_update;<br>DELETE FROM customers WHERE age > 60;<br>ROLLBACK TO before_update;<br>-- At this point, the DELETE is rolled back, but the<br>UPDATE remains.<br>COMMIT;|
|---|---|---|---|
|`ROLLBACK TO`<br>`SAVEPOINT`|The ROLLBACK TO<br>SAVEPOINT command is<br>used to roll back to a<br>specific savepoint within a<br>transaction.|`ROLLBACK TO`<br>`SAVEPOINT`<br>`savepoint_n`<br>`ame;`|`BEGIN TRANSACTION;`<br>`INSERT INTO employees (name, age) VALUES ('David',`<br>`42);`<br>`SAVEPOINT before_update;`<br>`UPDATE products SET price = 50.00 WHERE category =`<br>`'Electronics';`<br>`SAVEPOINT after_update;`<br>`DELETE FROM customers WHERE age > 60;`<br>`-- Rollback to the savepoint before the update`<br>`ROLLBACK TO SAVEPOINT before_update;`<br>`-- At this point, the UPDATE is rolled back, but the`<br>`INSERT remains.`<br>`COMMIT;`|
|`SET TRANSACTION`|The SET TRANSACTION<br>command is used to<br>configure properties for the<br>current transaction, such as<br>isolation level and<br>transaction mode.|`SET`<br>`TRANSACTION`<br>`[ISOLATION`<br>`LEVEL {`<br>`READ`<br>`COMMITTED |`<br>`SERIALIZABL`<br>`E }]`|`BEGIN TRANSACTION;`<br>`-- Set the isolation level to READ COMMITTED`<br>`SET TRANSACTION ISOLATION LEVEL READ COMMITTED;`<br>`-- SQL statements and changes within the transaction`<br>`INSERT INTO employees (name, age) VALUES ('Emily',`<br>`35);`<br>`UPDATE products SET price = 60.00 WHERE category =`<br>`'Electronics';`<br>`COMMIT;`|



The SQL tool with the highest user satisfaction. `[DBVIS.COM](https://www.dbvis.com/?utm_campaign=sql-cheat-sheet)` `->`


