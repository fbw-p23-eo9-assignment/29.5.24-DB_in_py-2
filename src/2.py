
import psycopg2

def get_connection():
    connection = psycopg2.connect(user="dci",
                                  password="dci@#21",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="dci_db")
    return connection

def close_connection(connection):
    if connection:
        connection.close()
        print("Postgres connection is closed")

def get_warehouse_detail(warehouse_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Warehouse where Warehouse_Id = %s"""
        cursor.execute(select_query, (warehouse_id,))
        records = cursor.fetchall()
        print("Printing Warehouse record")
        for row in records:
            print("Warehouse Id:", row[0], )
            print("Warehouse Name:", row[1])
            print("Employee Count:", row[2])
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)

def get_employee_detail(Employee_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Employee where Employee_Id = %s"""
        cursor.execute(select_query, (employee_id,))
        records = cursor.fetchall()
        print("Printing Employee record")
        for row in records:
            print("Employee Id:", row[0])
            print("Employee Name:", row[1])
            print("Warehouse Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6])
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)

print("Question 2: Read given warehouse and employee details \n")
get_warehouse_detail(2)
print("\n")
get_employee_detail(105)
