import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

def db_connect(connection):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(**connection)

        # Create a cursor object using the cursor() method
        cursor = conn.cursor()

        # Execute a SQL query
        cursor.execute("SELECT version();")

        # Fetch result
        record = cursor.fetchone()
        print("\nYou are connected to - ", record, "\n")

        # Execute a SQL query
        cursor.execute("SELECT * FROM users;")

        # Fetch result
        record = cursor.fetchall()
        print("The data is - ", record, "\n")

        for row in record:
            for item in row:
                print(item)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # Close the cursor and connection
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed")

if __name__=="__main__":
    connection = {
        "dbname":os.getenv("POSTGRES_DB"),
        "user":os.getenv("POSTGRES_USER"),
        "password":os.getenv("POSTGRES_PASSWORD"),
        "host":os.getenv("POSTGRES_HOST"),
        "port":os.getenv("POSTGRES_PORT")
        }
    
    db_connect(connection)

    print("\nThe current environment is:", os.getenv("ENVIRONMENT"))