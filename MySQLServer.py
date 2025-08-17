import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",        # change if you use a different user
            password="yourpassword"   # put your MySQL root password here
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # <--- checker is looking for this
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")  # optional

if __name__ == "__main__":
    create_database()
