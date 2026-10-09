 
##  SQL Basics Cheat Sheet

### 1. **Data Definition Language (DDL)**
Used to define and manage database structure.
- `CREATE TABLE table_name (...)` → make a new table  
- `ALTER TABLE table_name ADD column_name datatype` → change table  
- `DROP TABLE table_name` → delete table  

---

### 2. **Data Manipulation Language (DML)**
Used to work with data inside tables.
- `SELECT * FROM table_name;` → retrieve data  
- `INSERT INTO table_name VALUES (...);` → add data  
- `UPDATE table_name SET column=value WHERE condition;` → modify data  
- `DELETE FROM table_name WHERE condition;` → remove data  

---

### 3. **Data Query Language (DQL)**
Focuses on retrieving data.
- `SELECT column1, column2 FROM table_name;`  
- Clauses:  
  - `WHERE` → filter rows  
  - `ORDER BY` → sort results  
  - `GROUP BY` → group rows  
  - `HAVING` → filter groups  

---

### 4. **Data Control Language (DCL)**
Controls access and permissions.
- `GRANT SELECT ON table TO user;` → give rights  
- `REVOKE SELECT ON table FROM user;` → remove rights  

---

### 5. **Transaction Control Language (TCL)**
Ensures data integrity in multi-step operations.
- `BEGIN TRANSACTION;` → start  
- `COMMIT;` → save changes  
- `ROLLBACK;` → undo changes  

---

### 6. **Constraints**
Rules applied to columns.
- `PRIMARY KEY` → unique + not null  
- `FOREIGN KEY` → link to another table  
- `UNIQUE` → no duplicates  
- `NOT NULL` → must have value  
- `CHECK` → condition must be true  

---

### 7. **Aggregate Functions**
Operate on sets of rows.
- `COUNT()` → number of rows  
- `SUM()` → total  
- `AVG()` → average  
- `MIN()` / `MAX()` → smallest / largest  

---

### 8. **Joins**
Combine data from multiple tables.
- `INNER JOIN` → matching rows only  
- `LEFT JOIN` → all from left + matches  
- `RIGHT JOIN` → all from right + matches  
- `FULL JOIN` → all rows from both  

---

### 9. **Indexes**
Speed up searches.
- `CREATE INDEX idx_name ON table(column);`  

---

### 10. **Views**
Virtual tables based on queries.
- `CREATE VIEW view_name AS SELECT ...;`  

---

 