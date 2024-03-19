# Student Database Application

This application interacts with a PostgreSQL database to perform CRUD (Create, Read, Update, Delete) operations on a `students` table.

## Prerequisites

- Python 3.x
- PostgreSQL database
- `psycopg2` library for Python

## Setup

1. Create a PostgreSQL database for this application.

2. Create the `students` table using the following SQL script:

   ```sql
   CREATE TABLE students (
       student_id SERIAL PRIMARY KEY,
       first_name TEXT NOT NULL,
       last_name TEXT NOT NULL,
       email TEXT NOT NULL UNIQUE,
       enrollment_date DATE
   );

   INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
   ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
   ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
   ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

    ```

3. Execute this SQL script (```createtable.sql```) in pgAdmin or any PostgreSQL client to create the students table and populate it with the initial data.

If not already installed, install the required psycopg2 dependency by running the following command :
 ``` pip install psycopg2-binary ```



## Configuration

1. Open the ```my_db_connect.py``` file in VS Code or any other editor. 

2. Update the following variables based on your actual database details:

```python
    DB_HOST = 'localhost'
    DB_PORT = '5432'
    DB_NAME = 'your_database_name'
    DB_USER = 'your_username'
    DB_PASSWORD = 'your_password' 
```


## Usage

Simply run the python file ```my_db_connect.py``` via terminal. (like ```python file_name.py``` or using the run button in VScode)

This will execute the application and demonstrate the functionality of each function:

Retrieving all students
Adding a new student
Updating a student's email
Deleting a student

Observe the output in the console to see the results of each operation.

The application includes the following functions:

```get_all_students()```: Retrieves and displays all records from the students table.
```add_student(first_name, last_name, email, enrollment_date)```: Inserts a new student record into the students table.
```update_student_email(student_id, new_email)```: Updates the email address for a student with the specified student_id.
```delete_student(student_id)```: Deletes the record of the student with the specified student_id.


Demo Video: https://youtu.be/43ek_vpOghA 

GitHub Repo link: https://github.com/jarnailchahal/COMP-3005-Assignment3-Q1