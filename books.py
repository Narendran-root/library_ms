import db_config
from tabulate import tabulate

def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    category = input("Enter category: ")
    isbn = input("Enter ISBN: ")
    total_qty = int(input("Enter total quantity: "))

    conn = db_config.create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO books (title, author, category, isbn, total_quantity, available_quantity)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, author, category, isbn, total_qty, total_qty))
    conn.commit()
    print("✅ Book added successfully!")
    conn.close()

def update_book():
    book_id = input("Enter book ID to update: ")
    title = input("Enter new title: ")
    author = input("Enter new author: ")
    category = input("Enter new category: ")
    total_qty = int(input("Enter new total quantity: "))

    conn = db_config.create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books 
        SET title=%s, author=%s, category=%s, total_quantity=%s, available_quantity=%s 
        WHERE book_id=%s
    """, (title, author, category, total_qty, total_qty, book_id))
    conn.commit()
    print("✅ Book updated!")
    conn.close()

def delete_book():
    book_id = input("Enter book ID to delete: ")
    conn = db_config.create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
    conn.commit()
    print("✅ Book deleted!")
    conn.close()

def list_books():
    conn = db_config.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(rows, headers, tablefmt="psql"))
    conn.close()
