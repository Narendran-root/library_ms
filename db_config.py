import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",       # Change if you set a different user
        password="",       # Add password if you set one in XAMPP
        database="library_db"
    )
    return connection
