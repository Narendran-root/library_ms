import pandas as pd
import db_config

def export_borrowed_books_csv():
    conn = db_config.create_connection()
    query = """
        SELECT m.name, b.title, t.borrow_date, t.return_date, t.fine
        FROM transactions t
        JOIN members m ON t.member_id = m.member_id
        JOIN books b ON t.book_id = b.book_id
    """
    df = pd.read_sql(query, conn)
    df.to_csv("borrowed_books_report.csv", index=False)
    conn.close()
    print("✅ Report exported to borrowed_books_report.csv")
