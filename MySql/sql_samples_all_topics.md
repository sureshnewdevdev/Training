# SQL Samples — Complete Reference (Based on Your Topic List)

**Goal:** For each topic in your image, you get a definition, options/variants, and compact runnable samples using a single mini retail schema.

## Mini Retail Schema (used across examples)
```sql
CREATE TABLE Customer (
  CustomerID      SERIAL PRIMARY KEY,
  Name            VARCHAR(100) NOT NULL,
  Email           VARCHAR(120) UNIQUE,
  CreatedAt       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Product (
  ProductID       SERIAL PRIMARY KEY,
  Sku             VARCHAR(40) UNIQUE NOT NULL,
  Title           VARCHAR(120) NOT NULL,
  Price           DECIMAL(10,2) NOT NULL CHECK (Price >= 0)
);

CREATE TABLE "Order" (
  OrderID         SERIAL PRIMARY KEY,
  CustomerID      INT NOT NULL,
  OrderDate       DATE NOT NULL DEFAULT CURRENT_DATE,
  Status          VARCHAR(20) NOT NULL DEFAULT 'NEW',
  CONSTRAINT fk_order_customer
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE
);

CREATE TABLE OrderItem (
  OrderItemID     SERIAL PRIMARY KEY,
  OrderID         INT NOT NULL,
  ProductID       INT NOT NULL,
  Qty             INT NOT NULL CHECK (Qty > 0),
  UnitPrice       DECIMAL(10,2) NOT NULL CHECK (UnitPrice >= 0),
  CONSTRAINT fk_item_order   FOREIGN KEY (OrderID)  REFERENCES "Order"(OrderID)  ON DELETE CASCADE,
  CONSTRAINT fk_item_product FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

CREATE TABLE Payment (
  PaymentID       SERIAL PRIMARY KEY,
  OrderID         INT NOT NULL,
  Amount          DECIMAL(10,2) NOT NULL,
  Method          VARCHAR(20) NOT NULL CHECK (Method IN ('CARD','CASH','UPI')),
  PaidAt          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT fk_payment_order FOREIGN KEY (OrderID) REFERENCES "Order"(OrderID)
);

CREATE TABLE Department (
  DeptID SERIAL PRIMARY KEY,
  DeptName VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE Employee (
  EmpID SERIAL PRIMARY KEY,
  DeptID INT NOT NULL,
  FullName VARCHAR(100) NOT NULL,
  Salary DECIMAL(10,2) NOT NULL,
  CONSTRAINT fk_emp_dept FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
);
```

Seed:
```sql
INSERT INTO Customer (Name, Email) VALUES
('Asha', 'asha@example.com'), ('Rahul', 'rahul@example.com');

INSERT INTO Product (Sku, Title, Price) VALUES
('SKU-1','USB Cable',199.00), ('SKU-2','Mouse',899.00), ('SKU-3','Keyboard',1299.00);

INSERT INTO "Order"(CustomerID, Status) VALUES (1, 'PAID'), (2, 'NEW');

INSERT INTO OrderItem (OrderID, ProductID, Qty, UnitPrice) VALUES
(1,1,2,199.00), (1,2,1,899.00), (2,3,1,1299.00);

INSERT INTO Payment (OrderID, Amount, Method) VALUES (1,1297.00,'CARD');

INSERT INTO Department (DeptName) VALUES ('Sales'), ('IT');
INSERT INTO Employee (DeptID, FullName, Salary) VALUES (1, 'Priya N', 75000), (2,'Karthik S', 90000);
```

---

## Advanced-Schema

### Primary Key
```sql
CREATE TABLE City (
  CityID SERIAL PRIMARY KEY,
  Name   VARCHAR(80) NOT NULL
);
```

### Composite Key
```sql
CREATE TABLE Inventory (
  WarehouseID INT,
  ProductID   INT,
  OnHand      INT DEFAULT 0,
  PRIMARY KEY (WarehouseID, ProductID)
);
```

### Foreign Key (with actions)
```sql
ALTER TABLE OrderItem
  ADD CONSTRAINT fk_item_product2
  FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
  ON UPDATE CASCADE ON DELETE RESTRICT;
```

### Referential Integrity (demo failure)
```sql
INSERT INTO OrderItem (OrderID, ProductID, Qty, UnitPrice)
VALUES (999, 1, 1, 199.00); -- fails if 999 not in Order
```

### Unique / Alternate Key
```sql
ALTER TABLE Customer ADD CONSTRAINT uq_customer_email UNIQUE (Email);
-- Email serves as alternate key for lookups
SELECT * FROM Customer WHERE Email='asha@example.com';
```

### Normalization
-- 1NF, 2NF, 3NF covered by splitting Order/OrderItem and keeping atomic attributes.

### Multiplicity
-- Customer 1..N Order, Order 1..N OrderItem, Product 1..N OrderItem.

### Consistency
-- Enforced with PK/FK/UNIQUE/CHECK + transactions (see ACID).

### CREATE / DROP / TRUNCATE
```sql
CREATE TABLE TempLog (ID INT PRIMARY KEY, Msg TEXT);
TRUNCATE TABLE TempLog;
DROP TABLE TempLog;
```

### Constraints / CHECK / DEFAULT
```sql
ALTER TABLE Product ALTER COLUMN Title SET NOT NULL;
ALTER TABLE Product ADD CONSTRAINT chk_price CHECK (Price >= 0);
ALTER TABLE "Order" ALTER COLUMN Status SET DEFAULT 'NEW';
```

### Auto Incrementing
```sql
CREATE TABLE Ticket (
  TicketID BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  Title VARCHAR(120) NOT NULL
);
```

### CASCADE
```sql
DELETE FROM Customer WHERE CustomerID=1; -- cascades to Order & OrderItem via FKs
```

### INSERT / UPDATE / DELETE
```sql
INSERT INTO Customer (Name, Email) VALUES ('Divya','divya@example.com');
UPDATE Product SET Price = Price * 1.1 WHERE Sku='SKU-2';
DELETE FROM "Order" WHERE Status='NEW' AND OrderDate < CURRENT_DATE - INTERVAL '90 days';
```

---

## Aggregate Functions
```sql
SELECT COUNT(*) AS orders,
       SUM(Amount) AS total_received,
       AVG(Amount) AS avg_payment
FROM Payment;
```

## Scalar Functions
```sql
SELECT LOWER(Email) AS email_norm,
       COALESCE(Name,'Unknown') AS display_name
FROM Customer;
```

## Window Functions
```sql
SELECT
  o.CustomerID, o.OrderID, o.OrderDate,
  SUM(oi.Qty*oi.UnitPrice) AS order_total,
  SUM(SUM(oi.Qty*oi.UnitPrice)) OVER (
    PARTITION BY o.CustomerID ORDER BY o.OrderDate
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS running_total
FROM "Order" o
JOIN OrderItem oi ON oi.OrderID = o.OrderID
GROUP BY o.CustomerID, o.OrderID, o.OrderDate;
```

## Clauses (SELECT...WHERE...GROUP BY...HAVING...ORDER BY...LIMIT/OFFSET)
```sql
SELECT c.CustomerID, c.Name, COUNT(o.OrderID) AS order_count
FROM Customer c
LEFT JOIN "Order" o ON o.CustomerID = c.CustomerID
WHERE c.CreatedAt >= CURRENT_DATE - INTERVAL '180 days'
GROUP BY c.CustomerID, c.Name
HAVING COUNT(o.OrderID) >= 1
ORDER BY order_count DESC
LIMIT 10 OFFSET 0;
```

---

## Sub-Queries & Joins

### What Is a Subquery
```sql
SELECT * FROM Customer c
WHERE c.CustomerID IN (
  SELECT o.CustomerID
  FROM "Order" o
  JOIN OrderItem oi ON oi.OrderID = o.OrderID
  GROUP BY o.CustomerID
  HAVING AVG(oi.Qty*oi.UnitPrice) > (
    SELECT AVG(oi2.Qty*oi2.UnitPrice)
    FROM OrderItem oi2 JOIN "Order" o2 ON o2.OrderID = oi2.OrderID
  )
);
```

### What Is a Join (overview)
-- INNER, LEFT, RIGHT, FULL, CROSS, SELF

### Aliases
```sql
SELECT c.Name AS customer_name, o.OrderID AS oid
FROM Customer AS c JOIN "Order" AS o ON o.CustomerID = c.CustomerID;
```

### Cross Join
```sql
SELECT d.DeptName, p.Sku
FROM Department d CROSS JOIN Product p;
```

### Inner Join
```sql
SELECT o.OrderID, c.Name, SUM(oi.Qty*oi.UnitPrice) AS order_total
FROM "Order" o
JOIN Customer c ON c.CustomerID = o.CustomerID
JOIN OrderItem oi ON oi.OrderID = o.OrderID
GROUP BY o.OrderID, c.Name;
```

### Left and Right Joins
```sql
SELECT c.CustomerID, c.Name, o.OrderID
FROM Customer c LEFT JOIN "Order" o ON o.CustomerID = c.CustomerID;

SELECT c.CustomerID, c.Name, o.OrderID
FROM Customer c RIGHT JOIN "Order" o ON o.CustomerID = c.CustomerID;
```

### Outer Join (Full)
```sql
SELECT c.CustomerID, c.Name, o.OrderID
FROM Customer c FULL OUTER JOIN "Order" o ON o.CustomerID = c.CustomerID; -- not in MySQL
```

### Equi and Theta Joins
```sql
SELECT e.FullName, d.DeptName
FROM Employee e JOIN Department d ON e.DeptID = d.DeptID;  -- equi

SELECT e.FullName, d.DeptName
FROM Employee e JOIN Department d ON e.Salary > 80000 AND e.DeptID = d.DeptID; -- theta
```

---

## ACID Properties
-- Atomicity, Consistency, Isolation, Durability

## What Is a Transaction
```sql
BEGIN;
  UPDATE Product SET Price = Price - 100 WHERE Sku='SKU-2';
  INSERT INTO Payment (OrderID, Amount, Method) VALUES (2, 899.00, 'UPI');
COMMIT;
```

## Transaction Properties (Isolation Levels)
```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;
  -- Consistent snapshot inside txn
COMMIT;
```

## CRUD Operations
```sql
INSERT INTO Product (Sku, Title, Price) VALUES ('SKU-4','Headset',1999.00);
SELECT ProductID, Sku, Title, Price FROM Product WHERE Price BETWEEN 500 AND 2000;
UPDATE Product SET Price = Price * 0.95 WHERE Sku='SKU-4';
DELETE FROM Product WHERE Sku='SKU-4';
```

## Transaction Commit / Rollback / Isolation Demo
```sql
BEGIN;
  UPDATE "Order" SET Status='PAID' WHERE OrderID=2;
ROLLBACK;  -- undo
```

## Sequence
```sql
CREATE SEQUENCE public.order_ref_seq START WITH 1000 INCREMENT BY 1;
SELECT nextval('public.order_ref_seq');   -- 1000
ALTER SEQUENCE public.order_ref_seq RESTART WITH 2000;
```

---

## Window Function Options Cheat Sheet
```sql
SELECT p.ProductID, p.Title, p.Price,
       ROW_NUMBER() OVER (ORDER BY p.Price DESC) AS rn_global,
       RANK()       OVER (ORDER BY p.Price DESC) AS rk_global,
       DENSE_RANK() OVER (ORDER BY p.Price DESC) AS drk_global
FROM Product p;
```

## Clause Options Cheat Sheet (dialect notes)
-- WHERE vs HAVING; ORDER BY multi-keys;
-- LIMIT/OFFSET (Postgres/MySQL) vs TOP/OFFSET FETCH (SQL Server).

```sql
-- SQL Server paging
SELECT ProductID, Title, Price
FROM Product
ORDER BY Price DESC
OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY;
```

---

### Best Practices
- Surrogate PKs + natural UNIQUE keys.
- Define FK actions explicitly.
- CHECK for domain rules.
- Index FKs & join columns.
- Prefer window fns for analytic queries.
- Wrap multi-step writes in transactions; pick isolation level intentionally.
