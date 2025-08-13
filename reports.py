import db_config
from tabulate import tabulate

def borrowed_books_with_members():
    conn = db_config.create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, b.title, t.borrow_date 
        FROM transactions t
        JOIN members m ON t.member_id = m.member_id
        JOIN books b ON t.book_id = b.book_id
    """)
    rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(rows, headers, tablefmt="psql"))
    conn.close()

def books_borrowed_by_category():
    conn = db_config.create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT b.category, COUNT(*) AS total_borrowed
        FROM transactions t
        JOIN books b ON t.book_id = b.book_id
        GROUP BY b.category
    """)
    rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(rows, headers, tablefmt="psql"))
    conn.close()
