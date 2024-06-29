import pandas as pd
from sqlalchemy import create_engine

def read_data():
    try:
        # Update the connection string with your actual PostgreSQL credentials
        engine = create_engine('postgresql+psycopg2://postgres:Akash22@localhost/postgres')
        query = "SELECT * FROM students"
        df = pd.read_sql_query(query, engine)
        df.to_excel("students.xlsx", index=False)
        print("Data exported to Excel successfully")
    except Exception as error:
        print("Error reading data", error)

if __name__ == "__main__":
    read_data()
