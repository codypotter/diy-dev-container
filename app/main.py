import psycopg2

def connect():
    try:
        connection = psycopg2.connect(
            user="user",
            password="password",
            host="localhost",
            port="5432",
            database="mydatabase"
        )

        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print(f"You are connected to - {record}\n")

    except Exception as error:
        print(f"Error while connecting to PostgreSQL: {error}")
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    connect()
