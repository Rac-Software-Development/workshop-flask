import sqlite3  # Imports the sqlite3 module


class Database:
    def __init__(self, path):
        """
        Initialize the database class with a default path.
        Automatically sets up the required tables.
        """
        self.path = path
        self._setup_tables()

    def connect(self):
        """
        Establish and return a new connection to the database.
        """
        con = sqlite3.connect(self.path)
        con.row_factory = sqlite3.Row  # Returns results as dictionaries
        return con

    def _setup_tables(self):
        """
        Create the students table if it doesn't exist and add default entries.
        """
        with self.connect() as con:
            cursor = con.cursor()

            # Create the students table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    years_on_school INTEGER NOT NULL,
                    date_of_birth TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            ''')
            con.commit()

            # Insert default students if they don't already exist
            default_students = [
                ("Louella", "Creemers", 3, "2005-04-15", "louella.creemers@example.com", "password123"),
                ("Mark", "Otting", 4, "2004-08-20", "mark.otting@example.com", "securepass456"),
                ("Sietze", "van den Bergh", 2, "2006-01-10", "sietze.vdbergh@example.com", "mypassword789"),
                ("Veysel", "Altinok", 1, "2007-09-25", "veysel.altinok@example.com", "password456")
            ]

            for student in default_students:
                cursor.execute('''
                    INSERT INTO students (first_name, last_name, years_on_school, date_of_birth, email, password)
                    SELECT ?, ?, ?, ?, ?, ?
                    WHERE NOT EXISTS (
                        SELECT 1 FROM students
                        WHERE first_name = ? AND last_name = ?
                    )
                ''', (*student, student[0], student[1]))

            con.commit()
