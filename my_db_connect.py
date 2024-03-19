import psycopg2

# Database connection details
DB_HOST = 'localhost'  # Hostname of the database server
DB_PORT = '5432'  # Port number of the database server
DB_NAME = 'postgres'  # Name of the database
DB_USER = 'postgres'  # Username for database authentication
DB_PASSWORD = 'postgres'  # Password for database authentication

def get_db_connection():
    """
    Establishes a connection to the database.
    Returns:
        connection: psycopg2 connection object
    """
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return connection

def get_all_students():
    """
    Retrieves all students from the database.
    Returns:
        students: list of tuples representing student records
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    connection.close()
    return students

def add_student(first_name, last_name, email, enrollment_date):
    """
    Adds a new student to the database.
    Args:
        first_name: first name of the student
        last_name: last name of the student
        email: email address of the student
        enrollment_date: date of student enrollment
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s)
    ''', (first_name, last_name, email, enrollment_date))
    connection.commit()
    cursor.close()
    connection.close()

def update_student_email(student_id, new_email):
    """
    Updates the email address of a student.
    Args:
        student_id: ID of the student to update
        new_email: new email address for the student
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE students
        SET email = %s
        WHERE student_id = %s
    ''', (new_email, student_id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_student(student_id):
    """
    Deletes a student from the database.
    Args:
        student_id: ID of the student to delete
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('''
        DELETE FROM students
        WHERE student_id = %s
    ''', (student_id,))
    connection.commit()
    cursor.close()
    connection.close()

# Example usage
print('All students:')
students = get_all_students()
for student in students:
    print(student)

print('\nAdding a new student...')
add_student('Alice', 'Johnson', 'alice.johnson@example.com', '2023-09-03')

print('\nAll students after adding a new student:')
students = get_all_students()
for student in students:
    print(student)

print('\nUpdating student email...')
update_student_email(1, 'john.doe.updated@example.com')

print('\nAll students after updating email:')
students = get_all_students()
for student in students:
    print(student)

print('\nDeleting a student...')
delete_student(2)

print('\nAll students after deleting a student:')
students = get_all_students()
for student in students:
    print(student)



