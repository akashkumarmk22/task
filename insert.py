import psycopg2 
import pandas as pd

def insert_data(roll_number, name, marks, subject):
    try:
        connection = psycopg2.connect(
            dbname="postgres",
            user="postgres", 
            password="Akash22",
            host="localhost"
        )
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO students (roll_number, name, marks, subject)
        VALUES (%s, %s, %s, %s)
        """
        record_to_insert = (roll_number, name, marks, subject)
        cursor.execute(insert_query, record_to_insert)

        connection.commit()
        print("Data inserted successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error inserting data", error)
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    insert_data(1, 'Akash', 85, 'Math')
    insert_data(2, 'Rakshu', 92, 'Science')
