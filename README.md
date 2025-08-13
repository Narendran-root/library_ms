
# 📚 Library Management & Analytics System (Python + MySQL)

A simple **Library Management System** built with **Python** and **MySQL** to manage books, members, and transactions, with built-in **analytics reports** and **CSV export**.  
This project demonstrates **SQL joins, group by, aggregate functions, subqueries, date functions**, and **Python database integration**.

---

## 🚀 Features
### 📖 Book Management
- Add, update, delete books
- View all available books

### 👤 Member Management
- Add new members
- View member list

### 📦 Borrow & Return System
- Borrow books with quantity tracking
- Return books with late fine calculation (`₹5/day` after 14 days)

### 📊 Reports & Analytics
- **Joins:** List borrowed books with member details
- **Group By & Aggregate:** Borrow counts by category
- **Subqueries:** Books never borrowed, frequent borrowers
- **Date Functions:** Calculate late return fines

### 📤 Export
- Export reports to **CSV** for further analysis

---

## 🗄️ Database Schema

### **books**
| Field              | Type         |
|--------------------|--------------|
| book_id (PK)       | INT          |
| title              | VARCHAR(255) |
| author             | VARCHAR(255) |
| category           | VARCHAR(100) |
| isbn               | VARCHAR(20)  |
| total_quantity     | INT          |
| available_quantity | INT          |

### **members**
| Field             | Type         |
|-------------------|--------------|
| member_id (PK)    | INT          |
| name              | VARCHAR(255) |
| email             | VARCHAR(255) |
| phone             | VARCHAR(15)  |
| membership_date   | DATE         |

### **transactions**
| Field             | Type         |
|-------------------|--------------|
| transaction_id (PK)| INT         |
| book_id (FK)      | INT          |
| member_id (FK)    | INT          |
| borrow_date       | DATE         |
| return_date       | DATE         |
| fine              | DECIMAL(5,2) |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/library-management-system.git
cd library-management-system
````

### 2️⃣ Install Dependencies

```bash
pip install mysql-connector-python pandas tabulate
```

### 3️⃣ Set Up the Database

1. Open **phpMyAdmin** or MySQL CLI.
2. Run:

```sql
CREATE DATABASE library_db;
```

3. Import the provided `library_db.sql` file.

### 4️⃣ Configure Database Connection

Edit `config.py`:

```python
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = ""
DB_NAME = "library_db"
```

### 5️⃣ Run the Application

```bash
python main.py
```

---

## 📂 Project Structure

```
library-management-system/
│
├── main.py          # Main program
├── config.py        # DB connection settings
├── library_db.sql   # Database schema
├── README.md        # Documentation
```

---

## 👨‍💻 Author

**Narendran Subramani**

---






