from databases.database import Database


class Student:
    def __init__(self):
        database = Database('./databases/database.db')
        database.setup_student_table()

    def save_student(self, first_name, last_name, years_on_school, date_of_birth, email, password):
        database = Database('./databases/database.db')
        cursor, con = database.connect_db()

        cursor.execute(
            "INSERT INTO students (first_name, last_name, years_on_school, dob, email, password) VALUES (?, ?, ?, ?, "
            "?, ?)",
            (first_name, last_name, years_on_school, date_of_birth, email, password))
        con.commit()
        con.close()

    def get_all_students(self):
        database = Database('./databases/database.db')
        cursor, con = database.connect_db()

        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return students
