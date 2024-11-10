import sqlite3  # Imports the sqlite3 module


class Database(object):
    def __init__(self, path):
        self.path = path  # Ask for the database file path whenever Database() is called

    def connect_db(self):
        con = sqlite3.connect(self.path)  # Make a connection with the database stored in path
        con.row_factory = sqlite3.Row  # Save results in rows instead of a tuple
        cursor = con.cursor()  # Cursor for executing SQL statements
        return cursor, con  # Return the cursor and the db connection

    def setup_student_table(self):
        cursor, con = self.connect_db()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                years_on_school INTEGER NOT NULL,
                dob TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        con.commit()
        con.close()