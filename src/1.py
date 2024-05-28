import psycopg2

# connect to DB with your credentials
def get_connection():
    connection = psycopg2.connect(user="dci",
                                  password="dci@#21",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="dci_db")
    return connection

# close connection with this function
def close_connection(connection):
    if connection:
        connection.close()

# check and print postgres version
def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to PostgreSQL version: ", db_version)
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)

print("Question 1: Print Database version")
read_database_version()