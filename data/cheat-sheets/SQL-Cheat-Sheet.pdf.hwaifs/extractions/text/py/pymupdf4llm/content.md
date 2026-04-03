## SQL cheat sheet 

## Comprehensive 

## **Data Manipulation Language �DML�Commands** 

|**Command**|**Description**|**Syntax**|**Example**|
|---|---|---|---|
|SELECT|The SELECT command retrieves<br>data from a database.|SELECT column1, column2 FROM<br>table_name;|SELECT first_name, last_name<br>FROM customers;|
|INSERT|The INSERT command adds new<br>records to a table.|INSERT INTO table_name<br>(column1, column2) VALUES<br>(value1, value2);|INSERT INTO customers<br>(first_name, last_name)<br>VALUES ('Mary', 'Doe');|
|UPDATE|The UPDATE command is used<br>to modify existing records in a<br>table.|UPDATE table_name SET column1<br>= value1, column2 = value2<br>WHERE condition;|UPDATE employees SET<br>employee_name = ‘John Doe’,<br>department = ‘Marketing’;|
|DELETE|The DELETE command removes<br>records from a table.|DELETE FROM table_name WHERE<br>condition;|DELETE FROM employees WHERE<br>employee_name = ‘John Doe’;|



`UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;` 

## **Example** 

`SELECT first_name, last_name FROM customers;` 

`INSERT INTO customers (first_name, last_name) VALUES ('Mary', 'Doe');` 

`UPDATE employees SET employee_name = ‘John Doe’, department = ‘Marketing’; DELETE FROM employees WHERE employee_name = ‘John Doe’;` 

## **Data Definition Language �DDL�Commands** 

|**Command**|**Description**|**Syntax**|**Example**|
|---|---|---|---|
|CREATE|The CREATE command creates a<br>new database and objects, such<br>as a table, index, view, or stored<br>procedure.|CREATE TABLE table_name<br>(column1 datatype1,<br>column2 datatype2, ���);|CREATE TABLE employees (<br>employee_id INT<br>PRIMARY KEY,<br>first_name<br>VARCHAR(50),<br>last_name<br>VARCHAR(50),<br>age INT<br>);|
|ALTER|The ALTER command adds,<br>deletes, or modifies columns in<br>an existing table.|ALTER TABLE table_name<br>ADD column_name datatype;|ALTER TABLE customers ADD<br>email VARCHAR(100);|
|DROP|The DROP command is used to<br>drop an existing table in a<br>database.|DROP TABLE table_name;|DROP TABLE customers;|
|TRUNCATE|The TRUNCATE command is<br>used to delete the data inside a<br>table, but not the table itself.|TRUNCATE TABLE<br>table_name;|TRUNCATE TABLE customers;|



`DBVIS.COM` ~~ee~~ 

The SQL tool with the highest user satisfaction. `DBVIS.COM ��` 

## **Data Control Language �DCL�Commands** 

|**Command**|**Description**|**Syntax**|
|---|---|---|
|GRANT|The GRANT command is used to|GRANT SELECT, INSERT ON|
||give specific privileges to users|table_name TO user_name;|
||or roles.||
|REVOKE|The REVOKE command is used|REVOKE SELECT, INSERT ON|
||to take away privileges|table_name FROM|
||previously granted to users or|user_name;|
||roles.||



## **Example** 

`GRANT SELECT, INSERT ON employees TO ‘John Doe’; REVOKE SELECT, INSERT ON employees FROM ‘John Doe’;` 

## **Querying Data Commands** 

|**Command**|**Description**|
|---|---|
|SELECTStatement|The SELECT statement is the|
||primary command used to|
||retrieve data from a database|
|WHERE Clause|The WHERE clause is used to|
||filter rows based on a specified|
||condition.|
|ORDER BYClause|The ORDER BY clause is used to|
||sort the result set in ascending|
||or descending order based on a|
||specified column.|
|GROUP BYClause|The GROUP BY clause groups|
||rows based on the values in a|
||specified column. It is often<br>used with aggregate functions|
||like COUNT, SUM, AVG, etc.|
|HAVINGClause|The HAVING clause filters|
||grouped results based on a|
||specified condition.|



## **Syntax** 

`SELECT column1, column2 FROM table_name; SELECT * FROM table_name WHERE condition; SELECT * FROM table_name ORDER BY column_name ASC|DESC; SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;` 

`SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name HAVING condition;` 

## **Example** 

`SELECT first_name, last_name FROM customers; SELECT * FROM customers WHERE age > 30; SELECT * FROM products ORDER BY price DESC;` 

`SELECT category, COUNT(*) FROM products GROUP BY category;` 

`SELECT category, COUNT(*) FROM products GROUP BY category HAVING COUNT(*) > 5;` 

`DBVIS.COM` ~~ee~~ 

The SQL tool with the highest user satisfaction. `DBVIS.COM ��` 

## **Joining Commands** 

|**Joining Commands**||||
|---|---|---|---|
|**Command**|**Description**|**Syntax**|**Example**|
|INNER JOIN|The INNER JOIN command<br>returns rows with matching<br>values in both tables.|SELECT * FROM table1<br>INNER JOIN table2 ON<br>table1.column =<br>table2.column;|SELECT * FROM employees<br>INNER JOIN departments ON<br>employees.department_id =<br>departments.id;|
|LEFT JOIN/LEFT OUTER JOIN|The LEFT JOIN command<br>returns all rows from the left<br>table (first table) and the<br>matching rows from the right<br>table (second table).|SELECT * FROM table1 LEFT<br>JOIN table2 ON<br>table1.column =<br>table2.column;|SELECT * FROM employees LEFT<br>JOIN departments ON<br>employees.department_id =<br>departments.id;|
|RIGHT JOIN/RIGHT OUTER<br>JOIN|The RIGHT JOIN command<br>returns all rows from the right<br>table (second table) and the<br>matching rows from the left<br>table (first table).|SELECT * FROM table1<br>RIGHT JOIN table2 ON<br>table1.column =<br>table2.column;|SELECT *<br>FROM employees<br>RIGHT JOIN departments<br>ON employees.department_id =<br>departments.department_id;|
|FULL JOIN/FULL OUTER JOIN|The FULL JOIN command<br>returns all rows when there is a<br>match in either the left table or<br>the right table.|SELECT * FROM table1 FULL<br>JOIN table2 ON<br>table1.column =<br>table2.column;|SELECT *<br>FROM employees<br>LEFT JOIN departments ON<br>employees.employee_id =<br>departments.employee_id<br>UNION<br>SELECT *<br>FROM employees<br>RIGHT JOIN departments ON<br>employees.employee_id =<br>departments.employee_id;|
|CROSS JOIN|The CROSS JOIN command<br>combines every row from the<br>first table with every row from<br>the second table, creating a<br>Cartesian product.|SELECT * FROM table1<br>CROSS JOIN table2;|SELECT * FROM employees<br>CROSS JOIN departments;|
|SELF JOIN|The SELF JOIN command joins<br>a table with itself.|SELECT * FROM table1 t1,<br>table1 t2 WHERE t1.column<br>= t2.column;|SELECT * FROM employees t1,<br>employees t2<br>WHERE t1.employee_id =<br>t2.employee_id;|
|NATURAL JOIN|The NATURAL JOIN command<br>matches columns with the<br>same name in both tables.|SELECT * FROM table1<br>NATURAL JOIN table2;|SELECT * FROM employees<br>NATURAL JOIN departments;|



`DBVIS.COM` ~~ee~~ 

The SQL tool with the highest user satisfaction. `DBVIS.COM ��` 

## **Subqueries in SQL** 

|**Command**|**Description**|
|---|---|
|IN|The IN command is used to|
||determine whether a value|
||matches any value in a subquery<br>result. It is often used in the|
||WHERE clause.|
|ANY|The ANY command is used to|
||compare a value to any value|
||returned by a subquery. It can|
||be used with comparison<br>operators like =, >, <, etc.|
|ALL|The ALL command is used to|
||compare a value to all values|
||returned by a subquery. It can|
||be used with comparison<br>operators like =, >, <, etc.|
|**Aggregate Functions Commands**|**Aggregate Functions Commands**|
|**Command**|**Description**|
|COUNT()|The COUNT command counts|
||the number of rows or non-null|
||values in a specified column.|
|SUM()|The SUM command is used to|
||calculate the sum of all values in|
||a specified column.|
|AVG()|The AVG command is used to|
||calculate the average (mean) of|
||all values in a specified column.|
|MIN()|The MIN command returns the|
||minimum (lowest) value in a|
||specified column.|
|MAX()|The MAX command returns the|



## **Aggregate Functions Commands** 

The MAX command returns the maximum (highest) value in a specified column. 

## **Syntax** 

`SELECT column(s) FROM table WHERE value IN (subquery); SELECT column(s) FROM table WHERE value < ANY (subquery);` 

`SELECT column(s) FROM table WHERE value > ALL (subquery);` 

## **Syntax** 

`SELECT COUNT(column_name) FROM table_name;` 

`SELECT SUM(column_name) FROM table_name; SELECT AVG(column_name) FROM table_name;` 

`SELECT MIN(column_name) FROM table_name;` 

`SELECT MAX(column_name) FROM table_name;` 

## **Example** 

`SELECT * FROM customers WHERE city IN (SELECT city FROM suppliers);` 

`SELECT * FROM products WHERE price < ANY (SELECT unit_price FROM supplier_products);` 

`SELECT * FROM orders WHERE order_amount > ALL (SELECT total_amount FROM previous_orders);` 

## **Example** 

`SELECT COUNT(age) FROM employees;` 

`SELECT SUM(revenue) FROM sales;` 

`SELECT AVG(price) FROM products;` 

`SELECT MIN(price) FROM products;` 

`SELECT MAX(price) FROM products;` 

The SQL tool with the highest user satisfaction. `DBVIS.COM ��` ~~—~~ 

## **String Functions in SQL** 

|**Command**|**Description**|**Syntax**|**Example**|
|---|---|---|---|
|CONCAT()|The CONCAT command<br>concatenates two or more<br>strings into a single string.|SELECT CONCAT(string1,<br>string2, ���) AS<br>concatenated_string FROM<br>table_name;|SELECT CONCAT(first_name,<br>' ', last_name) AS<br>full_name FROM employees;|
|SUBSTRING()/SUBSTR()|The SUBSTRING command<br>extracts a substring from a<br>string.|SELECT SUBSTRING(string<br>FROM start_position [FOR<br>length]) AS substring<br>FROM table_name;|SELECT<br>SUBSTRING(product_name<br>FROM 1 FOR 5) AS<br>substring FROM products;|
|CHAR_LENGTH()/LENGTH()|The LENGTH command returns<br>the length (number of<br>characters) of a string.|SELECT<br>CHAR_LENGTH(string) AS<br>length FROM table_name;|SELECT<br>CHAR_LENGTH(product_name)<br>AS length FROM products;|
|UPPER()|The UPPER command converts<br>all characters in a string to<br>uppercase.|SELECT UPPER(string) AS<br>uppercase_string FROM<br>table_name;|SELECT UPPER(first_name)<br>AS uppercase_first_name<br>FROM employees;|
|LOWER()|The LOWER command converts<br>all characters in a string to<br>lowercase.|SELECT LOWER(string) AS<br>lowercase_string FROM<br>table_name;|SELECT LOWER(last_name)<br>AS lowercase_last_name<br>FROM employees;|
|TRIM()|The TRIM command removes<br>specified prefixes or suffixes (or<br>whitespace by default) from a<br>string.|SELECT TRIM([LEADING |<br>TRAILING | BOTH]<br>characters FROM string)<br>AS trimmed_string FROM<br>table_name;|SELECT TRIM(TRAILING ' '<br>FROM full_name) AS<br>trimmed_full_name FROM<br>customers;|
|LEFT()|The LEFT command returns a<br>specified number of characters<br>from the left of a string.|SELECT LEFT(string,<br>num_characters) AS<br>left_string FROM<br>table_name;|SELECT<br>LEFT(product_name, 5)<br>AS left_product_name<br>FROM products;|
|RIGHT()|The RIGHT command returns a<br>specified number of characters<br>from the right of a string.|SELECT RIGHT(string,<br>num_characters) AS<br>right_string FROM<br>table_name;|SELECT<br>RIGHT(order_number, 4) AS<br>right_order_number FROM<br>orders;|
|REPLACE()|The REPLACE command<br>replaces occurrences of a<br>substring within a string.|SELECT REPLACE(string,<br>old_substring,<br>new_substring) AS<br>replaced_string FROM<br>table_name;|SELECT<br>REPLACE(description,<br>'old_string',<br>'new_string') AS<br>replaced_description FROM<br>product_descriptions;|



`SELECT REPLACE(string, old_substring, new_substring) AS replaced_string FROM table_name;` 

## **Example** 

`SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;` 

## `SELECT` 

`SUBSTRING(product_name FROM 1 FOR 5) AS substring FROM products;` 

## `SELECT` 

`CHAR_LENGTH(product_name) AS length FROM products;` 

`SELECT UPPER(first_name) AS uppercase_first_name FROM employees;` 

`SELECT LOWER(last_name) AS lowercase_last_name FROM employees;` 

`SELECT TRIM(TRAILING ' ' FROM full_name) AS trimmed_full_name FROM customers;` 

## `SELECT` 

`LEFT(product_name, 5) AS left_product_name FROM products;` 

## `SELECT` 

`RIGHT(order_number, 4) AS right_order_number FROM orders;` 

## `SELECT` 

`REPLACE(description, 'old_string', 'new_string') AS replaced_description FROM product_descriptions;` 

The SQL tool with the highest user satisfaction. `DBVIS.COM ��` ~~—~~ 

## **Date and Time SQL Commands** 

|**Command**|**Description**|**Syntax**|**Example**|
|---|---|---|---|
|CURRENT_DATE()|The CURRENT_DATE command<br>returns the current date.|SELECT CURRENT_DATE() AS<br>current_date;|��|
|CURRENT_TIME()|The CURRENT_TIME command<br>returns the current time.|SELECT CURRENT_TIME() AS<br>current_time;|��|
|CURRENT_TIMESTAMP()|The CURRENT_TIMESTAMP<br>command returns the current<br>date and time.|SELECT<br>CURRENT_TIMESTAMP() AS<br>current_timestamp;|��|
|DATE_PART()|The DATE_PART command<br>extracts a specific part (e.g.,<br>year, month, day) from a date or<br>time.|SELECT DATE_PART('part',<br>date_expression) AS<br>extracted_part;|SELECT DATE_PART('year',<br>'2024-04-11') AS<br>extracted_part;|
|DATE_ADD()/DATE_SUB()|The DATE_ADD command adds<br>or subtracts a specified number<br>of days, months, or years<br>to/from a date.|SELECT<br>DATE_ADD(date_expression,<br>INTERVAL value unit) AS<br>new_date;|��DATE_ADD Example<br>SELECT<br>DATE_ADD('2024-04-11',<br>INTERVAL 1 DAY) AS<br>new_date;<br>��DATE_SUB Example<br>SELECT<br>DATE_SUB('2024-04-11',<br>INTERVAL 1 DAY) AS<br>new_date;|
|EXTRACT()|The EXTRACT command<br>extracts a specific part (e.g.,<br>year, month, day) from a date or<br>time.|SELECT EXTRACT(part FROM<br>date_expression) AS<br>extracted_part;|SELECT EXTRACT(YEAR FROM<br>'2024-04-11') AS<br>extracted_part;|
|TO_CHAR()|The TO_CHAR command<br>converts a date or time to a<br>specified format.|SELECT<br>TO_CHAR(date_expression,<br>'format') AS<br>formatted_date;|SELECT<br>TO_CHAR('2024-04-11',<br>'YYYY-MM-DD') AS<br>formatted_date;|
|TIMESTAMPDIFF()|The TIMESTAMPDIFF command<br>calculates the difference<br>between two timestamps in a<br>specified unit (e.g., days, hours,<br>minutes).|SELECT<br>TIMESTAMPDIFF(unit,<br>timestamp1, timestamp2)<br>AS difference;|SELECT TIMESTAMPDIFF(DAY,<br>'2024-04-10',<br>'2024-04-11') AS<br>difference;|
|DATEDIFF()|The DATEDIFF command<br>calculates the difference in days<br>between two dates.|SELECT DATEDIFF(date1,<br>date2) AS<br>difference_in_days;|SELECT<br>DATEDIFF('2024-04-11',<br>'2024-04-10') AS<br>difference_in_days;|



`SELECT DATE_PART('year', '2024-04-11') AS extracted_part;` 

`��DATE_ADD Example SELECT DATE_ADD('2024-04-11', INTERVAL 1 DAY) AS new_date;` 

`��DATE_SUB Example SELECT DATE_SUB('2024-04-11', INTERVAL 1 DAY) AS new_date;` 

`SELECT EXTRACT(YEAR FROM '2024-04-11') AS extracted_part;` 

`TO_CHAR('2024-04-11', 'YYYY-MM-DD') AS formatted_date;` 

`SELECT TIMESTAMPDIFF(DAY, '2024-04-10', '2024-04-11') AS difference;` 

`SELECT DATEDIFF(date1, date2) AS difference_in_days;` 

`DATEDIFF('2024-04-11', '2024-04-10') AS difference_in_days;` 

~~—~~ 

The SQL tool with the highest user satisfaction. 

`DBVIS.COM ��` 

## **Conditional Expressions** 

|**Command**|**Description**|**Syntax**|**Example**|
|---|---|---|---|
|CASE Statement|The CASE statement allows you<br>to perform conditional logic<br>within a query.|SELECT<br>column1,<br>column2,<br>CASE<br>WHEN condition1<br>THEN result1<br>WHEN condition2<br>THEN result2<br>ELSE<br>default_result<br>END AS alias<br>FROM table_name;|SELECT<br>order_id,<br>total_amount,<br>CASE<br>WHEN total_amount<br>> 1000 THEN 'High Value<br>Order'<br>WHEN total_amount<br>> 500 THEN 'Medium Value<br>Order'<br>ELSE 'Low Value<br>Order'<br>END AS order_status<br>FROM orders;|
|IF() Function|The IF��function evaluates a<br>condition and returns a value<br>based on the evaluation.|SELECT IF(condition,<br>true_value, false_value)<br>AS alias FROM table_name;|SELECT<br>name,<br>age,<br>IF(age > 50,<br>'Senior', 'Junior') AS<br>employee_category<br>FROM employees;|
|COALESCE() Function|The COALESCE��function<br>returns the first non-null value<br>from a list of values.|SELECT COALESCE(value1,<br>value2, ���) AS alias<br>FROM table_name;|SELECT<br>COALESCE(first_name,<br>middle_name) AS<br>preferred_name<br>FROM employees;|
|NULLIF() Function|The NULLIF��function returns<br>null if two specified expressions<br>are equal.|SELECT<br>NULLIF(expression1,<br>expression2) AS alias<br>FROM table_name;|SELECT<br>NULLIF(total_amount,<br>discounted_amount) AS<br>diff_amount FROM orders;|



The SQL tool with the highest user satisfaction. `DBVIS.COM ��` ~~—~~ 

## **Set Operations** 

|**Command**|**Description**||**Syntax**||**Example**|
|---|---|---|---|---|---|
|UNION|The UNION operator||SELECT column1, column2 FROM||SELECT first_name, last_name|
||combines the result sets of||table1||FROM customers|
||two or more SELECT||UNION||UNION|
||statements into a single<br>result set.||SELECT column1, column2 FROM<br>table2;||SELECT first_name, last_name<br>FROM employees;|
|INTERSECT|The INTERSECT operator||SELECT column1, column2 FROM||SELECT first_name, last_name|
||returns the common rows||table1||FROM customers|
||that appear in both result||INTERSECT||INTERSECT|
||sets.||SELECT column1, column2 FROM||SELECT first_name, last_name|
||||table2;||FROM employees;|
|EXCEPT|The EXCEPT operator||SELECT column1, column2 FROM||SELECT first_name, last_name|
||returns the distinct rows||table1||FROM customers|
||from the left result set that||EXCEPT||EXCEPT|
||are not present in the right<br>result set.||SELECT column1, column2 FROM<br>table2;||SELECT first_name, last_name<br>FROM employees;|
|**Transaction Control Commands**||||||
|**Command**|**Description**||**Syntax**|**Example**||
|COMMIT|The COMMIT command is||COMMIT;|BEGIN TRANSACTION;||
||used to save all the changes|||||
||made during the current|||��SQL statements and changes within the transaction||
||transaction and make them|||||
||permanent.|||INSERT INTO employees (name, age) VALUES ('Alice',||
|||||30);||
|||||UPDATE products SET|price = 25.00 WHERE category =|
|||||'Electronics';||
|||||COMMIT;||
|ROLLBACK|The ROLLBACK command is||ROLLBACK;|BEGIN TRANSACTION;||
||used to undo all the|||||
||changes made during the|||��SQL statements and changes within the transaction||
||current transaction and|||||
||discard them.|||INSERT INTO employees (name, age) VALUES ('Bob', 35);||
|||||UPDATE products SET|price = 30.00 WHERE category =|
|||||'Electronics';||
|||||ROLLBACK;||



## **Transaction Control Commands** 

The SQL tool with the highest user satisfaction. `DBVIS.COM ��` ~~—~~ 

|SAVEPOINT|The SAVEPOINT command<br>is used to set a point within<br>a transaction to which you<br>can later roll back.|SAVEPOINT<br>savepoint_n<br>ame;|BEGIN TRANSACTION;<br>INSERT INTO employees (name, age) VALUES ('Carol',<br>28);<br>SAVEPOINT before_update;<br>UPDATE products SET price = 40.00 WHERE category =<br>'Electronics';<br>SAVEPOINT after_update;<br>DELETE FROM customers WHERE age > 60;<br>ROLLBACK TO before_update;<br>��At this point, the DELETE is rolled back, but the<br>UPDATE remains.<br>COMMIT;|
|---|---|---|---|
|ROLLBACK TO<br>SAVEPOINT|The ROLLBACK TO<br>SAVEPOINT command is<br>used to roll back to a<br>specific savepoint within a<br>transaction.|ROLLBACK TO<br>SAVEPOINT<br>savepoint_n<br>ame;|BEGIN TRANSACTION;<br>INSERT INTO employees (name, age) VALUES ('David',<br>42);<br>SAVEPOINT before_update;<br>UPDATE products SET price = 50.00 WHERE category =<br>'Electronics';<br>SAVEPOINT after_update;<br>DELETE FROM customers WHERE age > 60;<br>��Rollback to the savepoint before the update<br>ROLLBACK TO SAVEPOINT before_update;<br>��At this point, the UPDATE is rolled back, but the<br>INSERT remains.<br>COMMIT;|
|SET TRANSACTION|The SET TRANSACTION<br>command is used to<br>configure properties for the<br>current transaction, such as<br>isolation level and<br>transaction mode.|SET<br>TRANSACTION<br>[ISOLATION<br>LEVEL {<br>READ<br>COMMITTED |<br>SERIALIZABL<br>E }]|BEGIN TRANSACTION;<br>��Set the isolation level to READ COMMITTED<br>SET TRANSACTION ISOLATION LEVEL READ COMMITTED;<br>��SQL statements and changes within the transaction<br>INSERT INTO employees (name, age) VALUES ('Emily',<br>35);<br>UPDATE products SET price = 60.00 WHERE category =<br>'Electronics';<br>COMMIT;|



The SQL tool with the highest user satisfaction. `DBVIS.COM ��` ~~—~~ 

