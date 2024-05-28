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

def create_employee(empolyeeSqlQuery):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = empolyeeSqlQuery
        cursor.execute(sql_select_query)
        records = cursor.fetchall()
        print("Printing new employee record \n")
        
        #get the last entry to database and print details
        last_employee = records[-1]
        
        print("New Employee: ", last_employee) 

        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)

print("Question 5: Insert a record for a new Employee\n")

create_employee("INSERT INTO test (Employee_Id, Employee_Name, Warehouse_Id, Joining_Date, Speciality, Salary, Experience) \
      VALUES ('109', 'Olivia', '2', '2021-09-10', 'Consultant', '67500', NULL)"
)