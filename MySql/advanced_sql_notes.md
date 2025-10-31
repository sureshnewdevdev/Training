# 🧠 Advanced SQL – Detailed Notes with Examples

---

## 1️⃣ Indexes

### 🔹 What is an Index?
An **Index** in SQL is a data structure (like an index in a book) that helps speed up data retrieval from a table.  
Instead of scanning every row, SQL uses the index to quickly locate the required rows.

### 🔹 Why use it?
- Improves performance of `SELECT` queries.  
- Reduces I/O operations while searching.  
- Particularly useful on large tables.

### 🔹 Syntax:
```sql
CREATE INDEX index_name
ON table_name (column1, column2, ...);
```

### 🔹 Example:
```sql
CREATE INDEX idx_customer_name
ON Customers(CustomerName);
```

### 🔹 Notes:
- Indexes **slow down INSERT, UPDATE, DELETE** (since index also needs updating).  
- Use indexes on columns that are **frequently searched or used in WHERE, JOIN, ORDER BY**.

---

## 2️⃣ Triggers

### 🔹 What is a Trigger?
A **Trigger** is an automatic action executed by the database **in response to a specific event** (INSERT, UPDATE, DELETE).

### 🔹 Why use it?
- To enforce business rules automatically.  
- To log audit information (e.g., who changed what).  
- To maintain data consistency.

### 🔹 Syntax:
```sql
CREATE TRIGGER trigger_name
AFTER INSERT
ON table_name
FOR EACH ROW
BEGIN
   -- actions
END;
```

### 🔹 Example:
```sql
CREATE TRIGGER trg_after_insert_sales
AFTER INSERT
ON Sales
FOR EACH ROW
BEGIN
   INSERT INTO Sales_Log(SaleID, Action, ActionDate)
   VALUES (NEW.SaleID, 'INSERTED', NOW());
END;
```

### 🔹 Notes:
- Types: **BEFORE** and **AFTER** triggers.  
- Avoid complex logic to prevent performance issues.  
- Useful for maintaining history logs or auditing.

---

## 3️⃣ Views

### 🔹 What is a View?
A **View** is a **virtual table** based on the result of an SQL query.  
It doesn’t store data physically; it displays data from one or more tables dynamically.

### 🔹 Why use it?
- Simplifies complex queries.  
- Provides data security by restricting access to specific columns.  
- Allows reusability of common query logic.

### 🔹 Syntax:
```sql
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;
```

### 🔹 Example:
```sql
CREATE VIEW Active_Customers AS
SELECT CustomerID, CustomerName, City
FROM Customers
WHERE Status = 'Active';
```

### 🔹 Notes:
- You can query a view like a normal table:
  ```sql
  SELECT * FROM Active_Customers;
  ```
- Some databases allow **updatable views** (you can perform INSERT/UPDATE).

---

## 4️⃣ Stored Procedures

### 🔹 What is a Stored Procedure?
A **Stored Procedure (SP)** is a **precompiled block of SQL code** that performs one or more tasks.  
It can take **input parameters**, return **output**, and execute logic.

### 🔹 Why use it?
- Improves performance (compiled once, executed multiple times).  
- Reduces code duplication.  
- Enhances security by restricting direct table access.  
- Supports automation (e.g., monthly sales reports).

### 🔹 Syntax:
```sql
CREATE PROCEDURE procedure_name (@parameter datatype)
AS
BEGIN
   -- SQL statements
END;
```

### 🔹 Example:
```sql
CREATE PROCEDURE GetCustomerOrders
    @CustomerID INT
AS
BEGIN
    SELECT OrderID, OrderDate, TotalAmount
    FROM Orders
    WHERE CustomerID = @CustomerID;
END;
```

### 🔹 Execution:
```sql
EXEC GetCustomerOrders @CustomerID = 101;
```

### 🔹 Notes:
- Can contain **IF-ELSE**, **LOOPS**, and **TRANSACTIONS**.  
- Often used for complex business logic inside databases.

---

## 5️⃣ User Defined Functions (UDFs)

### 🔹 What is a UDF?
A **User Defined Function** is a **custom reusable function** created by the user to perform calculations or return specific results.

### 🔹 Types of UDFs:
1. **Scalar Function** → returns a single value.  
2. **Table-Valued Function** → returns a table.

### 🔹 Syntax (Scalar Function):
```sql
CREATE FUNCTION function_name (@param datatype)
RETURNS datatype
AS
BEGIN
   DECLARE @result datatype;
   SET @result = -- expression
   RETURN @result;
END;
```

### 🔹 Example:
```sql
CREATE FUNCTION fn_GetDiscount(@Amount DECIMAL(10,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
   DECLARE @Discount DECIMAL(10,2);
   IF @Amount > 10000
       SET @Discount = @Amount * 0.10;
   ELSE
       SET @Discount = @Amount * 0.05;
   RETURN @Discount;
END;
```

### 🔹 Usage:
```sql
SELECT dbo.fn_GetDiscount(15000) AS DiscountAmount;
```

---

# 🧬 Quick Comparison Table

| Concept | Definition | Purpose | Returns Data | Example Use Case |
|----------|-------------|----------|---------------|------------------|
| **Index** | Data structure to speed up search | Performance | No | Searching customers by name |
| **Trigger** | Auto action on data change | Automation / Audit | No | Log updates in audit table |
| **View** | Virtual table from query | Simplify queries | Yes | Show only active users |
| **Stored Procedure** | Precompiled SQL block | Reuse logic | Optional | Get monthly report |
| **UDF** | Custom reusable function | Modularization | Yes (value/table) | Calculate discount or tax |

---

