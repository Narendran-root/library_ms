import db_config
from tabulate import tabulate

def add_member():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    conn = db_config.create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO members (name, email, phone, membership_date)
        VALUES (%s, %s, %s, CURDATE())
    """, (name, email, phone))
    conn.commit()
    print("✅ Member added!")
    conn.close()

def list_members():
    conn = db_config.create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(rows, headers, tablefmt="psql"))
    conn.close()
