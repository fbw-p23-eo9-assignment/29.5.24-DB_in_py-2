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

def get_specialist_employee_list(speciality, salary):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """select * from Employee where Speciality=%s and Salary > %s"""
        cursor.execute(sql_select_query, (speciality, salary))
        records = cursor.fetchall()
        print("Printing employees whose specialty is", speciality, "and salary greater than", salary, "\n")
        for row in records:
            print("Employee Id: ", row[0])
            print("Employee Name:", row[1])
            print("Warehouse Id:", row[2])
            print("Joining Date:", row[3])
            print("Specialty:", row[4])
            print("Salary:", row[5])
            print("Experience:", row[6], "\n")
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)

print("Question 4: Get Employees as per given Speciality\n")
get_specialist_employee_list("Driver", 30000)