# 🧾 Database Normalization (1NF to 5NF)

## 📘 What is Normalization?
Normalization is the process of organizing data in a database to eliminate redundancy and ensure data integrity. It divides large tables into smaller, related tables and defines relationships between them.

## 🎯 Why Normalize?
- To remove redundancy and anomalies
- To improve data integrity and efficiency
- To make maintenance easier and queries faster

---

## 💡 Real-World Scenario: Online Bookstore Example

| OrderID | CustomerName | CustomerAddress | BookTitle | Author | Price | Quantity | TotalAmount |
|----------|---------------|----------------|------------|---------|--------|-----------|--------------|
| 1 | Ravi Kumar | Delhi | DBMS Concepts | Navathe | 400 | 2 | 800 |
| 2 | Ravi Kumar | Delhi | SQL Fundamentals | Groff | 500 | 1 | 500 |
| 3 | Priya Singh | Mumbai | Python Basics | Reema | 600 | 1 | 600 |

Problems:
- Repeated customer info
- Redundancy in data
- Update and deletion anomalies

---

## 🧩 1st Normal Form (1NF)

### Definition
A table is in **1NF** if each column contains atomic (indivisible) values and each record is unique.

### Unnormalized Table
| OrderID | CustomerName | Address | BooksPurchased |
|----------|--------------|----------|----------------|
| 1 | Ravi Kumar | Delhi | DBMS Concepts, SQL Fundamentals |
| 2 | Priya Singh | Mumbai | Python Basics |

### Normalized Table (1NF)
| OrderID | CustomerName | Address | BookTitle |
|----------|--------------|----------|------------|
| 1 | Ravi Kumar | Delhi | DBMS Concepts |
| 1 | Ravi Kumar | Delhi | SQL Fundamentals |
| 2 | Priya Singh | Mumbai | Python Basics |

### Diagram
Unnormalized → 1NF
```
 ┌────────────┐          ┌────────────────────┐
 | OrderID    |          | OrderID | BookTitle|
 | Customer   |          | Customer| Address  |
 | Books[]    |  ---->   | (Atomic values)    |
 └────────────┘          └────────────────────┘
```

### Benefits
- Eliminates repeating groups
- Each field holds atomic value
- Simplifies filtering and sorting

---

## 🧩 2nd Normal Form (2NF)

### Definition
A table is in **2NF** if it is in 1NF and all non-key columns depend on the entire primary key (not part of it).

### 1NF Table
| OrderID | CustomerName | Address | BookTitle | Price |
|----------|---------------|----------|------------|--------|
| 1 | Ravi Kumar | Delhi | DBMS Concepts | 400 |
| 1 | Ravi Kumar | Delhi | SQL Fundamentals | 500 |
| 2 | Priya Singh | Mumbai | Python Basics | 600 |

Problem: CustomerName and Address depend only on OrderID.

### Normalized Tables (2NF)
**Orders**
| OrderID | CustomerName | Address |
|----------|---------------|----------|
| 1 | Ravi Kumar | Delhi |
| 2 | Priya Singh | Mumbai |

**OrderDetails**
| OrderID | BookTitle | Price |
|----------|------------|--------|
| 1 | DBMS Concepts | 400 |
| 1 | SQL Fundamentals | 500 |
| 2 | Python Basics | 600 |

### Diagram
```
Orders ───┬─── OrderDetails
OrderID   │   OrderID(FK)
```
### Benefits
- Removes partial dependencies
- Reduces redundancy

---

## 🧩 3rd Normal Form (3NF)

### Definition
A table is in **3NF** if it is in 2NF and has no transitive dependencies (non-key attribute depends on another non-key attribute).

### 2NF Table
| OrderID | CustomerName | Address | City | Pincode |
|----------|---------------|----------|--------|----------|
| 1 | Ravi Kumar | Lajpat Nagar | Delhi | 110024 |
| 2 | Priya Singh | Andheri | Mumbai | 400058 |

Problem: City depends on Pincode.

### Normalized Tables (3NF)
**Orders**
| OrderID | CustomerName | Pincode |
|----------|---------------|----------|
| 1 | Ravi Kumar | 110024 |
| 2 | Priya Singh | 400058 |

**Pincode**
| Pincode | City | Address |
|----------|--------|----------|
| 110024 | Delhi | Lajpat Nagar |
| 400058 | Mumbai | Andheri |

### Diagram
```
Orders → Pincode
(Customer → Pincode → City)
```
### Benefits
- Removes transitive dependencies
- Improves integrity and consistency

---

## 🧩 Boyce–Codd Normal Form (BCNF)

### Definition
A table is in BCNF if for every functional dependency (X → Y), X is a super key.

### Example
| Professor | Subject | Department |
|------------|----------|-------------|
| Amit | DBMS | CS |
| Amit | OS | CS |
| Rahul | Networks | IT |

Problem: Professor → Department (Professor not a key).

### Normalized Tables
**Professor**
| Professor | Department |
|------------|-------------|
| Amit | CS |
| Rahul | IT |

**Subject**
| Professor | Subject |
|------------|----------|
| Amit | DBMS |
| Amit | OS |
| Rahul | Networks |

### Benefits
- Removes non-key dependencies
- Improves reliability

---

## 🧩 4th Normal Form (4NF)

### Definition
A table is in **4NF** if it is in BCNF and has no multi-valued dependencies.

### Example
| Student | Course | Hobby |
|----------|---------|--------|
| Ravi | DBMS | Cricket |
| Ravi | DBMS | Chess |
| Ravi | Python | Cricket |
| Ravi | Python | Chess |

Problem: Repeated combinations due to multi-valued dependency.

### Normalized Tables (4NF)
**StudentCourse**
| Student | Course |
|----------|---------|
| Ravi | DBMS |
| Ravi | Python |

**StudentHobby**
| Student | Hobby |
|----------|--------|
| Ravi | Cricket |
| Ravi | Chess |

### Benefits
- Removes multi-valued dependencies
- Simpler and faster data operations

---

## 🧩 5th Normal Form (5NF)

### Definition
A table is in **5NF** if it cannot be decomposed further without loss of information and all join dependencies are preserved.

### Example
| Vendor | Product | Customer |
|---------|----------|-----------|
| V1 | P1 | C1 |
| V1 | P1 | C2 |
| V1 | P2 | C1 |

### Normalized Tables (5NF)
**VendorProduct**
| Vendor | Product |
|---------|----------|
| V1 | P1 |
| V1 | P2 |

**ProductCustomer**
| Product | Customer |
|----------|-----------|
| P1 | C1 |
| P1 | C2 |
| P2 | C1 |

**VendorCustomer**
| Vendor | Customer |
|---------|-----------|
| V1 | C1 |
| V1 | C2 |

### Benefits
- Eliminates redundancy from join dependencies
- Maintains data consistency

---

## 🧠 Summary Table

| Normal Form | Removes | Dependency Type | Example Issue |
|--------------|----------|----------------|----------------|
| 1NF | Repeating Groups | None | Multiple books in one cell |
| 2NF | Partial Dependencies | Composite key → part key | Customer depends only on OrderID |
| 3NF | Transitive Dependencies | Non-key → Non-key | City depends on Pincode |
| BCNF | Non-key determinant | Non-key → key | Professor → Dept |
| 4NF | Multi-valued Dependencies | Independent sets | Course and Hobby |
| 5NF | Join Dependencies | Complex joins | Vendor, Product, Customer |

---

## ✅ Benefits of Normalization
- Reduces redundancy  
- Enhances data integrity  
- Simplifies maintenance  
- Improves query efficiency  
- Provides scalable data structure
