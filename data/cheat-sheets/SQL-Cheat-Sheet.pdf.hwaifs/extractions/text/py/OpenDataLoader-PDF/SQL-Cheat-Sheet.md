# SQL cheat sheet

## Comprehensive

Data Manipulation Language  DML  Commands

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>SELECT</td>
    <td>The SELECT command retrieves data from a database.</td>
    <td>SELECT column1, column2 FROM table_name;</td>
    <td>SELECT first_name, last_name FROM customers;</td>
  </tr>
  <tr>
    <td>INSERT</td>
    <td>The INSERT command adds new records to a table.</td>
    <td>INSERT INTO table_name (column1, column2) VALUES (value1, value2);</td>
    <td>INSERT INTO customers (first_name, last_name) VALUES ('Mary', 'Doe');</td>
  </tr>
  <tr>
    <td>UPDATE</td>
    <td>The UPDATE command is used to modify existing records in a table.</td>
    <td>UPDATE table_name SET column1<br><br>= value1, column2 = value2 WHERE condition;</td>
    <td>UPDATE employees SET employee_name = ‘John Doe’, department = ‘Marketing’;</td>
  </tr>
  <tr>
    <td>DELETE</td>
    <td>The DELETE command removes records from a table.</td>
    <td>DELETE FROM table_name WHERE condition;</td>
    <td>DELETE FROM employees WHERE employee_name = ‘John Doe’;</td>
  </tr>
</table>


Data Definition Language  DDL  Commands

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>CREATE</td>
    <td>The CREATE command creates a new database and objects, such as a table, index, view, or stored procedure.</td>
    <td>CREATE TABLE table_name (column1 datatype1, column2 datatype2,    );</td>
    <td>CREATE TABLE employees (<br><br>employee_id INT PRIMARY KEY,<br><br>first_name VARCHAR(50),<br><br>last_name VARCHAR(50),<br><br>age INT );</td>
  </tr>
  <tr>
    <td>ALTER</td>
    <td>The ALTER command adds, deletes, or modifies columns in an existing table.</td>
    <td>ALTER TABLE table_name ADD column_name datatype;</td>
    <td>ALTER TABLE customers ADD email VARCHAR(100);</td>
  </tr>
  <tr>
    <td>DROP</td>
    <td>The DROP command is used to drop an existing table in a database.</td>
    <td>DROP TABLE table_name;</td>
    <td>DROP TABLE customers;</td>
  </tr>
  <tr>
    <td>TRUNCATE</td>
    <td>The TRUNCATE command is used to delete the data inside a table, but not the table itself.</td>
    <td>TRUNCATE TABLE table_name;</td>
    <td>TRUNCATE TABLE customers;</td>
  </tr>
</table>


![image 1](SQL-Cheat-Sheet_images/imageFile1.png)

### Data Control Language  DCL  Commands

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>GRANT</td>
    <td>The GRANT command is used to give specific privileges to users or roles.</td>
    <td>GRANT SELECT, INSERT ON table_name TO user_name;</td>
    <td>GRANT SELECT, INSERT ON employees TO ‘John Doe’;</td>
  </tr>
  <tr>
    <td>REVOKE</td>
    <td>The REVOKE command is used to take away privileges previously granted to users or roles.</td>
    <td>REVOKE SELECT, INSERT ON table_name FROM user_name;</td>
    <td>REVOKE SELECT, INSERT ON employees FROM ‘John Doe’;</td>
  </tr>
</table>


### Querying Data Commands

#### Command Description Syntax Example

SELECT Statement The SELECT statement is the primary command used to retrieve data from a database

WHERE Clause The WHERE clause is used to filter rows based on a specified condition.

ORDER BY Clause The ORDER BY clause is used to sort the result set in ascending or descending order based on a specified column.

GROUP BY Clause The GROUP BY clause groups rows based on the values in a specified column. It is often used with aggregate functions like COUNT, SUM, AVG, etc.

HAVING Clause The HAVING clause filters grouped results based on a specified condition.

SELECT column1, column2 FROM table_name;

SELECT * FROM table_name WHERE condition;

SELECT * FROM table_name ORDER BY column_name ASC|DESC;

SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;

SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name HAVING condition;

SELECT first_name, last_name FROM customers;

SELECT * FROM customers WHERE age > 30;

SELECT * FROM products ORDER BY price DESC;

SELECT category, COUNT(*) FROM products GROUP BY category;

SELECT category, COUNT(*) FROM products GROUP BY category HAVING COUNT(*) > 5;

### Joining Commands

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>INNER JOIN</td>
    <td>The INNER JOIN command returns rows with matching values in both tables.</td>
    <td>SELECT * FROM table1 INNER JOIN table2 ON<br><br>table1.column =<br>table2.column;<br></td>
    <td>SELECT * FROM employees INNER JOIN departments ON employees.department_id = departments.id;</td>
  </tr>
  <tr>
    <td>LEFT JOIN/LEFT OUTER JOIN</td>
    <td>The LEFT JOIN command returns all rows from the left table (first table) and the matching rows from the right table (second table).</td>
    <td>SELECT * FROM table1 LEFT JOIN table2 ON<br><br>table1.column =<br>table2.column;<br></td>
    <td>SELECT * FROM employees LEFT JOIN departments ON employees.department_id = departments.id;</td>
  </tr>
  <tr>
    <td>RIGHT JOIN/RIGHT OUTER JOIN</td>
    <td>The RIGHT JOIN command returns all rows from the right table (second table) and the matching rows from the left table (first table).</td>
    <td>SELECT * FROM table1 RIGHT JOIN table2 ON<br><br>table1.column =<br>table2.column;<br></td>
    <td>SELECT * FROM employees RIGHT JOIN departments ON employees.department_id = departments.department_id;</td>
  </tr>
  <tr>
    <td>FULL JOIN/FULL OUTER JOIN</td>
    <td>The FULL JOIN command returns all rows when there is a match in either the left table or the right table.</td>
    <td>SELECT * FROM table1 FULL JOIN table2 ON<br><br>table1.column =<br>table2.column;<br></td>
    <td>SELECT * FROM employees LEFT JOIN departments ON employees.employee_id = departments.employee_id UNION SELECT * FROM employees RIGHT JOIN departments ON employees.employee_id = departments.employee_id;</td>
  </tr>
  <tr>
    <td>CROSS JOIN</td>
    <td>The CROSS JOIN command combines every row from the first table with every row from the second table, creating a Cartesian product.</td>
    <td>SELECT * FROM table1 CROSS JOIN table2;</td>
    <td>SELECT * FROM employees CROSS JOIN departments;</td>
  </tr>
  <tr>
    <td>SELF JOIN</td>
    <td>The SELF JOIN command joins a table with itself.</td>
    <td>SELECT * FROM table1 t1, table1 t2 WHERE t1.column<br><br>= t2.column;</td>
    <td>SELECT * FROM employees t1, employees t2 WHERE t1.employee_id = t2.employee_id;</td>
  </tr>
  <tr>
    <td>NATURAL JOIN</td>
    <td>The NATURAL JOIN command matches columns with the same name in both tables.</td>
    <td>SELECT * FROM table1 NATURAL JOIN table2;</td>
    <td>SELECT * FROM employees NATURAL JOIN departments;</td>
  </tr>
</table>


### Subqueries in SQL

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>IN</td>
    <td>The IN command is used to determine whether a value matches any value in a subquery result. It is often used in the WHERE clause.</td>
    <td>SELECT column(s) FROM table WHERE value IN (subquery);</td>
    <td>SELECT * FROM customers WHERE city IN (SELECT city FROM suppliers);</td>
  </tr>
  <tr>
    <td>ANY</td>
    <td>The ANY command is used to compare a value to any value returned by a subquery. It can be used with comparison operators like =, >, <, etc.</td>
    <td>SELECT column(s) FROM table WHERE value < ANY (subquery);</td>
    <td>SELECT * FROM products WHERE price < ANY (SELECT unit_price FROM supplier_products);</td>
  </tr>
  <tr>
    <td>ALL</td>
    <td>The ALL command is used to compare a value to all values returned by a subquery. It can be used with comparison operators like =, >, <, etc.</td>
    <td>SELECT column(s) FROM table WHERE value > ALL (subquery);</td>
    <td>SELECT * FROM orders WHERE order_amount > ALL (SELECT total_amount FROM previous_orders);</td>
  </tr>
</table>


### Aggregate Functions Commands

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>COUNT()</td>
    <td>The COUNT command counts the number of rows or non-null values in a specified column.</td>
    <td>SELECT COUNT(column_name) FROM table_name;</td>
    <td>SELECT COUNT(age) FROM employees;</td>
  </tr>
  <tr>
    <td>SUM()</td>
    <td>The SUM command is used to calculate the sum of all values in a specified column.</td>
    <td>SELECT SUM(column_name) FROM table_name;</td>
    <td>SELECT SUM(revenue) FROM sales;</td>
  </tr>
  <tr>
    <td>AVG()</td>
    <td>The AVG command is used to calculate the average (mean) of all values in a specified column.</td>
    <td>SELECT AVG(column_name) FROM table_name;</td>
    <td>SELECT AVG(price) FROM products;</td>
  </tr>
  <tr>
    <td>MIN()</td>
    <td>The MIN command returns the minimum (lowest) value in a specified column.</td>
    <td>SELECT MIN(column_name) FROM table_name;</td>
    <td>SELECT MIN(price) FROM products;</td>
  </tr>
  <tr>
    <td>MAX()</td>
    <td>The MAX command returns the maximum (highest) value in a specified column.</td>
    <td>SELECT MAX(column_name) FROM table_name;</td>
    <td>SELECT MAX(price) FROM products;</td>
  </tr>
</table>


### String Functions in SQL

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>CONCAT()</td>
    <td>The CONCAT command concatenates two or more strings into a single string.</td>
    <td>SELECT CONCAT(string1, string2,    ) AS concatenated_string FROM table_name;</td>
    <td>SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM employees;</td>
  </tr>
  <tr>
    <td>SUBSTRING()/SUBSTR()</td>
    <td>The SUBSTRING command extracts a substring from a string.</td>
    <td>SELECT SUBSTRING(string FROM start_position [FOR length]) AS substring FROM table_name;</td>
    <td>SELECT SUBSTRING(product_name FROM 1 FOR 5) AS substring FROM products;</td>
  </tr>
  <tr>
    <td>CHAR_LENGTH()/LENGTH()</td>
    <td>The LENGTH command returns the length (number of characters) of a string.</td>
    <td>SELECT CHAR_LENGTH(string) AS length FROM table_name;</td>
    <td>SELECT CHAR_LENGTH(product_name) AS length FROM products;</td>
  </tr>
  <tr>
    <td>UPPER()</td>
    <td>The UPPER command converts all characters in a string to uppercase.</td>
    <td>SELECT UPPER(string) AS uppercase_string FROM table_name;</td>
    <td>SELECT UPPER(first_name) AS uppercase_first_name FROM employees;</td>
  </tr>
  <tr>
    <td>LOWER()</td>
    <td>The LOWER command converts all characters in a string to lowercase.</td>
    <td>SELECT LOWER(string) AS lowercase_string FROM table_name;</td>
    <td>SELECT LOWER(last_name) AS lowercase_last_name FROM employees;</td>
  </tr>
  <tr>
    <td>TRIM()</td>
    <td>The TRIM command removes specified prefixes or suffixes (or whitespace by default) from a string.</td>
    <td>SELECT TRIM([LEADING | TRAILING | BOTH] characters FROM string) AS trimmed_string FROM table_name;</td>
    <td>SELECT TRIM(TRAILING ' ' FROM full_name) AS trimmed_full_name FROM customers;</td>
  </tr>
  <tr>
    <td>LEFT()</td>
    <td>The LEFT command returns a specified number of characters from the left of a string.</td>
    <td>SELECT LEFT(string, num_characters) AS left_string FROM table_name;</td>
    <td>SELECT LEFT(product_name, 5) AS left_product_name FROM products;</td>
  </tr>
  <tr>
    <td>RIGHT()</td>
    <td>The RIGHT command returns a specified number of characters from the right of a string.</td>
    <td>SELECT RIGHT(string, num_characters) AS right_string FROM table_name;</td>
    <td>SELECT RIGHT(order_number, 4) AS right_order_number FROM orders;</td>
  </tr>
  <tr>
    <td>REPLACE()</td>
    <td>The REPLACE command replaces occurrences of a substring within a string.</td>
    <td>SELECT REPLACE(string, old_substring, new_substring) AS replaced_string FROM table_name;</td>
    <td>SELECT REPLACE(description, 'old_string', 'new_string') AS replaced_description FROM product_descriptions;</td>
  </tr>
</table>


### Date and Time SQL Commands

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>CURRENT_DATE()</td>
    <td>The CURRENT_DATE command returns the current date.</td>
    <td>SELECT CURRENT_DATE() AS current_date;</td>
    <td>  </td>
  </tr>
  <tr>
    <td>CURRENT_TIME()</td>
    <td>The CURRENT_TIME command returns the current time.</td>
    <td>SELECT CURRENT_TIME() AS current_time;</td>
    <td>  </td>
  </tr>
  <tr>
    <td>CURRENT_TIMESTAMP()</td>
    <td>The CURRENT_TIMESTAMP command returns the current date and time.</td>
    <td>SELECT CURRENT_TIMESTAMP() AS current_timestamp;</td>
    <td>  </td>
  </tr>
  <tr>
    <td>DATE_PART()</td>
    <td>The DATE_PART command extracts a specific part (e.g., year, month, day) from a date or time.</td>
    <td>SELECT DATE_PART('part', date_expression) AS extracted_part;</td>
    <td>SELECT DATE_PART('year', '2024-04-11') AS extracted_part;</td>
  </tr>
  <tr>
    <td>DATE_ADD()/DATE_SUB()</td>
    <td>The DATE_ADD command adds or subtracts a specified number of days, months, or years to/from a date.</td>
    <td>SELECT DATE_ADD(date_expression, INTERVAL value unit) AS new_date;</td>
    <td>   DATE_ADD Example SELECT DATE_ADD('2024-04-11', INTERVAL 1 DAY) AS new_date;<br><br>   DATE_SUB Example SELECT DATE_SUB('2024-04-11', INTERVAL 1 DAY) AS new_date;</td>
  </tr>
  <tr>
    <td>EXTRACT()</td>
    <td>The EXTRACT command extracts a specific part (e.g., year, month, day) from a date or time.</td>
    <td>SELECT EXTRACT(part FROM date_expression) AS extracted_part;</td>
    <td>SELECT EXTRACT(YEAR FROM '2024-04-11') AS extracted_part;</td>
  </tr>
  <tr>
    <td>TO_CHAR()</td>
    <td>The TO_CHAR command converts a date or time to a specified format.</td>
    <td>SELECT TO_CHAR(date_expression, 'format') AS formatted_date;</td>
    <td>SELECT TO_CHAR('2024-04-11', 'YYYY-MM-DD') AS formatted_date;</td>
  </tr>
  <tr>
    <td>TIMESTAMPDIFF()</td>
    <td>The TIMESTAMPDIFF command calculates the difference between two timestamps in a specified unit (e.g., days, hours, minutes).</td>
    <td>SELECT TIMESTAMPDIFF(unit, timestamp1, timestamp2) AS difference;</td>
    <td>SELECT TIMESTAMPDIFF(DAY,<br><br>'2024-04-10',<br>'2024-04-11') AS difference;<br></td>
  </tr>
  <tr>
    <td>DATEDIFF()</td>
    <td>The DATEDIFF command calculates the difference in days between two dates.</td>
    <td>SELECT DATEDIFF(date1, date2) AS difference_in_days;</td>
    <td>SELECT DATEDIFF('2024-04-11', '2024-04-10') AS difference_in_days;</td>
  </tr>
</table>


### Conditional Expressions

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>CASE Statement</td>
    <td>The CASE statement allows you to perform conditional logic within a query.</td>
    <td>SELECT<br><br>column1,<br>column2, CASE<br><br><br>WHEN condition1<br><br>THEN result1<br><br>WHEN condition2<br><br>THEN result2 ELSE<br><br><br><br><br>default_result<br><br>END AS alias FROM table_name;</td>
    <td>SELECT order_id, total_amount, CASE<br><br>WHEN total_amount > 1000 THEN 'High Value Order'<br><br>WHEN total_amount > 500 THEN 'Medium Value Order'<br><br>ELSE 'Low Value Order'<br><br>END AS order_status FROM orders;</td>
  </tr>
  <tr>
    <td>IF() Function</td>
    <td>The IF   function evaluates a condition and returns a value based on the evaluation.</td>
    <td>SELECT IF(condition, true_value, false_value) AS alias FROM table_name;</td>
    <td>SELECT name, age, IF(age > 50,<br><br>'Senior', 'Junior') AS employee_category FROM employees;</td>
  </tr>
  <tr>
    <td>COALESCE() Function</td>
    <td>The COALESCE   function returns the first non-null value from a list of values.</td>
    <td>SELECT COALESCE(value1, value2,    ) AS alias FROM table_name;</td>
    <td>SELECT<br><br>COALESCE(first_name, middle_name) AS preferred_name FROM employees;</td>
  </tr>
  <tr>
    <td>NULLIF() Function</td>
    <td>The NULLIF   function returns null if two specified expressions are equal.</td>
    <td>SELECT NULLIF(expression1, expression2) AS alias FROM table_name;</td>
    <td>SELECT NULLIF(total_amount, discounted_amount) AS diff_amount FROM orders;</td>
  </tr>
</table>


### Set Operations

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>UNION</td>
    <td>The UNION operator combines the result sets of two or more SELECT statements into a single result set.</td>
    <td>SELECT column1, column2 FROM<br><br>table1 UNION SELECT column1, column2 FROM<br>table2;<br></td>
    <td>SELECT first_name, last_name FROM customers UNION SELECT first_name, last_name FROM employees;</td>
  </tr>
  <tr>
    <td>INTERSECT</td>
    <td>The INTERSECT operator returns the common rows that appear in both result sets.</td>
    <td>SELECT column1, column2 FROM<br><br>table1 INTERSECT SELECT column1, column2 FROM<br>table2;<br></td>
    <td>SELECT first_name, last_name FROM customers INTERSECT SELECT first_name, last_name FROM employees;</td>
  </tr>
  <tr>
    <td>EXCEPT</td>
    <td>The EXCEPT operator returns the distinct rows from the left result set that are not present in the right result set.</td>
    <td>SELECT column1, column2 FROM<br><br>table1 EXCEPT SELECT column1, column2 FROM<br>table2;<br></td>
    <td>SELECT first_name, last_name FROM customers EXCEPT SELECT first_name, last_name FROM employees;</td>
  </tr>
</table>


### Transaction Control Commands

<table>
  <tr>
    <th>Command</th>
    <th>Description</th>
    <th>Syntax</th>
    <th>Example</th>
  </tr>
  <tr>
    <td>COMMIT</td>
    <td>The COMMIT command is used to save all the changes made during the current transaction and make them permanent.</td>
    <td>COMMIT;</td>
    <td>BEGIN TRANSACTION;<br><br>   SQL statements and changes within the transaction<br><br>INSERT INTO employees (name, age) VALUES ('Alice', 30); UPDATE products SET price = 25.00 WHERE category = 'Electronics';<br><br>COMMIT;</td>
  </tr>
  <tr>
    <td>ROLLBACK</td>
    <td>The ROLLBACK command is used to undo all the changes made during the current transaction and discard them.</td>
    <td>ROLLBACK;</td>
    <td>BEGIN TRANSACTION;<br><br>   SQL statements and changes within the transaction<br><br>INSERT INTO employees (name, age) VALUES ('Bob', 35); UPDATE products SET price = 30.00 WHERE category = 'Electronics';<br><br>ROLLBACK;</td>
  </tr>
</table>


<table>
  <tr>
    <th>SAVEPOINT</th>
    <th>The SAVEPOINT command is used to set a point within a transaction to which you can later roll back.</th>
    <th>SAVEPOINT savepoint_n ame;</th>
    <th>BEGIN TRANSACTION;<br><br>INSERT INTO employees (name, age) VALUES ('Carol', 28);<br><br>SAVEPOINT before_update;<br><br>UPDATE products SET price = 40.00 WHERE category = 'Electronics';<br><br>SAVEPOINT after_update;<br><br>DELETE FROM customers WHERE age > 60;<br><br>ROLLBACK TO before_update;<br><br>   At this point, the DELETE is rolled back, but the UPDATE remains.<br><br>COMMIT;</th>
  </tr>
  <tr>
    <td>ROLLBACK TO SAVEPOINT</td>
    <td>The ROLLBACK TO SAVEPOINT command is used to roll back to a specific savepoint within a transaction.</td>
    <td>ROLLBACK TO SAVEPOINT savepoint_n ame;</td>
    <td>BEGIN TRANSACTION;<br><br>INSERT INTO employees (name, age) VALUES ('David', 42);<br><br>SAVEPOINT before_update;<br><br>UPDATE products SET price = 50.00 WHERE category = 'Electronics';<br><br>SAVEPOINT after_update;<br><br>DELETE FROM customers WHERE age > 60;<br><br>   Rollback to the savepoint before the update ROLLBACK TO SAVEPOINT before_update;<br><br>   At this point, the UPDATE is rolled back, but the INSERT remains.<br><br>COMMIT;</td>
  </tr>
  <tr>
    <td>SET TRANSACTION</td>
    <td>The SET TRANSACTION command is used to configure properties for the current transaction, such as isolation level and transaction mode.</td>
    <td>SET TRANSACTION [ISOLATION LEVEL { READ COMMITTED | SERIALIZABL E }]</td>
    <td>BEGIN TRANSACTION;<br><br>   Set the isolation level to READ COMMITTED SET TRANSACTION ISOLATION LEVEL READ COMMITTED;<br><br>   SQL statements and changes within the transaction<br><br>INSERT INTO employees (name, age) VALUES ('Emily', 35); UPDATE products SET price = 60.00 WHERE category = 'Electronics';<br><br>COMMIT;</td>
  </tr>
</table>


