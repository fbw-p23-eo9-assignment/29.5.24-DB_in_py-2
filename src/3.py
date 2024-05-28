import psycopg2
import datetime
from dateutil.relativedelta import relativedelta

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

def update_employee_experience(employee_id):
    # Update Employee Experience in Years
    try:
        # Get joining date
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select Joining_Date from Employee where Employee_Id = %s"""
        cursor.execute(select_query, (employee_id,))
        joining_date = cursor.fetchone()

        # Calculate Experience in years
        joining_date_1 = datetime.datetime.strptime(''.join(map(str, joining_date)), '%Y-%m-%d')
        today_date = datetime.datetime.now()
        experience = relativedelta(today_date, joining_date_1).years

        # Update Employee's Experience now
        connection = get_connection()
        cursor = connection.cursor()
        sql_select_query = """update Employee set Experience = %s where Employee_Id =%s"""
        cursor.execute(sql_select_query, (experience, employee_id))
        connection.commit()
        print("Employee Id:", employee_id, " Experience updated to ", experience, " years")
        close_connection(connection)

    except (Exception, psycopg2.Error) as error:
        print("Error while getting employee's data", error)

print("Question 3: Calculate and Update experience of all employee  \n")
update_employee_experience(101)