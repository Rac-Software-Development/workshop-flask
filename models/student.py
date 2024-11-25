from databases.database import Database
class Student:
    def __init__(self, path):
        """
        Initialize the Student class with a reference to the database.
        """
        self.db = Database(path)

    def save_student(self, first_name, last_name, years_on_school, date_of_birth, email, password):
        """
        saves a new student to the database.
        """
        con = self.db.connect()
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO students (first_name, last_name, years_on_school, date_of_birth, email, password) VALUES (?, ?, ?, ?, ?, ?)",
            (first_name, last_name, years_on_school, date_of_birth, email, password))
        con.commit()
        return cursor.lastrowid

    def get_single_student(self, student_id):
        """
        Retrieve a single student's details from the database by ID.
        """
        con = self.db.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        con.commit()
        return cursor.fetchone()

    def get_all_students(self):
        """
        Retrieve all students from the database.
        """
        con = self.db.connect()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM students")
        con.commit()
        return cursor.fetchall()