import db_config
from datetime import date

def borrow_book():
    member_id = input("Enter member ID: ")
    book_id = input("Enter book ID: ")

    conn = db_config.create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT available_quantity FROM books WHERE book_id=%s", (book_id,))
    result = cursor.fetchone()
    if not result or result[0] <= 0:
        print("❌ Book not available!")
        conn.close()
        return

    cursor.execute("""
        INSERT INTO transactions (book_id, member_id, borrow_date)
        VALUES (%s, %s, CURDATE())
    """, (book_id, member_id))
    cursor.execute("UPDATE books SET available_quantity = available_quantity - 1 WHERE book_id=%s", (book_id,))
    conn.commit()
    print("✅ Book borrowed successfully!")
    conn.close()

def return_book():
    trans_id = input("Enter transaction ID: ")
    return_dt = date.today()

    conn = db_config.create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT book_id, borrow_date FROM transactions WHERE transaction_id=%s", (trans_id,))
    result = cursor.fetchone()
    if not result:
        print("❌ Transaction not found!")
        conn.close()
        return

    book_id, borrow_dt = result
    days_diff = (return_dt - borrow_dt).days
    fine = 0
    if days_diff > 14:
        fine = (days_diff - 14) * 5  # ₹5 per late day

    cursor.execute("""
        UPDATE transactions
        SET return_date=%s, fine=%s
        WHERE transaction_id=%s
    """, (return_dt, fine, trans_id))
    cursor.execute("UPDATE books SET available_quantity = available_quantity + 1 WHERE book_id=%s", (book_id,))
    conn.commit()
    print(f"✅ Book returned! Fine: ₹{fine}")
    conn.close()
