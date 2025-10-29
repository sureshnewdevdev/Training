# MySQL Sub-Languages – Detailed Notes with Examples

SQL (Structured Query Language) is divided into **five major sub-languages** based on their purpose. Each serves a distinct role in managing and interacting with a database.

---

## 🔹 1. Overview of Sub-Languages

| Sub-Language | Full Form | Purpose |
|---------------|------------|----------|
| **DDL** | Data Definition Language | Defines structure of database objects (tables, schema, etc.) |
| **DML** | Data Manipulation Language | Manipulates (insert/update/delete) actual data |
| **DQL** | Data Query Language | Fetches data from database |
| **DCL** | Data Control Language | Controls access and permissions |
| **TCL** | Transaction Control Language | Manages transactions in a database |

---

## 🧱 2. DDL (Data Definition Language)

### **Purpose:**  
Used to **define or modify** the database structure (schemas, tables, indexes, etc.)

### **Commands:**
- `CREATE` – Create database objects  
- `ALTER` – Modify existing structure  
- `DROP` – Delete entire structure  
- `TRUNCATE` – Remove all data but keep structure  
- `RENAME` – Rename an object  

### **Example:**
```sql
-- Create a table
CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    Department VARCHAR(30),
    Salary DECIMAL(10,2)
);

-- Add a new column
ALTER TABLE Employees ADD COLUMN HireDate DATE;

-- Rename the table
RENAME TABLE Employees TO Staff;

-- Remove all rows (faster than DELETE)
TRUNCATE TABLE Staff;

-- Delete the table permanently
DROP TABLE Staff;
```

💡 **Note:** DDL commands auto-commit — you **cannot rollback** changes made by them.

---

## ✏️ 3. DML (Data Manipulation Language)

### **Purpose:**  
Used to **manipulate or modify** data stored in database tables.

### **Commands:**
- `INSERT` – Add new records  
- `UPDATE` – Modify existing records  
- `DELETE` – Remove records  

### **Example:**
```sql
-- Insert data
INSERT INTO Employees (EmpID, EmpName, Department, Salary)
VALUES (101, 'Amit Sharma', 'IT', 60000);

-- Update data
UPDATE Employees
SET Salary = 65000
WHERE EmpID = 101;

-- Delete data
DELETE FROM Employees
WHERE EmpID = 101;
```

💡 **Tip:** DML operations can be **rolled back** if enclosed in a transaction.

---

## 🔍 4. DQL (Data Query Language)

### **Purpose:**  
Used to **retrieve data** from one or more tables.

### **Primary Command:**  
- `SELECT`

### **Example:**
```sql
-- Get all employees
SELECT * FROM Employees;

-- Get specific columns
SELECT EmpName, Department FROM Employees;

-- Filtered result
SELECT * FROM Employees WHERE Department = 'IT';

-- Sort by salary
SELECT * FROM Employees ORDER BY Salary DESC;

-- Aggregate example
SELECT Department, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department;
```

💡 **Note:** DQL does not modify data; it only **queries**.

---

## 🔐 5. DCL (Data Control Language)

### **Purpose:**  
Used to **control access and privileges** in a database.

### **Commands:**
- `GRANT` – Give privileges  
- `REVOKE` – Remove privileges  

### **Example:**
```sql
-- Grant permission to a user
GRANT SELECT, INSERT ON company_db.* TO 'user1'@'localhost';

-- Remove permission
REVOKE INSERT ON company_db.* FROM 'user1'@'localhost';
```

💡 **Tip:** DCL is often used by administrators to maintain database security.

---

## 🔁 6. TCL (Transaction Control Language)

### **Purpose:**  
Used to **manage transactions** ensuring data integrity.

### **Commands:**
- `COMMIT` – Save changes permanently  
- `ROLLBACK` – Undo changes  
- `SAVEPOINT` – Create intermediate points to rollback partially  

### **Example:**
```sql
START TRANSACTION;

INSERT INTO Employees VALUES (201, 'Kavya Nair', 'HR', 50000);
UPDATE Employees SET Salary = Salary + 5000 WHERE EmpID = 201;

-- Savepoint before deletion
SAVEPOINT before_delete;

DELETE FROM Employees WHERE EmpID = 202;

-- Rollback only to savepoint
ROLLBACK TO before_delete;

-- Finalize transaction
COMMIT;
```

💡 **Note:** Transactions are crucial when multiple operations must succeed or fail together.

---

## 🧠 7. Queries (Practical Examples)

### **1️⃣ Simple SELECT**
```sql
SELECT EmpName, Salary FROM Employees;
```

### **2️⃣ Filter with WHERE**
```sql
SELECT * FROM Employees WHERE Salary > 50000;
```

### **3️⃣ Sorting and Limiting**
```sql
SELECT * FROM Employees ORDER BY Salary DESC LIMIT 3;
```

### **4️⃣ Joining Two Tables**
```sql
SELECT e.EmpName, d.DeptName
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DeptID;
```

### **5️⃣ Aggregate and Group**
```sql
SELECT Department, COUNT(*) AS Total, AVG(Salary) AS AvgSalary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 55000;
```

### **6️⃣ Subquery Example**
```sql
SELECT EmpName
FROM Employees
WHERE Salary > (SELECT AVG(Salary) FROM Employees);
```

---

## ✅ Summary Table

| Category | Keyword | Description |
|-----------|----------|--------------|
| **DDL** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` | Structure definition |
| **DML** | `INSERT`, `UPDATE`, `DELETE` | Data modification |
| **DQL** | `SELECT` | Data retrieval |
| **DCL** | `GRANT`, `REVOKE` | Permission control |
| **TCL** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` | Transaction control |

---
